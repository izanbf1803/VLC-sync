
from flask import Flask, redirect, url_for, request, render_template
from time import time

app = Flask(__name__)

def global_update():
    t = int(time()*1000)
    dt = t - GLOBAL["last_upd"]
    if GLOBAL["play"] == 1:
        GLOBAL["time"] = max(1, min(
            GLOBAL["time"] + dt,
            GLOBAL["duration"] - 1000
        ))
    GLOBAL["last_upd"] = t

@app.route('/update/')
def update():
    global_update()
    print("upd", GLOBAL["time"])
    return "OK"

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/set_global/<name>/<value>')
def set_global(name, value):
    global GLOBAL
    try:
        GLOBAL[name] = G_TYPE[name](value)
        print("set", name, value)
        return "OK"
    except:
        return "ERROR", 400

@app.route('/get_global/<name>')
def get_global(name):
    global GLOBAL
    try:
        return str(GLOBAL[name])
    except:
        return "ERROR", 400

@app.route('/get_globals/')
def get_globals():
    global GLOBAL
    try:
        global_update()
        return str(GLOBAL).replace("'", '"')
    except:
        return "ERROR", 400

 
if __name__ == '__main__':
    G_TYPE = {}
    GLOBAL = {}
    INIT = [
        ("time", 0, int),
        ("duration", 0, int),
        ("last_upd", 0, int),
        ("play", 0, int)
    ]

    for name, val, typ in INIT:
        GLOBAL[name] = val
        G_TYPE[name] = typ
    app.run(debug=False, threaded=False, host='0.0.0.0', port=8080)
