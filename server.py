import os
from flask import Flask
from flask import request
from bot import run, send_message

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def receive():
    try:
        run(request.json)
        return "Hello"
    except Exception as e:
        print(e)
        return "error of some description"

@app.route("/done", methods=["GET", "POST"])
def done():
    """
    Send a message to me telling me that the thing is done
    """
    try:
        send_message("The thing is done", os.environ['TELEGRAM_CHAT_ID'])
    except:
        return "I tried to send the message to you but it didn't work"
    return "The thing happened"
