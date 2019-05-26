#!/home/sean/virtualenvs/check_miner/bin/python

import os
import sys
from httplib2 import Http
from json import dumps

from dotenv import find_dotenv, load_dotenv

def send_hangouts(message='Hello!'):
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)

    url = os.environ.get('HANGOUTS_WEBHOOK')
    bot_message = {'text' : f'{message}'}

    message_headers = {
        'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(uri=url,
                                method='POST',
                                headers=message_headers,
                                body=dumps(bot_message),
                               )

    #print(response)

if __name__ == '__main__':
    try:
        send_hangouts(sys.argv[1])
    except IndexError:
        send_hangouts()
