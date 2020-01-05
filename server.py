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


@app.route("/msg", methods=["GET", "POST"])
def msg():
    """
    Send a message in headers
    """

    text = request.headers.get('msg')

    try:
        send_message(text, os.environ['TELEGRAM_CHAT_ID'])
    except Exception as e:
        msg = "I tried to send the message to you " \
              "but it didn't work: {} - {}".format(type(e), e)
        return msg
    return "Sent message to you on Telegram: {}".format(text)

