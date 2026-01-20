# backend/app.py

"""
Flask Backend for Sports Injury Risk Prediction System

This file initializes the Flask application and defines
the main routes for input handling and prediction.

Model inference and planning logic will be added incrementally.
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend setup complete"

if __name__ == "__main__":
    app.run(debug=True)
