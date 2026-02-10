import json

import requests


usd = requests.get("https://cbu.uz/oz/arkhiv-kursov-valyut/json/USD/").json()
rub = requests.get("https://cbu.uz/oz/arkhiv-kursov-valyut/json/RUB/").json()

class Convertor:
    def __init__(self):
        self.usd_rate = float(usd[0]["Rate"])
        self.rub_rate = float(rub[0]["Rate"])    

    def usd_to_uzs(self, amount):
        result = amount * self.usd_rate
        return f"{result:,.2f}"

    def usd_to_rub(self, amount):
        amount_in_uzs = amount * self.usd_rate
        result = amount_in_uzs / self.rub_rate
        return f"{result:,.2f}"

    def uzs_to_usd(self, amount):
        result = amount / self.usd_rate
        return f"{result:,.2f}"

    def uzs_to_rub(self, amount):
        amount_in_usd = amount / self.usd_rate
        result = amount_in_usd * self.rub_rate
        return f"{result:,.2f}"

    def rub_to_usd(self, amount):
        amount_in_uzs = amount * self.rub_rate
        result = amount_in_uzs / self.usd_rate
        return f"{result:,.2f}"

    def rub_to_uzs(self, amount):
        result = amount * self.rub_rate
        return f"{result:,.2f}"