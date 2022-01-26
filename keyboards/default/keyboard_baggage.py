from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_1 = KeyboardButton('Да, нужен')
button_2 = KeyboardButton('Нет, не нужен')

menu_baggage = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2,
)

menu_baggage.add(button_1, button_2)