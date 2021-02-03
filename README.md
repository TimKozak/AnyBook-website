-----------------------------------------------------------


^ANY.BOOK website is made for easy acces to Robert Louis Stevenson books.
You can search by his books by region (and recieve google links to every book), 
by year, by publisher, by title and by parts of a title.

This program uses dataset that contains infromation about books of Robert Louis Stevenson. 


-----------------------------------------------------------


How to use the program:
Run launch_website module and click on go to http://127.0.0.1:5000/ to view the webpage.


-----------------------------------------------------------


Structure must look like this:

├── LICENSE
├── README.md
├── setup.py
├── launch_website.py
├── tests
└── any_book_project
    ├── __init__.py
    ├── main.py
    ├── tools.py
    ├── templates
        ├── about.html
        ├── all_books.html
        ├── base.html
        └── country.html
    ├── static
        └── book.jpg
    └── Stevenson_data
        ├── titles.csv
        └── Readme - Robert Louis Stevenson.txt


-----------------------------------------------------------


The result of a program is a website that allows you to easily discover Robert Louis Stevenson's books, 
find out the amount of languages they were translated, read/buy them via google links that are provided to every book, 
search books by any character that is in it's title, publisher or date.
