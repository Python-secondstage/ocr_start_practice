from flask import Flask
from flask import render_template
from flask import request
from PIL import Image
import pyocr

app = Flask(__name__)


@app.route("/")
def index2():
    return render_template("index2.html")


@app.route("/upload", methods=["POST"])
def upload():
    # リクエストファイルの読み込み
    ocr_file = request.files["ocrFile"]
    img = Image.open(ocr_file)
    # print('POST UPLOAD')

    # OCR準備
    tools = pyocr.get_availzble_tools()
    tool = tools[0]
    # OCR
    txt = tool.image_to_string(
        img,
        lang="eng+jpn",
        builder=pyocr.builders.TextBuilder()
    )
    # print(txt)
    if txt == "":
        txt = "読み取りエラー"
    return render_template("index2.html", txt=txt)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
