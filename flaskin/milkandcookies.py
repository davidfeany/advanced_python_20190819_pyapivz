#!/usr/bin/python3

############################################################################
#  connect to DB and pull info needed to create html
############################################################################


from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/index")
@app.route("/")
def index():
    # can create function to connect to DB
    # can create function to pull info from DB
    try:
        return render_template("index.html")

    except Exception as err:
        return "uh-oh!  " + str(err)

@app.route("/setcookie", methods = ["POST", "GET"])
def setcookie():
    if request.method == "POST":
        user = request.form.get("nm")
        if user == None:
            return "uh-oh!  Could not POST in setcookie()"
        resp = make_response(render_template("readcookie.html"))
        resp.set_cookie("userID", user)
        return resp

    elif request.method == "GET":
        return render_template("index.html")

@app.route("/getcookie")
def getcookie():
    username = request.cookies.get("userID")
    #return f"Welcome back, {username}"
    return render_template("helloname.html", name=username)


if __name__ == "__main__":
    #app.run(port=5006)                   # Bind to localhost
    #app.run(port=5006, host="127.0.0.1") # Bind to localhost
    app.run(port=5006, host="0.0.0.0")    # Bind to any IP


