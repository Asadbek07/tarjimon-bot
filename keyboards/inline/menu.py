from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


menu = InlineKeyboardMarkup(
	inline_keyboard=[
			[
				InlineKeyboardButton('🇬🇧English', callback_data='eng'),
				InlineKeyboardButton(text="🇺🇿O'zbekcha", callback_data='eng'),
			],
			[
				InlineKeyboardButton(text='🇷🇺Pусский', callback_data='rus')
			],


		],
		resize_keyboard=True
	)