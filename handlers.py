from aiogram import types, Router
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
    await msg.answer("Привет! Я твой помощник по it-центру", reply_markup=buttons.get_keyboard_main())


@router.message(Command("video"))
async def message_handler(msg: Message):
    video = FSInputFile(path="video.mp4")
    await msg.answer_video(video)


@router.message(Command("video_note"))
async def message_handler(msg: Message):
    video = FSInputFile(path="note.mp4")
    await msg.answer_video_note(video)
    await msg.answer("Хуй соси за 300 баллов",  reply_markup=buttons.get_keyboard())


# @router.message()
# async def message_handler(msg: Message):
#     await msg.answer(f"Твой ID: {msg.from_user.id}", reply_markup=buttons.get_keyboard())


# @router.message()
# async def echo_handler(message: types.Message) -> None:
#     room = ['IT-1', 'IT-2', 'IT-3', 'IT-4', 'IT-5', 'IT-6', 'IT-7', 'IT-8', 'IT-9', 'IT-10', 'IT-11', 'IT-12', 'IT-13',
#             'IT-14', 'IT-15', 'IT-16', 'IT-17', 'IT-18']
#     index = 0
#     if message.text.upper() in room:
#         index = room.index(message.text.upper())
#
#     await message.answer(f"Инфа по аудитории", reply_markup=buttons.get_keyboard_nav(index))
