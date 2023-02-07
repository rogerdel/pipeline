from flask import Flask
import os
import time

PORT = os.getenv("PORT")

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    return "Hello world"

@app.route("/time", methods= ["GET"])
def get_time():
    return time.strftime("%H:%M:%S", time.localtime())


if __name__ == '__main__':
    app.run("0.0.0.0", PORT)