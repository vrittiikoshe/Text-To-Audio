from flask import Flask, render_template, request
from gtts import gTTS
import os

app = Flask(__name__)

# Start Page
@app.route("/")
def start():
    return render_template("start.html")

# Converter Page
@app.route("/convert", methods=["GET", "POST"])
def convert():
    audio_file = None

    if request.method == "POST":
        text = request.form.get("text")

        if text and text.strip():
            audio_dir = os.path.join("static", "audio")
            os.makedirs(audio_dir, exist_ok=True)

            audio_file = os.path.join(audio_dir, "audiobook.mp3")

            tts = gTTS(text=text.strip(), lang="en")
            tts.save(audio_file)

    return render_template("index.html", audio_file=audio_file)


if __name__ == "__main__":
    app.run(port=5001)
