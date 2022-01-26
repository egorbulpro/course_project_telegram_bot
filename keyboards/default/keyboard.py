from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_1 = KeyboardButton('До 8-ми человек')
button_2 = KeyboardButton('От 9-ти до 15-ти человек')
button_3 = KeyboardButton('От 16-ти до 20-ти человек')
button_4 = KeyboardButton('От 20-ти до 50-ти человек')


menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2,
)
menu.add(button_1,button_2,button_3,button_4)
