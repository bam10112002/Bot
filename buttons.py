from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Идентификатор Чата', callback_data='navigation_chat')
    keyboard_builder.button(text='Идентификатор Пользователя', callback_data='navigation_user')

    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()


def get_keyboard_nav(index=0):
    room = ['IT-1', 'IT-2', 'IT-3', 'IT-4', 'IT-5', 'IT-6', 'IT-7', 'IT-8', 'IT-9', 'IT-10', 'IT-11', 'IT-12', 'IT-13',
            'IT-14', 'IT-15', 'IT-16', 'IT-17', 'IT-18']
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text=room[index - 1], callback_data=f'audience-{(index + 17) % 18}')
    keyboard_builder.button(text=room[(index + 1) % 18], callback_data=f'audience-{(index + 1) % 18}')
    keyboard_builder.adjust(2)
    keyboard_builder.button(text='Главное меню', callback_data=f'main')
    keyboard_builder.button(text='Список всех аудиторий', callback_data=f'all_audience')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()


def get_keyboard_all_audience(index=0):
    room = ['IT-1', 'IT-2', 'IT-3', 'IT-4', 'IT-5', 'IT-6', 'IT-7', 'IT-8', 'IT-9', 'IT-10', 'IT-11', 'IT-12', 'IT-13',
            'IT-14', 'IT-15', 'IT-16', 'IT-17', 'IT-18']
    keyboard_builder = InlineKeyboardBuilder()
    for i in range(3):
        keyboard_builder.button(text=room[index], callback_data=f'audience-{index}')
        index += 1
    keyboard_builder.adjust(3)
    for i in range(3):
        keyboard_builder.button(text=room[index], callback_data=f'audience-{index}')
        index += 1
    keyboard_builder.adjust(3)

    keyboard_builder.button(text='Главное меню', callback_data=f'main')
    keyboard_builder.button(text='Назад', callback_data=f'page_aud-{(index + 6) % 18}')
    keyboard_builder.button(text='Дальше', callback_data=f'page_aud-{(index) % 18}')
    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()


def get_keyboard_main():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Экскурсия по аудиториям', callback_data=f'all_audience')
    keyboard_builder.button(text='Контакты', callback_data=f'contact')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()


def get_keyboard_contact():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Главное меню', callback_data=f'main')
    keyboard_builder.button(text='Экскурсия по аудиториям', callback_data=f'all_audience')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()
