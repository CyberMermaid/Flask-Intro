from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# Build a simple calculator with Flask, which uses URL query parameters to get the numbers to calculate with.
# Make a Flask app that responds to 4 different routes.
# Each route does a math operation with two numbers, ***a*** and ***b***, which will be passed in as URL GET-style query parameters.

# ***/add***   Adds ***a*** and ***b*** and returns result as the body.
# ***/sub***   Same, subtracting ***b*** from ***a***.
# ***/mult***   Same, multiplying ***a*** and ***b***.
# ***/div***   Same, dividing ***a*** by ***b***.

# For example, a URL like ***http://localhost:5000/add?a=10&b=20*** should return a string response of exactly **30**.
# Write the routes for this.


@app.route("/add")
def add():
    # return sum
    a = request.args["a"]
    b = request.args["b"]
    return f"{add(a, b)}"


@app.route("/sub")
def add():
    # return difference
    a = request.args["a"]
    b = request.args["b"]
    return f"{sub(a, b)}"


@app.route("/mult")
def mult():
    # return product
    a = request.args["a"]
    b = request.args["b"]
    return f"{mult(a, b)}"


@app.route("/div")
def div():
    # return quotient
    a = request.args["a"]
    b = request.args["b"]
    return f"{div(a, b)}"
