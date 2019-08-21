#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

# Decorators
@app.route("/hello/")
@app.route("/hello")
@app.route("/")
def hello_world():
    with open("helloworld.txt", "w") as hello:
        hello.write("You just wrote this line into helloworld.txt")
    return "Hello World! File created.\n"

@app.route("/goodbye/")
@app.route("/goodbye")
def goodbye_world():
    return "Goodby!  See ya!\n"


if __name__ == "__main__":
    app.run(port=5006)

