import requests
from datetime import datetime

class CurrencyConverter:
    def __init__(self, date=None):
        self.date = date or datetime.now().strftime('%Y%m%d')
        self.rate = self.get_exchange_rate()
    def get_exchange_rate(self):
        url = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date={self.date}&json'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                return float(data[0]['rate'])
        raise Exception('Не вдалося отримати курс валют.')
    def convert_to_usd(self, amount_uah):
        if self.rate:
            return amount_uah / self.rate
        else:
            raise Exception('Курс валют не встановлено.')
if __name__ == '__main__':
    try:
        converter = CurrencyConverter()
        amount_uah = float(input('кількість гривень: '))
        amount_usd = converter.convert_to_usd(amount_uah)
        print(f'{amount_uah:.2f} гривень це {amount_usd:.2f}$ доларів.')
    except Exception as e:
        print(f'Помилка: {e}')
