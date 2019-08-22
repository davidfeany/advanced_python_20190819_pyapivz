#!/usr/bin/python3

############################################################################
# curl "http://127.0.0.1:5006/ciscoios?mask=128.0.0.0&mtu=65535&gateway=1.1.1.1" -L
############################################################################


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/ciscoios/")
def ciscoios():
    try:
        qparms = {}
        qparms['switchname'] = request.args.get('switchname', 
                                                'bootstrapped switch')
        qparms['username'] = request.args.get('username', 'admin')
        qparms['defaultgateway'] = request.args.get('gateway', '0.0.0.0')
        qparms['switchIP'] = request.args.get('ip', '0.0.0.0')
        qparms['netmask'] = request.args.get('mask', '255.255.255.0')
        qparms['mtusize'] = request.args.get('mtu', '1450')
        return render_template("baseIOS.conf.j2", **qparms)

    except Exception as err:
        return "uh-oh!  " + str(err)

if __name__ == "__main__":
    app.run(port=5006)


