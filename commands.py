from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot):
    commands = [
        BotCommand(command="video_note", description="Кружок"),
        BotCommand(command="video", description="Видос")
    ]
    await bot.set_my_commands(commands)
