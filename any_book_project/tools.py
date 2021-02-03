"""
Module contatins functions that analyze Stevenson_data.
Results of functions are used in main module.
"""
import doctest
import pandas as pd
from googlesearch import search


def read_stevenson():
    """
    Returns DataFrame of
    Title, Name, Publisher, Date, Languages
    from titles.csv file.
    """
    df = pd.read_csv("any_book_project/Stevenson_data/titles.csv")

    df = df[["Title", "Name", "Publisher",
             "Date of creation/publication", "Languages"]]

    df = df.fillna(0)

    df = df[(df["Title"] != 0) &
            (df["Name"] == "Stevenson, Robert Louis") &
            (df["Publisher"] != 0) &
            (df["Date of creation/publication"] != 0) &
            (df["Languages"] != 0)]

    return df


def google_links(title: str, publisher: str) -> list:
    """
    Generates a google search link based on title and publisher.

    :title: dfkkw
    :publisher:
    :return: link
    """
    search_line = "Robert Louis Stevenson " + title + " " + publisher + "read"

    for output in search(search_line, lang="en", num=1):

        return output


def empty_language_dict(df) -> list:
    """
    Generates a list of all available languages.

    >>> empty_language_dict(read_stevenson())  #doctest: +ELLIPSIS
    {'Afrikaans': []...}

    >>> type(empty_language_dict(read_stevenson()))
    <class 'dict'>
    """
    language_dict = {}

    column = list(df["Languages"])

    for language in column:

        if language not in language_dict.keys():

            if ";" in language:
                langs = language.split(" ; ")
                for lang in langs:
                    if lang not in language_dict.keys():
                        language_dict[lang] = []
            else:
                language_dict[language] = []

    language_dict = dict(sorted(language_dict.items()))

    return language_dict


# For dropdown item in "base.html"
def language_list(df) -> list:
    """
    Returns a list of all available languages
    for dropdown element on website.

    >>> language_list(read_stevenson()) # doctest: +ELLIPSIS
    ['Afrikaans', 'Bengali', 'Cornish'...]

    >>> type(language_list(read_stevenson()))
    <class 'list'>
    """
    languages = []

    column = list(df["Languages"])
    for language in column:

        if language not in languages:

            if ";" in language:
                langs = language.split(" ; ")

                for lang in langs:

                    if lang not in languages:
                        languages.append(lang)
            else:
                languages.append(language)

    languages.sort()

    return languages


# For table in "country.html"
def language_info_table(df, chosen_language: str, amount_of_results=10) -> list:
    """
    Returns a list of tuples of title, year, publisher and link.

    >>> language_info_table(read_stevenson(), "Ukrainian", 1) #doctest: +ELLIPSIS
    [(1, 'Ostriv skarbiv (1974)', 'Molodʹ', ...)]

    >>> language_info_table(read_stevenson(), "Russian", 1) #doctest: +ELLIPSIS
    [(1, 'Poterpevshie korablekrushenie : roman (1986)', 'Mai︠a︡k', ...)]
    """
    lang_dict = empty_language_dict(df)
    output_list = []
    num = 1

    for row in df.iterrows():

        language = row[1][4]

        if language == chosen_language and \
           language in lang_dict and \
           len(output_list) < amount_of_results:

            title = row[1][0]
            title_year = "{} ({})".format(row[1][0], row[1][3])
            publisher = row[1][2]
            link = google_links(title, publisher)

            line = num, title_year, publisher, link
            num += 1

            if line not in output_list:
                output_list.append(line)

    return output_list


# For table in "all_books.html"
def books_info_table(df, amount_of_results=2598) -> list:
    """
    Returns a list of tuples of title, year, author and publisher.

    >>> books_info_table(read_stevenson().tail(5), 1) #doctest: +ELLIPSIS
    [(1, 'Собрание сочинений в пяти томах, etc. (Под общей редакцией М. Урнова.) (1967)', ...]

    >>> books_info_table(read_stevenson(), 1) #doctest: +ELLIPSIS
    [(1, "'A Penny Plain and Twopence Coloured' ...]
    """
    output_list = []
    num = 1

    for row in df.iterrows():

        if len(output_list) < amount_of_results:

            title_year = "{} ({})".format(row[1][0], row[1][3])
            author = row[1][1]
            publisher = row[1][2]

            line = num, title_year, author, publisher

            num += 1

            output_list.append(line)

    return output_list


# For info in "all_books.html"
def num_of_books(df) -> int:
    """
    Returns the amount of books in the dataset.

    >>> num_of_books(read_stevenson())
    2598
    """
    number = df["Languages"].count()

    return number


# For info in "country.html"
def num_of_books_by_language(df, chosen_language: str) -> int:
    """
    Returns the amount of books in the dataset of a given language.

    >>> num_of_books_by_language(read_stevenson(), "English")
    2396
    >>> num_of_books_by_language(read_stevenson(), "Ukrainian")
    2
    >>> num_of_books_by_language(read_stevenson(), "Russian")
    6
    """
    languages = df[df["Languages"] == chosen_language]
    number = len(languages)

    return number


# For search in "all_books.html"
def find_on_all_books(keyword: str) -> list:
    """
    Function returns a list of tuples where the given keyword appears.

    >>> find_on_all_books("domow") #doctest: +ELLIPSIS
    [(1337, 'Short stories. Selections. Upper Lusatian (1977)', ...]

    >>> find_on_all_books("PRAVDA") #doctest: +ELLIPSIS
    [(1361, 'Sobranie sochineniĭ (1981)', 'Stevenson, Robert Louis', 'Pravda')...]

    >>> find_on_all_books("Hello World")
    []
    """
    info_table = books_info_table(read_stevenson())
    output_list = []

    for info in info_table:
        for elem in info:

            if isinstance(elem, str):

                if keyword.lower() in elem.lower():

                    if info not in output_list:

                        output_list.append(info)

    return output_list


if __name__ == "__main__":
    print(doctest.testmod())
