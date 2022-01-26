from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_1 = KeyboardButton('СНГ')
button_2 = KeyboardButton('Европа')

menu_country = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2,
)
menu_country.add(button_1,button_2)