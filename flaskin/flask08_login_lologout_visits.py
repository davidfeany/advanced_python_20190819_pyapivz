#!/usr/bin/python3

from flask import Flask
from flask import session
from flask import render_template
from flask import redirect
from flask import url_for
from flask import escape
from flask import request

app = Flask("__name__")

app.secret_key = "AnY RaNdOm StRiNG"

@app.route("/")
def index():
    if "username" in session:
        un = session["username"]
        if 'visits' in session:
            session['visits'] = session.get('visits') + 1
        else:
            session['visits'] = 1
        visitno = f"total visits: {session.get('visits')}"

        return  render_template("index1.html", 
                                username=un,
                                visitno=visitno) 

    return render_template("index2.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form.get("username")
        return redirect(url_for("index"))

    else:
        return """
        <form action = "/login" method="POST">
        <p><input type='text' name = username /></p>
        <p><input type='submit' value=login /> </p>
        </form>
        """
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))  # redirect to function index()

@app.route("/delete-visits")
def delete_visits(): 
    if "username" in session:
        session.pop("visits", None)
        return 'visits deleted'
    else:
        return render_template("index2.html")

if __name__ == "__main__":
    app.run(port=5006)
