import requests
import pandas as pd
from bs4 import BeautifulSoup
import smtplib


import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Data:
    def __init__(self):
        SHEET_NAME = "pag1"
        SHEET_ID = "1InWEVnFr2ICuyLQa-w_KmQBcRtemqWpAGQG06TwJHzg"
        self.URL_SHEET = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
        self.df = self.get_data()
    def get_data(self):
        df = pd.read_csv(self.URL_SHEET)
        return df


class Amazon:
    @staticmethod
    def get_price(link):
        response = requests.get(link, headers={
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
                        })
        soup = BeautifulSoup(response.text, "lxml")
        print(soup.find("span", {"id": "productTitle"}).get_text())
        return soup.find("span", {"class": "a-price-whole"}).get_text().replace(".","")


class Mail:
    @staticmethod
    def send_email(msg, mail):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=os.getenv("user"), password=os.getenv("pass"))
            connection.sendmail(from_addr=os.getenv('user'), to_addrs=mail, msg=f"Subject:Amazon Tracker: \n\n{msg}")


if __name__=="__main__":
    data = Data()
    for i,item in data.df.iterrows():
        actual = Amazon.get_price(item['link'])
        if int(actual) <= item['price']:
            Mail.send_email(
                f"item: {item['name']} is now on the price tracked or bellow, price: {int(actual)} please check the link {item['link']} ",
                "mafraelmg@gmail.com")