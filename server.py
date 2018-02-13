from flask import Flask
from flask import request
from bot import run

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def receive():
    try:
        run(request.json)
        return ""
    except Exception as e:
        print(e)
        return ""

@app.route("/done", methods=["GET", "POST"])
def done():
    """
    Send a message to me telling me that the thing is done"
    """
    return "the thing is done"
