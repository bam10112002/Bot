from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery

from Bot.buttons import get_keyboard_all_audience, get_keyboard_contact, get_keyboard_main, get_keyboard_nav
from config import room


async def navigation(call: CallbackQuery):
    print(call.data)
    answer = ''
    mrkp = None
    is_edit = False
    if call.data == 'navigation_chat':
        answer = f'ID чата: {call.message.chat.id}'
    elif call.data == 'navigation_user':
        answer = f'ID пользователя: {call.message.from_user.id}'
    elif call.data.startswith('audience'):
        answer = f'Инфа по аудитории {room[int(call.data.split("-")[1])]}'
        mrkp = get_keyboard_nav(int(call.data.split('-')[1]))
    elif call.data.startswith('page_aud'):
        answer = f'Список аудиторий'
        mrkp = get_keyboard_all_audience(int(call.data.split('-')[1]))
        is_edit = True
    elif call.data == 'all_audience':
        answer = f'Список всех локаций'
        mrkp = get_keyboard_all_audience(0)
    elif call.data == 'main':
        answer = """
        Добро пожаловать в бот Института №8 Московского авиационного института

        Приветствую тебя! Я - ваш гид по IT-этажу Института №8. Давай я покажу тебе, что у нас есть.

        """
        mrkp = get_keyboard_main()
    elif call.data == 'contact':
        answer = f'Здесь будут контакты'
        mrkp = get_keyboard_contact()

    if is_edit:
        await call.message.edit_text(answer, reply_markup=mrkp)
    else:
        await call.message.answer(answer, reply_markup=mrkp)
    await call.answer()
