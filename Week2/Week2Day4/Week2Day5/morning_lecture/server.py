from flask_app import app
# !Don't forget to import all your controllers here
from flask_app.controllers import author_controller, book_controller
if __name__ == "__main__":
    app.run(debug=True)