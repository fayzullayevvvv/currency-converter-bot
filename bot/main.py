from telegram.ext import Updater, CommandHandler

from .config import Settings

from .handlers import start_command, help_command, convert_command, rate


def main() -> None:
    updater = Updater(Settings.BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        handler=CommandHandler(command="start", callback=start_command)
    )
    dispatcher.add_handler(
        handler=CommandHandler(command="help", callback=help_command)
    )
    dispatcher.add_handler(
        handler=CommandHandler(command="convert", callback=convert_command)
    )
    dispatcher.add_handler(handler=CommandHandler(command="kurs", callback=rate))

    updater.start_polling()
    updater.idle()
