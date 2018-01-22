#!/home/sean/virtualenvs/check_miner/bin/python

import os
import sys
from requests import Session
from datetime import datetime
from dotenv import find_dotenv, load_dotenv
from send_sms import send_sms

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

my_miner_address = os.environ.get('MINER_ADDRESS')


def get_last_seen_time(miner_address=my_miner_address):
    ehtermine_api_url = 'https://api.ethermine.org/'
    miner_status_query = 'https://api.ethermine.org/miner/{}/workers/monitor'.format(miner_address)

    with Session() as r:
        last_seen = r.get(url=miner_status_query).json()['data'][0]['lastSeen']

    return datetime.fromtimestamp(last_seen)

def get_last_seen_minutes(last_seen_time):
    return int(round((datetime.now() - last_seen_time).seconds/60))

def main(threshold_mins=30):
    last_seen = get_last_seen_time()
    last_seen_minutes = get_last_seen_minutes(last_seen)
    print('Last seen time: {}'.format(last_seen))
    print('Miner last seen {} minutes ago.'.format(last_seen_minutes))
    if last_seen_minutes > threshold_mins:
        send_sms('Miner last seen {} minutes ago.'.format(last_seen_minutes))

if __name__ == '__main__':
    try:
        main(int(sys.argv[1]))
    except IndexError:
        main()
