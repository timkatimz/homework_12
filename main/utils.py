import json
import logging
from json import JSONDecodeError


def load_posts():
    try:
        with open("posts.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except (JSONDecodeError, FileNotFoundError):
        return "<pre><h2> Не удалось преобразовать файл формата .json <h2></pre>"
    else:
        return data


def search_posts(search_key):
    found_posts = []
    for post in load_posts():
        if search_key in post["content"].lower() and len(search_key) > 0:
            found_posts.append(post)
    logging.info(f"Произведен поиск постов по запросу '{search_key}'")
    return found_posts
