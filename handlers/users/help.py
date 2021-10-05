from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp, bot


@dp.message_handler(commands = ["commands"])
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/about - Yordam",
            "/commands - Buyruqlar to'plami")
    chat_id = message.from_user.id
    await bot.send_chat_action(chat_id=chat_id, action='typing')
    await message.answer("\n".join(text))
