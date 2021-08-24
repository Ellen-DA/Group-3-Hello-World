from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    name = "Ellen"
    return "Hello, " + name
