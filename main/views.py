from flask import Blueprint, request, render_template
from main.utils import search_posts

main = Blueprint("main", __name__, template_folder="templates")


@main.route("/")
def main_page():
    return render_template("index.html")


@main.route("/search/")
def search_page():
    search_key = request.args.get("s")
    found_posts = search_posts(search_key)
    return render_template("post_list.html", search_key=search_key, found_posts=found_posts)
