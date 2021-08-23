from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    name = input("Name: ").title()
    return "Hello, " + name
