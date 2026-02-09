from telegram.ext import Updater, CommandHandler

from .config import Settings

from .handlers import start_polling


def main() -> None:
    updater = Updater(Settings.BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        handler=CommandHandler(command="start", callback=start_polling)
    )

    updater.start_polling()
    updater.idle()
