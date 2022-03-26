from flask import Flask
from main.views import main
from loader.views import loader
import logging

UPLOAD_FOLDER = "uploads/images"


app = Flask(__name__)
logging.basicConfig(filename="logs.log", level=logging.INFO)
app.config["UPLOAD_FOLDER"] = "UPLOAD_FOLDER"
app.register_blueprint(main)
app.register_blueprint(loader)


if __name__ == "__main__":
    app.run(debug=True)

