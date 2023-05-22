from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://media.tenor.com/MINogBSXIpcAAAAM/dog.gif",
    "https://media.tenor.com/JtazXURiW6kAAAAM/dog.gif",
    "https://media.tenor.com/YGDMt2ZOFlsAAAAM/dog.gif",
    "https://media.tenor.com/Egt2H3v94ZYAAAAM/dog-pool.gif",
    "https://media.tenor.com/zB332adxbhgAAAAM/cute-dog-unexpected.gif",
    "https://media.tenor.com/JIgNM-eR2pYAAAAM/dog.gif",
    "https://media.tenor.com/aVwPGJ5SOHkAAAAM/dog.gif",
    "https://media.tenor.com/ppCwE74b5UIAAAAM/kirr.gif",
    "https://media.tenor.com/Mq-_bbmxrNsAAAAM/dressed-dog-viralhog.gif",
    "https://media.tenor.com/XnPAw_TO1fIAAAAM/dog.gif",
    "https://media.tenor.com/JHAtTk7HhOoAAAAM/cute-dog.gif",
    "https://media.tenor.com/rGqEYtuMNF4AAAAM/dog-armadillo.gif"
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
