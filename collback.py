from aiogram.types import CallbackQuery

from Bot.buttons import get_keyboard_all_audience, get_keyboard_contact, get_keyboard_main, get_keyboard_nav

room = ['IT-1', 'IT-2', 'IT-3', 'IT-4', 'IT-5', 'IT-6', 'IT-7', 'IT-8', 'IT-9', 'IT-10', 'IT-11', 'IT-12', 'IT-13',
        'IT-14', 'IT-15', 'IT-16', 'IT-17', 'IT-18']


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
        answer = f'Список аудиторий'
        mrkp = get_keyboard_all_audience(0)
    elif call.data == 'main':
        answer = f'Главная'
        mrkp = get_keyboard_main()
    elif call.data == 'contact':
        answer = f'Здесь будут контакты'
        mrkp = get_keyboard_contact()

    if is_edit:
        await call.message.edit_text(answer, reply_markup=mrkp)
    else:
        await call.message.answer(answer, reply_markup=mrkp)
    await call.answer()
