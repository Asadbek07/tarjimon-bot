from aiogram import types
from aiogram.dispatcher import FSMContext
from states.adminstate import Admin
from aiogram.dispatcher.filters import Text
from loader import dp, bot
from user_infos.chat_ids import read_from_file
import sqlite3

# chat_ids = [853443199, 644230165, 1914622728]


@dp.message_handler(Text(equals='1c5bc700-effa-4eea-803c-5cb437e5567d', ignore_case=True))
async def checking_admin(message : types.Message):
	print(message.from_user.id)
	if message.from_user.id == 644230165:
		await message.answer("Siz adminsiz. Reklama yuborishingiz mumkin.")
		await Admin.reklama.set()
	else :
		await message.answer(message.text)	


@dp.message_handler(content_types=['photo'], state=Admin.reklama)
async def sending_advertisement(message : types.Message, state : FSMContext):
	
	conn = sqlite3.connect("users.db")
	c = conn.cursor()
	c.execute("""SELECT * FROM user_infos """)
	users = c.fetchall()
	chat_ids = []
	for user in users:
	    chat_ids.append(user[1])
	# c.commit()
	c.close()
	for chat_id in chat_ids:
		if message.reply_markup:
			await bot.send_photo(chat_id=int(chat_id), photo=str(message.photo[-1].file_id), caption=message.caption, reply_markup=message.reply_markup)
		else:
			await bot.send_photo(chat_id=int(chat_id),photo=str(message.photo[-1].file_id), caption=message.caption)	
	# print("Rasm jo'natildi")
	await state.update_data(
		{
			"reklama" : "jo'natildi",
		}

	)	
	await state.reset_state()



@dp.message_handler(content_types=['video'], state=Admin.reklama)
async def sending_advertisement(message : types.Message, state : FSMContext):
	
	conn = sqlite3.connect("users.db")
	c = conn.cursor()
	c.execute("""SELECT * FROM user_infos """)
	users = c.fetchall()
	chat_ids = []
	for user in users:
	    chat_ids.append(user[1])
	# c.commit()
	c.close()
	print(message.video.file_id)
	file_id = message.video.file_id
	print(file_id)
	# await bot.send_video(chat_id=chat_ids[0], video=file_id, caption=message.caption)
	for chat_id in chat_ids:
		if message.reply_markup:
			await bot.send_video(chat_id=int(chat_id), video=file_id, caption=message.caption, reply_markup=message.reply_markup)
		else:
			await bot.send_video(chat_id=int(chat_id), video=file_id, caption=message.caption)
	# print("Rasm jo'natildi")
	await state.update_data(
		{
			"reklama" : "jo'natildi",
		}

	)	
	await state.reset_state()

@dp.message_handler(state=Admin.reklama)
async def sending_advertisement_text(message : types.Message, state : FSMContext):
	conn = sqlite3.connect("users.db")
	c = conn.cursor()
	c.execute("""SELECT * FROM user_infos """)
	users = c.fetchall()
	chat_ids = []
	for user in users:
	    chat_ids.append(user[1])
	# c.commit()
	c.close()
	print(message)
	for chat_id in chat_ids:
		await bot.send_message(chat_id=chat_id, text=message.text)

	await state.update_data(
		{
			"reklama" : "jo'natildi",
		}

	)	
	await state.reset_state()
	
	