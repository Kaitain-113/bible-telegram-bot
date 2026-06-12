from bible_cli.processor import QueryProcessor
from telegram import Update
from telegram.ext import ContextTypes


def fetch_versicle_data(query: str):
    processor = QueryProcessor()
    return processor.process_query(query)


async def get_versicle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = ' '.join(context.args)
    versicle = fetch_versicle_data(query)
    await update.message.reply_text(versicle)
