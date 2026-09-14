from flask import Flask, render_template
import sqlite3
from dbclass import *
from db import *

app = Flask(__name__)

init_db()

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)