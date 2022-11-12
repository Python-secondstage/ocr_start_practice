from PIL import Image
from flask import Flask
from flask import render_template
from flask import request
import pyocr


app = Flask(__name__)


img = Image.open("spartacamp_jp.png")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload")
def upload():
    tools = pyocr.get_available_tools()
    tool = tools[0]
    txt = tool.image_to_string(
        img, lang="eng+jpn", builder=pyocr.builders.TextBuilder()
    )
    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)
