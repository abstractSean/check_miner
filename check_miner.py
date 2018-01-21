from requests import Session
from datetime import datetime
from send_sms import send_sms

def get_last_seen_time(miner_address='b9562a99dcfd11164a8e9b125dddc9867b035b9b'):
    ehtermine_api_url = 'https://api.ethermine.org/'
    miner_status_query = 'https://api.ethermine.org/miner/{}/workers/monitor'.format(miner_address)

    with Session() as r:
        last_seen = r.get(url=miner_status_query).json()['data'][0]['lastSeen']

    return datetime.fromtimestamp(int(last_seen))#.strftime('%Y-%m-%d %H:%M:%S')

def get_last_seen_minutes(last_seen_time):
    return int(round((datetime.now() - last_seen_time).seconds/60))

def main():
    last_seen = get_last_seen_time()
    last_seen_minutes = get_last_seen_minutes(last_seen)
    print('Last seen time: {}'.format(last_seen))
    print('Miner last seen {} minutes ago.'.format(last_seen_minutes))
    if last_seen_minutes > 30:
        send_sms('Miner last seen {} minutes ago.'.format(last_seen_minutes))

if __name__ == '__main__':
    main()


