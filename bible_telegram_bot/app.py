import os

from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

from bible_telegram_bot.registry import CommandRegistry

load_dotenv()

TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

app = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()

app.add_handler(
    CommandHandler(
        CommandRegistry.GET_VERSICLE.trigger, CommandRegistry.GET_VERSICLE.action
    )
)

app.run_polling()
