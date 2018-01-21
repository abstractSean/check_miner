# -*- coding: utf-8 -*-
import os
from dotenv import find_dotenv, load_dotenv
from twilio.rest import Client

def send_sms(message='Hello!'):
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)

    twilio_id = os.environ.get('TWILIO_ACCOUNT_SID')
    twilio_auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    twilio_number = os.environ.get('TWILIO_NUMBER')
    my_number = os.environ.get('MY_NUMBER')

    client = Client(twilio_id, twilio_auth_token)

    client.messages.create(to=my_number, from_=twilio_number,
                           body=message)


