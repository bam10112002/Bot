from aiogram import types, F, Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

import buttons

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")


@router.message(Command("video"))
async def message_handler(msg: Message):
    video = FSInputFile(path="video.mp4")
    await msg.answer_video(video)


@router.message(Command("video_note"))
async def message_handler(msg: Message):
    video = FSInputFile(path="note.mp4")
    await msg.answer_video_note(video)
    await msg.answer("Хуй соси за 300 баллов",  reply_markup=buttons.get_keyboard())



@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}", reply_markup=buttons.get_keyboard())


