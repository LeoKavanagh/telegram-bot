import os
import requests

# The main URL for the Telegram API with our bot's token
BASE_URL = "https://api.telegram.org/bot{}".format(os.environ['THINGDONE_BOT_TOKEN'])

def receive_message(msg):
    """Receive a raw message from Telegram"""
    try:
        message_text = str(msg["message"]["text"])
        chat_id = msg["message"]["chat"]["id"]
        return message_text, chat_id
    except Exception as e:
        print(e)
        return (None, None)

def handle_message(message_text):
    """Calculate a response to the message"""
    return message_text

def send_message(message_text, chat_id):
    """Send a message to the Telegram chat defined by chat_id"""
    data = {"text": message_text.encode("utf8"), "chat_id": chat_id}
    url = BASE_URL + "/sendMessage"
    try:
        response = requests.post(url, data).content
    except Exception as e:
        print(e)

def run(message):
    """Receive a message, handle it, and send a response"""
    try:
        message_text, chat_id = receive_message(message)
        response = handle_message(message_text)
        send_message(response, chat_id)
    except Exception as e:
        print(e)
