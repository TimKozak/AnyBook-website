"""
Module that connects HTML script with database analysis functions.
To start a website you need to run code from this module.
"""
from flask import Flask, render_template, request
from any_book_project.tools import read_stevenson, language_list, num_of_books, \
                  num_of_books_by_language, books_info_table, \
                  language_info_table, find_on_all_books

app = Flask(__name__)

dataset = read_stevenson()
languages = language_list(dataset)


@app.route("/all_books", methods=['GET', 'POST'])
@app.route("/")
def all_books():
    """
    Generates a webpage with count of books and information
    table about all books in the dataset.
    """
    books = num_of_books(dataset)
    info_table = books_info_table(dataset, books)
    noresult = ""

    if request.method == 'POST':

        msg = request.form.get('msg')
        info_table = find_on_all_books(str(msg))

        if len(info_table) == 0:
            noresult = "No results found"

        return render_template("all_books.html", language_list=languages, books=books, \
                                                 info_table=info_table, msg=msg, noresult=noresult)


    return render_template("all_books.html", language_list=languages, books=books, \
                                             info_table=info_table, noresult=noresult)


@app.route("/<language>")
def country(language):
    """
    Generates a webpage with count of books and information
    table about all books for every given language.
    """
    books = num_of_books_by_language(dataset, language)
    info_table = language_info_table(dataset, language, 10)

    return render_template("country.html", language_list=languages, language=language, \
                                           books=books, info_table=info_table)


@app.route("/about")
def about():
    """
    Generates a webpage with description of the project.
    """
    return render_template("about.html", language_list=languages)


def launch_website():
    """
    Function that launches the website.
    """
    app.run()
