import json

import requests


usd = requests.get("https://cbu.uz/oz/arkhiv-kursov-valyut/json/USD/").json()
rub = requests.get("https://cbu.uz/oz/arkhiv-kursov-valyut/json/RUB/").json()

usd_rate = float(usd[0]["Rate"])
rub_rate = float(rub[0]["Rate"])

def usd_to_uzs(amount):
    result = amount * usd_rate
    return f"{result:,.2f}"

def usd_to_rub(amount):
    amount_in_uzs = amount * usd_rate
    result = amount_in_uzs / rub_rate
    return f"{result:,.2f}"

def uzs_to_usd(amount):
    result = amount / usd_rate
    return f"{result:,.2f}"

def uzs_to_rub(amount):
    amount_in_usd = amount / usd_rate
    result = amount_in_usd * rub_rate
    return f"{result:,.2f}"

def rub_to_usd(amount):
    amount_in_uzs = amount * rub_rate
    result = amount_in_uzs / usd_rate
    return f"{result:,.2f}"

def rub_to_uzs(amount):
    result = amount * rub_rate
    return f"{result:,.2f}"