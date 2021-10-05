from aiogram import types
import requests
from aiogram.dispatcher import FSMContext
from keyboards.inline.menu import menu
from keyboards.inline.uzb_btn import uzbek_btn
from aiogram.dispatcher.filters import Text
from time import sleep
from loader import dp, bot
from states.user_photo import Photo
from ocr.ocr import ocr_space_url
import json
api_key = '8f21fec35f88957'



@dp.message_handler(Text(equals='Rasmdagi matnni tarjima qilish', ignore_case=True))
async def entering_photo(msg : types.Message):
	chat_id = msg.from_user.id
	await bot.send_chat_action(chat_id=chat_id, action='typing')
	await msg.answer("Matn bo'lgan rasmni yuklang 📝!")
	await Photo.photo_path.set()

@dp.message_handler(content_types=types.ContentType.PHOTO, state=Photo.photo_path)
async def photo_get(msg : types.Message, state : FSMContext):
	file_id = msg.photo[-1].file_id
	print(file_id)
	file_info = await bot.get_file(file_id)
	fi = file_info.file_path
	photo_url = f'https://api.telegram.org/file/bot1910663617:AAGCFhwAGiiRlkkbhgq6d1VgqQq4kvdBgYc/{fi}'
	await state.update_data(
		{
			'photo' : photo_url,
		},
		)
	chat_id = msg.from_user.id
	await bot.send_chat_action(chat_id=chat_id, action='typing')	
	await msg.answer('Matn tilini tanlang!', reply_markup=menu)
	await Photo.next()


@dp.callback_query_handler(state=Photo.lang)
async def process_callback_button1(callback_query: types.CallbackQuery, state : FSMContext):
	lang = callback_query.data
	message_id = callback_query.message.message_id
	chat_id = callback_query.message.chat.id
	await bot.edit_message_text(text='Ozroq kuting matn aniqlanmoqda!', chat_id=chat_id, message_id=message_id)
	
	await state.update_data(
			{
				'lang' : lang,
			},
		)
	# Ma'lumotlarni olish
	data = await state.get_data()
	fi = data.get('photo')
	lang = data.get('lang')
	print(fi)

	# result = requests.get(f"https://api.ocr.space/parse/imageurl?apikey={api_key}&url={fi}&language={lang}&detectOrientation=True&filetype=JPG&OCREngine=1&isTable=True&scale=True")
	result = requests.get("https://api.ocr.space/parse/imageurl?apikey=" + api_key +"&url="+fi + "&language="+ lang +"&detectOrientation=True&filetype=JPG&OCREngine=1&isTable=True&scale=True")
	result = result.json()
	print(result)
	
	try:
		if result['IsErroredOnProcessing']==False:
			result_text = result['ParsedResults'][0]['ParsedText']
			if len(result_text) < 5:
				await bot.send_chat_action(chat_id=chat_id, action='typing')
				await bot.edit_message_text(text="Iltimos, tarkibida kamida 5 tadan ortiq belgi bo'lgan rasm yuklang", chat_id=chat_id, message_id=message_id)
			else :
				await bot.send_chat_action(chat_id=chat_id, action='typing')
				await bot.edit_message_text(text=result_text, chat_id=chat_id, message_id=message_id, reply_markup=uzbek_btn)

	except:			
	
		print(result)
		await bot.edit_message_text(text="⚠️Qandaydir xatolik yuz berdi, iltimos qaytadan urinib ko'ring⚠️", chat_id=chat_id, message_id=message_id)	

		
		

	
	await state.reset_state()

