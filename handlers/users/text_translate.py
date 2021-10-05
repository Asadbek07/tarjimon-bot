from aiogram import types
from aiogram.dispatcher.filters import Text
from googletrans import Translator
from loader import dp, bot 
from googletrans import Translator

def translate(text):
    translator = Translator()
    lang = translator.detect(text).lang
    dest = 'uz' if not lang == 'uz' else 'en'
    translated_text = translator.translate(text=text, dest=dest).text
    return translated_text

@dp.message_handler(state=None)
async def text_example(msg: types.Message):
	print(msg.text)
	translated_text = translate(msg.text)
	await msg.reply(translated_text)


@dp.callback_query_handler()
async def process_callback_button1(callback_query: types.CallbackQuery):
	if callback_query.data == 'uz':
		text = callback_query.message.text
		translated_text = translate(text)
		message_id = callback_query.message.message_id
		chat_id = callback_query.message.chat.id
		await bot.edit_message_text(text=translated_text, chat_id=chat_id, message_id=message_id)
	
