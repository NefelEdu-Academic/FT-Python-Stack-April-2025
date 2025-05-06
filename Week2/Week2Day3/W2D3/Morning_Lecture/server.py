from flask import Flask, request, render_template, redirect
from artist import Artist
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


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

@app.route("/home")
def all_artists():
    all_artists = Artist.get_all_artists()
    print(all_artists)
    return render_template("home.html", all_artists=all_artists)
        
if __name__ == "__main__":
    app.run(debug= True)