from flask import Flask

app = Flask(__name__)
# Put your app in here.
# Make a simple Flask app that responds to these routes with simple text messages:

# ***/welcome***   Returns “welcome”

# ***/welcome/home***   Returns “welcome home”

# ***/welcome/back***   Return “welcome back”


@app.route("/welcome")
def say_welcome():
    return "welcome"


@app.route("/welcome/home")
def say_welcome_home():
    return "welcome home"


@app.route("/welcome/back")
def say_welcome_back():
    return "welcome back"
