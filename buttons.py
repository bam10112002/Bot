from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Идентификатор Чата', callback_data='navigation_chat')
    keyboard_builder.button(text='Идентификатор Пользователя', callback_data='navigation_user')

    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()
