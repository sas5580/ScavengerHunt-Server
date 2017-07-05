from app import app, Game
from flask import render_template

@app.route('/')
def test():
    return Game.get_by_key(Game.get_list()[0]).key + render_template("test.html")

@app.route('/create')
@app.route('/index')
def create():
    return render_template("create.html")
