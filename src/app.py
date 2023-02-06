from flask import Flask
import os

PORT = os.getenv("PORT")

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    return "Hello world"



app.run("0.0.0.0", PORT)