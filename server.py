import os
import requests
from flask import Flask, request

app = Flask(__name__)

bot_token = os.environ['THINGDONE_BOT_TOKEN']

def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(bot_token, method)

def process_message(update):
    data = {}

    data['chat_id'] = update['message']['from']['id']
    data['text'] = "The thing is done"

    r = requests.post(get_url('sendMessage'), data=data)

@app.route("/{}".format(bot_token), methods=['POST'])
def process_update():
    if request.method == 'POST':
        update = request.get_json()

        if 'message' in update:
            process_message(update)

        return 'OK', 200

@app.route("/{}/sendMessage".format(bot_token), methods=['GET'])
def send_message():
    """Send a message to the Telegram chat defined by chat_id"""
    data = {"text": "Hi Leo, the thing is done", 
	    "chat_id": "-100c1220063200"}
    try:
        response = requests.post(url, data).content
    except Exception as e:
        print(e)
