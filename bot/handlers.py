from telegram import Update
from telegram.ext import CallbackContext


def start_polling(update: Update, context: CallbackContext):
    print("Start is working :) ")
