from telegram import Update
from telegram.ext import CallbackContext
import requests

from .utils import Converter


def start_command(update: Update, context: CallbackContext):
    first_name = update.message.from_user.first_name

    greeting = (
        f"Assalomu alaykum, {first_name}!\n\n"
        "Bizning *Pul konvertor* botimizga xush kelibsiz.\n\n"
        "Botdan toʻliq foydalanishni bilish uchun /help buyrugʻini bosing."
    )
    update.message.reply_text(greeting)


def help_command(update: Update, context: CallbackContext):
    help_text = (
        "ℹ️ *Yordam*\n\n"
        "🔹 /kurs — 1 USD va 1 RUB necha so‘m ekanini ko‘rsatadi\n\n"
        "🔹 /convert — valyuta aylantirish\n"
        "   Misol: /convert 100 USD UZS"
    )

    update.message.reply_text(help_text)


def convert_command(update: Update, context: CallbackContext):
    if len(context.args) != 3:
        update.message.reply_text("Iltimos formatga rioya qiling: /convert 100 USD UZS")
        return

    amount, from_cur, to_cur = context.args
    from_cur = from_cur.upper()
    to_cur = to_cur.upper()
    try:
        amount = float(amount)
    except ValueError:
        update.message.reply_text("Miqdor raqam bo‘lishi kerak!")
        return

    convertor = Converter()

    result = None
    if from_cur == "USD" and to_cur == "UZS":
        result = convertor.usd_to_uzs(amount)
    elif from_cur == "USD" and to_cur == "RUB":
        result = convertor.usd_to_rub(amount)
    elif from_cur == "UZS" and to_cur == "USD":
        result = convertor.uzs_to_usd(amount)
    elif from_cur == "UZS" and to_cur == "RUB":
        result = convertor.uzs_to_rub(amount)
    elif from_cur == "RUB" and to_cur == "USD":
        result = convertor.rub_to_usd(amount)
    elif from_cur == "RUB" and to_cur == "UZS":
        result = convertor.rub_to_uzs(amount)
    else:
        update.message.reply_text(
            "Kechirasiz, bu valyuta kombinatsiyasi qo‘llab-quvvatlanmaydi."
        )
        return

    update.message.reply_text(f"{amount} {from_cur} = {result} {to_cur}")


def rate(update: Update, context: CallbackContext):
    usd = requests.get("https://cbu.uz/oz/arkhiv-kursov-valyut/json/USD/").json()

    rub = requests.get("https://cbu.uz/oz/arkhiv-kursov-valyut/json/RUB/").json()

    usd_rate = float(usd[0]["Rate"])
    rub_rate = float(rub[0]["Rate"])

    text = (
        "💱 *Bugungi valyuta kurslari:*\n\n"
        f"🇺🇸 1 USD = {usd_rate:,.2f} UZS\n"
        f"🇷🇺 1 RUB = {rub_rate:,.2f} UZS"
    )

    update.message.reply_text(text, parse_mode="Markdown")
