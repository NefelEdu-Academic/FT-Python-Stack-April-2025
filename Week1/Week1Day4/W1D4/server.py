from flask import Flask, render_template # type: ignore
app = Flask(__name__)

@app.route("/welcome")
def index():
    return "Hello World!"

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/users")
def get_users():
    users=[
        {"id": 1, "username": "Alice"},
        {"id": 2, "username": "Bob"},
        {"id": 3, "username": "Charlie"},
        {"id": 4, "username": "Diana"}
    ]
    return render_template("users.html", all_users =users)

@app.route("/home/<username>")
def hello_user(username):
    return render_template("user.html", username= username)

@app.route("/numbers/<int:num>/<color>")
def numbers(num, color):
    return render_template("num.html", num=num, color=color)

if __name__ == "__main__":
    app.run(debug = True, port=5001)