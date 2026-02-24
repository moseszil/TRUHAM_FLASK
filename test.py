# Importing flask to our application
from flask import *
# Initializing the flask app 
app  = Flask(__name__)
# Defining a simple route or an endpoint
# this route corresponds to a web application function 
@app.route("/api/home")
# This is the function that runs when the route is accessed
def home():
    return jsonify({'message':'Welcome To Home API'})


# Define a simple ruote 
@app.route("/api/products")
# Function corresponding to the route
def products():
    return jsonify({'message' : 'Welcome To Products API!'})


@app.route("/api/services")
def services():
    return jsonify({'response': 'This is our services API'})

# Runs the app when this file is executed
app.run(debug=True)