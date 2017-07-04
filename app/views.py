from app import app
from flask import render_template

@app.route('/')
def test():
    return render_template("test.html")

@app.route('/create')
@app.route('/index')
def create():
    return render_template("create.html")
