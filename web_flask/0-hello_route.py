#!/usr/bin/python3
"""# Import the necessary modules
from flask import Flask

# Create a Flask application object
app = Flask(__name__)

# Define a route and a function to handle requests
@app.route('/airbnb-onepage/')
def hello():
    return "Hello, this is your Airbnb clone content!"

    # Run the app on port 5000
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
        )
