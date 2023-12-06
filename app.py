from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "PoC by NAP https://hackerone.com/nap65537?type=user"
