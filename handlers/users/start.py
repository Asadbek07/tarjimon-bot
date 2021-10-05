from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main_menu import choose_oper
from loader import dp, bot
# from user_infos.chat_ids import write_to_file, read_from_file
import sqlite3
 


@dp.message_handler(CommandStart(deep_link='kunuz'))
async def bot_start(message: types.Message):
    args = message.get_args()
    text = f'Salom, {message.from_user.full_name}!\n'
    text += f'Sizni {args} tavsiya qildi'
    await message.answer(text)


@dp.message_handler(commands=['start'])
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    chat_id = message.from_user.id        
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    # c.execute("""CREATE TABLE user_infos (
    #     username text,
    #     chat_id integer
    # )""")
    c.execute("""SELECT * FROM user_infos """)
    users = c.fetchall()
    chat_ids = []
    for user in users:
        chat_ids.append(user[1])
    if  chat_id not in chat_ids:
        c.execute("INSERT INTO user_infos VALUES (?, ?) ", (str(message.from_user.username), str(chat_id)))   
    conn.commit()
    c.execute("""SELECT * FROM user_infos """)
    users = c.fetchall()
    print(users)

    conn.close()
    await bot.send_chat_action(chat_id=chat_id, action='typing')
    await message.answer(f"Salom, {message.from_user.full_name}.Tarjimon botga xush kelibsiz!", reply_markup=choose_oper)

