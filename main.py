from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import requests

TOKEN = '6797398693:AAF7pvi6ZvG0l8iCtybdh0KTPV3jjCz1mZA'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот, который предоставляет советы. Используй /advice, чтобы получить совет.')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Используй /advice, чтобы получить совет.')

def advice(update: Update, context: CallbackContext) -> None:
    advice_response = requests.get('https://api.adviceslip.com/advice')
    advice_data = advice_response.json()

    advice_text = advice_data['slip']['advice']
    update.message.reply_text(f"Совет: {advice_text}")

def on_text(update: Update, context: CallbackContext) -> None:
    help_command(update, context)

def main() -> None:
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("advice", advice))

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, on_text))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()