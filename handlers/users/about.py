from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp, bot


@dp.message_handler(commands = ["about"])
async def bot_help(message: types.Message):
    text = ("Botning maqsadi: ",
            "<strong>1)</strong> Foydalanuvchilarga telegramdan chiqmagan holda sifatli tarjimon xizmati bilan ta'minlash,",
            "<strong>2)</strong> Rasmdagi matnni bot orqali olish,",
            "<strong>3)</strong> Rasmdan olingan matnni bot orqali tarjima qilish.")
    chat_id = message.from_user.id
    await bot.send_chat_action(chat_id=chat_id, action='typing')
    await message.answer("\n\n".join(text))
