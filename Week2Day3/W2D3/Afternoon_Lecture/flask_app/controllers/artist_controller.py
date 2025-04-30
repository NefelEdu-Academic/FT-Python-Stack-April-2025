from flask import Flask, request, render_template, redirect
from flask_app.models.artist_model import Artist
from flask_app import app

# -------Create Artist
# ?GET route : to see the form
@app.route("/")
def index():
    return render_template("index.html")

# ?Action route to handle data after submission
@app.route("/create", methods=['POST'])
def create():
    dict_data={
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "rate": request.form['rate'],
        "image": request.form['image'],
        "style": request.form['style'],
        
    }
    
    if "is_popular" in request.form:
        dict_data['is_popular']=1
    else:
        dict_data['is_popular']=0
    Artist.create_artist(dict_data)
    return redirect("/home")
# ------------Display All Artists
# ?GET route to display all artists
@app.route("/home")
def all_artists():
    all_artists = Artist.get_all_artists()
    print(all_artists)
    return render_template("home.html", all_artists=all_artists)


# --------------Update Artist
# ?Display route for displaying edit form
@app.route("/edit/<int:id>")
def edit(id):
    artist= Artist.get_one_artist({"id": id})
    return render_template("edit.html", id=id, artist= artist)

# ?Action route to handle updated data
@app.route("/update/<int:id>", methods=['POST'])
def update(id):
    data={
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "rate": request.form['rate'],
        "image": request.form['image'],
        "style": request.form['style'],
    }
    if "is_popular" in request.form:
        data['is_popular']=1
    else:
        data['is_popular']=0
    data['id']=id
    Artist.update(data)
    return redirect("/home")
# ?action route for deleteing artist
@app.route("/delete/<int:id>", methods=['POST'])
def delete(id):
    Artist.delete({"id":id})
    return redirect("/home")

# ?Display route for showing one artist
@app.route("/show/<int:id>")
def show(id):
    artist = Artist.get_one_artist({"id":id})
    return render_template("show.html", artist= artist)
