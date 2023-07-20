import string
import random

from flask import Flask,render_template, redirect, request

app = Flask(__name__)
shortenend_url = {}


def genereate_url(length=6):
    chars = string.ascii_letters + string.digits
    short_url = "".join(random.choice(chars) for _ in range(length))
    return short_url

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        long_url = request.form['long_url'];
        short_url = genereate_url()
        while short_url in shortenend_url:
            short_url = genereate_url()

        shortenend_url[short_url] = long_url
        return f"Shortenend URL : {request.url_root}{short_url}"
    return render_template("index.html")

@app.route("/<short_url>")

def redirect_url(short_url) :
    long_url = shortenend_url.get(short_url)
    if long_url:
        return  redirect(long_url)
    else :
        return "URL NOT FOUND", 404

if __name__ == "__main__" :
    app.run(debug=True)