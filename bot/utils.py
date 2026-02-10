import requests


class Converter:
    def __init__(self):
        usd = requests.get("https://cbu.uz/oz/arkhiv-kursov-valyut/json/USD/").json()
        rub = requests.get("https://cbu.uz/oz/arkhiv-kursov-valyut/json/RUB/").json()

        self.usd_rate = float(usd[0]["Rate"])
        self.rub_rate = float(rub[0]["Rate"])

    def usd_to_uzs(self, amount):
        return round(amount * self.usd_rate, 2)

    def usd_to_rub(self, amount):
        return round((amount * self.usd_rate) / self.rub_rate, 2)

    def uzs_to_usd(self, amount):
        return round(amount / self.usd_rate, 2)

    def uzs_to_rub(self, amount):
        return round((amount / self.usd_rate) * self.rub_rate, 2)

    def rub_to_usd(self, amount):
        return round((amount * self.rub_rate) / self.usd_rate, 2)

    def rub_to_uzs(self, amount):
        return round(amount * self.rub_rate, 2)
