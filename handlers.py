from aiogram import types, Router
from aiogram.enums import ParseMode
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

import buttons
from aiogram.types import KeyboardButton

router = Router()

main_kb = [
    [
        KeyboardButton(text='Экскурсия по аудиториям'),
        KeyboardButton(text='Ссылки')
    ]
]
main_keyboard = types.ReplyKeyboardMarkup(keyboard=main_kb, resize_keyboard=True)


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("""
        Добро пожаловать в бот Института №8 Московского авиационного института!

        Приветствую тебя! Я - ваш гид по IT-этажу Института №8. Давай я покажу тебе, что у нас есть.

        """, reply_markup=buttons.get_keyboard_main())

# @router.message(Command("video"))
# async def message_handler(msg: Message):
#     video = FSInputFile(path="video.mp4")
#     await msg.answer_video(video)
#
#
# @router.message(Command("video_note"))
# async def message_handler(msg: Message):
#     video = FSInputFile(path="note.mp4")
#     await msg.answer_video_note(video)
#     await msg.answer("Хуй соси за 300 баллов",  reply_markup=buttons.get_keyboard())
