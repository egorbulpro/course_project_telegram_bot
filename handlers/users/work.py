from aiogram import types
from loader import dp
from keyboards.default import menu
from keyboards.default.keyboard_country import menu_country
from keyboards.default.keyboard_baggage import menu_baggage


@dp.message_handler(text='Привет')
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!Я - Бот. Наша компания осуществляет международную перевозку пассажиров современными автобусами вместительностью от 8 до 50 человек. Выберите, пожалуйста, количество пассажиров!', reply_markup=menu, parse_mode='Markdown')

@dp.message_handler(text='До 8-ми человек')
async def start_2(message: types.Message):
    await message.answer(f'Отлично, {message.from_user.full_name}! Так как мы занимаемся именно международными перевозками, Вам необходимо выбрать направление!',reply_markup=menu_country, parse_mode='Markdown')

@dp.message_handler(text='От 9-ти до 15-ти человек')
async def start_3(message: types.Message):
    await message.answer(f'Отлично, {message.from_user.full_name}! Так как мы занимаемся именно международными перевозками, Вам необходимо выбрать направление!',reply_markup=menu_country, parse_mode='Markdown')

@dp.message_handler(text='От 16-ти до 20-ти человек')
async def start_4(message: types.Message):
    await message.answer(f'Отлично, {message.from_user.full_name}! Так как мы занимаемся именно международными перевозками, Вам необходимо выбрать направление!',reply_markup=menu_country, parse_mode='Markdown')

@dp.message_handler(text='От 20-ти до 50-ти человек')
async def start_5(message: types.Message):
    await message.answer(f'Отлично, {message.from_user.full_name}! Так как мы занимаемся именно международными перевозками, Вам необходимо выбрать направление!',reply_markup=menu_country, parse_mode='Markdown')

@dp.message_handler(text='СНГ')
async def start_6(message: types.Message):
    await message.answer(f'Хорошо, {message.from_user.full_name}! Подскажите, нужен ли Вам дополнительный багажник?', reply_markup=menu_baggage, parse_mode='Markdown')

@dp.message_handler(text='Европа')
async def start_6(message: types.Message):
    await message.answer(f'Хорошо, {message.from_user.full_name}! Подскажите, нужен ли Вам дополнительный багажник?', reply_markup=menu_baggage, parse_mode='Markdown')

@dp.message_handler(text='Да, нужен')
async def start_6(message: types.Message):
    await message.answer(f'Благодарим Вас, {message.from_user.full_name} за предоставленную информацию. В ближайшее время Вам напишет менеджер и для согласования даты и стоимости поездки. Спасибо что выбрали нашу компанию!')

@dp.message_handler(text='Нет, не нужен')
async def start_6(message: types.Message):
    await message.answer(f'Благодарим Вас, {message.from_user.full_name} за предоставленную информацию. В ближайшее время Вам напишет менеджер и для согласования даты и стоимости поездки. Спасибо что выбрали нашу компанию!')
