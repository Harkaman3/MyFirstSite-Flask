from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)


@views.route("/")
@login_required
def home():
    cards = [
        {'img':'static/img/1.jpg', 'title':'куртая картинка 1'},
        {'img':'static/img/2.jpg', 'title':'куртая картинка 2'},
        {'img':'static/img/3.jpg', 'title':'куртая картинка 3'},
        {'img':'static/img/4.jpg', 'title':'куртая картинка 4'},
        {'img':'static/img/5.jpg', 'title':'куртая картинка 5'},
        {'img':'static/img/6.jpg', 'title':'куртая картинка 6'},
        ]
        
        
    return render_template("index.html", cards=cards, user=current_user)


@views.route("/items")
@login_required
def buy():
    return render_template("items.html",user=current_user)

@views.route("/about")
@login_required
def about():
    return render_template("about.html",user=current_user)

@views.route("/faqs")
@login_required
def faqs():
    return render_template("faqs.html",user=current_user)

