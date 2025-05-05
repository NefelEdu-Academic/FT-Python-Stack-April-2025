from flask_app.models.user_model import User
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
# which is made by invoking the function Bcrypt with our app as an argument


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=['POST'])
def register():
    if User.validate_user(request.form):
        password_hashed = bcrypt.generate_password_hash(request.form['password'])
        data={
            **request.form,
            "password": password_hashed
        }
        id =User.register(data)
        session['user_id']=id
        return redirect("/dashboard")
    return redirect('/')

@app.route("/dashboard")
def dashboard():
    # Route guard
    if "user_id" not in session:
        return redirect("/")
    user = User.get_by_id({"id": session['user_id']})
    return render_template("dashboard.html", user=user)

@app.route("/login", methods=['POST'])
def login():
    user_from_db= User.get_by_email({"email": request.form['email']})
    # if user_from_db == False:
    if not user_from_db:
        flash("Wrong email or Password", "login")
        return redirect('/')
    elif not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
        flash("Wrong email or Password", "login")
        return redirect("/")
    session['user_id']=user_from_db.id
    return redirect("/dashboard")

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect("/")