from aiogram.dispatcher.filters.state import StatesGroup, State

class Photo(StatesGroup):
	photo_path = State()
	lang = State()