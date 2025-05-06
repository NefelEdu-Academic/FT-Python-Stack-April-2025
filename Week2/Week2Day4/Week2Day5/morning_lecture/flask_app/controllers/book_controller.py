from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author_model import Author
from flask_app.models.book_model import Book

@app.route("/book/new")
def create_book():
    all_authors= Author.get_all()
    return render_template("new_book.html", all_authors=all_authors)

@app.route("/create/book", methods=['POST'])
def new_book():
    Book.create(request.form)
    return redirect("/")

@app.route("/books/<int:author_id>")
def authors_books(author_id):
    author = Author.get_one_by_id_with_books({"id": author_id})
    return render_template("my_books.html", author= author)