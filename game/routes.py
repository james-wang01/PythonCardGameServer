from flask import render_template, redirect, url_for
from game import myGame
from game.forms import CreateGame, JoinGame, EnterNameEven, EnterNameOdd

@myGame.route("/")
@myGame.route("/index")
def index():
    return render_template("index.html", title="Home")

@myGame.route("/startAGame", methods=["GET", "POST"])
def startAGame():
    form = CreateGame()
    if form.validate_on_submit():
        return redirect(url_for("index"))
    return render_template("startAGame.html", title="Start", form=form)

