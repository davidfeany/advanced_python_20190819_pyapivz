#!/usr/bin/python3

###########################################################
# curl http://127.0.0.1:5006/login?nm=Dave -L
# firefox http://127.0.0.1:5006/start
# firefox http://127.0.0.1:5006/success/Dave
###########################################################


from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route("/success/<name>")
def success(name):
    return f"Welcome {name}"

@app.route("/start")
@app.route("/")
def start():
    return render_template("postmaker.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    # Browser method
    if request.method == "POST":
        user = request.form.get("nm")
        return redirect(url_for("success", name=user))

    # Provide parameters method
    elif request.method == "GET":
        if request.args.get("nm"):
            user = request.args.get("nm")
        else:
            user = "defaultuser"
        return redirect(url_for("success", name=user))

    # Undefined method
    else:
        return "What the???!!!"
    

if __name__ == "__main__":
    app.run(port=5006)



