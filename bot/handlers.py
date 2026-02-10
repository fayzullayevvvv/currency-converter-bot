from telegram import Update
from telegram.ext import CallbackContext

from .utils import Convertor


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
        "🔹 *Pul konvertor — yordam*\n\n"
        "Quyidagicha foydalaning:\n\n"
        "1) Oddiy konvertatsiya (buyruq orqali):\n"
        "   /convert 100 USD UZS\n"
        "   — Bu 100 AQSH dollarini soʻmga aylantirishni soʻraydi.\n\n"
        "2) Oddiy format qoidalari:\n"
        "   • Miqdor (raqam) — masalan: 100, 12.5\n"
        "   • Valyuta kodi — 3-harfli kod: USD, UZS, RUB.\n\n"
        "3) Misollar:\n"
        "   /convert 50 USD UZS\n"
        "   /convert 1000 UZS RUB\n\n"
        "Eslatma: real kurslar uchun bot internetdan kurslarni oladi."
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

    convertor = Convertor()

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
