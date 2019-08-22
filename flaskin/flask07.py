#!/usr/bin/python3

from flask import Flask, session, render_template, redirect, url_for, escape, request

app = Flask("__name__")

app.secret_key = "AnY RaNdOm StRiNG"

@app.route("/")
def index():
    if "username" in session:
        username = session["username"]
        return  render_template("index1.html", username=username) ##"Logged in as " + username +

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
    return redirect(url_for("index"))
'''
@app.route("/delete-visits")

def delete_visits(): 
    if "username" in session:
        session.pop("visits", none)
        return 'visits deleted'
    else:
        return render_template("index2.html")
'''
if __name__ == "__main__":
    app.run(port=5006)
