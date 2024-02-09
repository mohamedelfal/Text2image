from flask import Flask, render_template, request
from text2image import generate_image

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_image():
    text = request.form["text"]
    image = generate_image(text)
    return render_template("index.html", image=image)

if __name__ == "__main__":
    app.run()
