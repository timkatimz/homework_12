from flask import Blueprint, request, render_template, send_from_directory
from loader.utils import get_add_posts
import logging

ALLOWED_EXTENSIONS = {"jpg", "png", "jpeg"}

loader = Blueprint("loader", __name__, template_folder="templates")


@loader.route("/post/", methods=["GET"])
def upload_page():
    return render_template("post_form.html")


@loader.route("/post/", methods=["POST"])
def upload_done():
    try:
        picture = request.files.get("picture")
        content = request.form.get("content")
        filename = picture.filename
        extension = filename.split(".")[-1]
        if extension in ALLOWED_EXTENSIONS:
            picture.save(f"uploads/images/{filename}")
        else:
            logging.info(f"Ошибка. Попытка загрузки файла формата '{extension}'")
            return f"<pre><h2> Упс! Файлы формата {extension} не поддерживаются. <h2></pre>"
        picture_url = f"./../uploads/images/{filename}"
        get_add_posts(picture_url, content)
    except FileNotFoundError:
        logging.error("Ошибка при загрузке файла")
        return "<pre><h2> Ошибка загрузке файла. Попробуйте ещё раз <h2></pre>"
    else:
        return render_template("post_uploaded.html", filename=filename, content=content, picture_url=picture_url)


@loader.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)
