import pandas as pd

def parse_log(logfile='cron.log'):

    with open(logfile, 'r') as log:
        lines = [line for line in log]

    dates = [line for line in lines if line[0]=='L']
    dates = [date.split(': ')[1].strip() for date in dates]

    minutes = [line for line in lines if line[0]=='M']
    minutes = [minute.split(' ')[3].strip() for minute in minutes]

    df = pd.DataFrame(pd.to_numeric(minutes), index=pd.to_datetime(dates))
    df.columns = ['minutes']
    return df

if __name__ == '__main__':
    main()
