from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)


@views.route("/")
@login_required
def home():
    cards = ['static/img/1.jpg','static/img/2.jpg','static/img/3.jpg','static/img/1.jpg','static/img/2.jpg','static/img/3.jpg']
    return render_template("index.html", cards=cards, user=current_user)


@views.route("/buy")
def buy():
    return render_template("items.html")
