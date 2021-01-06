from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def home():
    return "Welcome"

@app.route('/welcome/home')
def welcom_home():
    return "Welcome home"

@app.route('/welcome/back')
def welcome_back():
    return "Welcome back"

