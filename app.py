# !/usr/bin/python
# -- coding: utf-8 --
from flask import Flask, request, render_template, redirect, url_for, abort, jsonify
from gevent import pywsgi
from bingApi import handleResult

app = Flask(__name__)
app.debug = True
app.config["JSON_AS_ASCII"] = False


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")



@app.route("/api/v1/bing")
def bingImageData():
    data = handleResult()
    return jsonify(data)


@app.route("/api/v1/bing/t")
def bingImageApi():
    data = handleResult()
    return redirect(data["data"]["url"])


@app.route("/bing/index")
def bingImageDownload():
    data = handleResult()
    return render_template("bing.html", bing=data)


server = pywsgi.WSGIServer(('0.0.0.0', 54321), app)
server.serve_forever()
