from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author_model import Author
@app.route("/")
def index():
    all_authors= Author.get_all()
    return render_template("index.html", all_authors=all_authors)

@app.route("/create/author", methods=['post'])
def create():
    # data={
    #     "author_name": request.form['author_name'],
    #     "style": request.form['style']
    # }
    # Author.author_create(data)
    Author.author_create(request.form)
    return redirect("/")
    