import os
from pprint import import pprint
import requests

# Telegram botfather will give you this
bot_token = os.environ['THINGDONE_BOT_TOKEN']

# The place where the code is running; ngrok or AWS Lambda or wherever
deployed_url = os.environ['THINGDONE_BOT_DEPLOYED_URL']

test_url = deployed_url + "/{}".format(bot_token)

def get_url(method):
        return "https://api.telegram.org/bot{}/{}".format(bot_token,method)

    r = requests.get(get_url("setWebhook"), data={"url": test_url})
    r = requests.get(get_url("getWebhookInfo"))
    pprint(r.status_code)
    pprint(r.json())
