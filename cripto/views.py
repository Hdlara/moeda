import time
import requests as requests
from .models import CandleStick
from datetime import datetime


# function to add candle to table
def interval_add(data):
    try:
        CandleStick.objects.create(
            dolar=data[0],
            euro=data[1],
            jpy=data[2],
            real=data[3],
            period=data[4],
        )
    except:
        pass

def generate_chart(self):
    print('Chamada iniciada')
    while True:
        # Poloniex api call
        price = requests.get(
            'https://api.vatcomply.com/rates?base=USD').json()

        data = [
            price["rates"]["USD"],
            price["rates"]["EUR"],
            price["rates"]["JPY"],
            price["rates"]["BRL"],
            datetime.now().strftime("%Y-%m-%d %H:%M")
        ]
        interval_add(data)
        time.sleep(30)
