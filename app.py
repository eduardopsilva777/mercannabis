from flask import Flask, render_template, send_file, Response, request, jsonify, url_for, flash
import requests
from dbclass import *
from db import *

app = Flask(__name__)

init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/adicionar")
def adicionar_produto():
    None



if __name__ == "__main__":
    app.run(debug=True)