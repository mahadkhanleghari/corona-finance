import pandas as pd
from datetime import datetime
def daily_report(date):
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/' \
          'csse_covid_19_data/csse_covid_19_daily_reports/{date}.csv'.format(date=date)
    df = pd.read_csv(url)
    return df

if __name__ == "__main__":
    date = "03-23-2020"
    df = daily_report(date)
    df.to_csv("/Users/mahadafzal/corona/test_data.csv")
    print(df.describe()
    print(df.head())

