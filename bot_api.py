import aiogram as ai
from request import suma_ks, suma_for, suma_dor
from aiogram.types import  KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery


access = '6645959837:AAHQHTobLoEQ7Pdz5Tg6sUYEFzy1sCPO4GQ'
bot = ai.Bot(access)
dp = ai.Dispatcher(bot)
suma_ks = '{:,}'.format(round(suma_ks, 2)).replace(",", " ")
suma_for = '{:,}'.format(round(suma_for, 2)).replace(",", " ")
suma_dor = '{:,}'.format(round(suma_dor, 2)).replace(",", " ")


@dp.message_handler (commands = 'start')
async def start(message: Message):
    await message.answer(f'Общая сумма КС-2: {suma_ks} руб.\nСумма КС-2 до выверки: {suma_for}руб.\nНа доработке: {suma_dor}руб.')

if __name__ == '__main__':
    ai.executor.start_polling(dp, skip_updates=True)