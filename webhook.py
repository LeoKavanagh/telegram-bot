import os
from pprint import pprint
import requests

bot_token = os.environ['THINGDONE_BOT_TOKEN']
test_url = "https://8e67a859.ngrok.io/{}".format(bot_token)

def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(bot_token, method)

r = requests.get(get_url('setWebHook'), data={'url': test_url})
r = requests.get(get_url('getWebhookInfo'))

pprint(r.status_code)
pprint(r.json())
