from datetime import datetime
from unittest.mock import AsyncMock, MagicMock

import pytest
from telegram import Chat, Message, Update, User

from bible_telegram_bot.handlers import ErrorMessages, get_versicle

ERROR_MESSAGE = ErrorMessages.INVALID_PARAMS.formatted


@pytest.mark.parametrize(
    ('context_args', 'expected_content'),
    [
        (
            ['João', '3:16'],
            'Deus amou o mundo',
        ),
        (
            ['Eclesiastes', '3:15', 'NVI'],
            'Aquilo que é, já foi, e o que será, já foi anteriormente',
        ),
        (
            ['Salmos', '23:1-2', 'ARC'],
            'Deitar-me faz em verdes pastos'
            ', guia-me mansamente a águas tranquilas',
        ),
        (
            ['Salmos', '23', 'ARC'],
            ERROR_MESSAGE,
        ),
        (
            ['Mateus', '3a', 'B'],
            ERROR_MESSAGE,
        ),
        (
            ['Apocalipse', '22:44', 'NVT'],
            ERROR_MESSAGE,
        ),
        (
            ['Apocalipse', '22:10-44', 'NVT'],
            'Que a graça do Senhor Jesus esteja com todos',
        ),
    ],
    ids=[
        'default_acf_translation',
        'user_specified_translation',
        'verse_range',
        'error_verse_not_specified',
        'error_invalid_query',
        'max_verse_exceeded_single',
        'max_verse_exceeded_range',
    ],
)
@pytest.mark.asyncio
async def test_get_versicle_sends_correct_message_with_context_args(
    context_args,
    expected_content,
):
    mock_bot = AsyncMock()
    mock_bot.id = 123

    user = User(id=1, first_name='Tester', is_bot=False)
    chat = Chat(id=10, type='private')
    text = MagicMock()
    message = Message(
        message_id=1,
        date=datetime.now(),
        chat=chat,
        from_user=user,
        text=text
    )

    message.set_bot(mock_bot)
    update = Update(update_id=1, message=message)

    mock_context = AsyncMock()
    mock_context.args = context_args

    await get_versicle(update, mock_context)

    assert mock_bot.send_message.called

    args, kwargs = mock_bot.send_message.call_args

    response = kwargs.get('text') or args[1]

    assert expected_content in response
