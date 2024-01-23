from aiogram import Bot
from aiogram.types import CallbackQuery


async def navigation(call: CallbackQuery, bot: Bot):
    print(call.data)
    answer = ''
    if call.data == 'navigation_chat':
        answer = f'ID чата: {call.message.chat.id}'
    elif call.data == 'navigation_user':
        answer = f'ID пользователя: {call.message.from_user.id}'

    await call.message.answer(answer)
    await call.answer()
