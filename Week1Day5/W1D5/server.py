from flask import Flask, render_template, request, redirect, session #type: ignore

app = Flask(__name__)
app.secret_key = "super secret key here"
# display route
@app.route("/")
def form():
    return render_template("form.html")
# action route
@app.route("/submit_form", methods=['POST'])
def form_action():
    print(request.form)
    print("*"*100)
    username_variable = request.form['username']
    email_variable = request.form['email']
    session['user'] = username_variable
    session['email'] = email_variable
    # return f"Name: {username_variable}, email: {email_variable}"
    # !NEver ever render template on method POST
    return redirect("/display")
# display route
@app.route("/display")
def display_data():
    u= session['user']
    msg= u+", "
    return render_template("display.html",u=msg)

# action route
@app.route("/reset", methods=['POST'])
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)