from enum import StrEnum
from typing import Optional

from bible_cli.processor import QueryProcessor
from telegram import Update
from telegram.ext import ContextTypes

DEFAULT_TRANSLATION = 'ACF'
EXPECTED_ARGS_LENGTH = 3


class ErrorMessages(StrEnum):
    INVALID_PARAMS = 'Parâmetros inválidos.'

    @property
    def formatted(self) -> str:
        info_example = 'Tente enviar algo: Eclesiastes 3:15 ARA'
        return f'{self.value} {info_example}'


def fetch_versicle_data(query: str) -> Optional[str]:
    try:
        processor = QueryProcessor()
        return processor.process_query(query)
    except ValueError:
        return None


async def get_versicle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    parsed_args = context.args.copy()

    if len(context.args) < EXPECTED_ARGS_LENGTH:
        parsed_args.append(DEFAULT_TRANSLATION)

    query = ' '.join(parsed_args)
    query_result = fetch_versicle_data(query)

    message_text = (
        query_result
        if query_result
        else ErrorMessages.INVALID_PARAMS.formatted
    )

    await update.message.reply_text(message_text)
