from flask import Flask

app = Flask(__name__)
DB="login_registration_schema"
app.secret_key="Super secret key"