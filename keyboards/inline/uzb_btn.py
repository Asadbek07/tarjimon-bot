from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


uzbek_btn = InlineKeyboardMarkup(
	inline_keyboard=[
			[
			
				InlineKeyboardButton(text="🇺🇿O'zbekcha", callback_data='uz'),
			],
		],
		resize_keyboard=True
	)