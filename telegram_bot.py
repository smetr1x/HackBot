from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '6452903465:AAGdst40w-MLmyEk4X8pr1scMujl4k7I9z0'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# настройка получения сообщений
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5602787567:AAGYv7NrSjwyW7qPs_yvu70C060zrcfZDbQ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("Здарова, бандиты")

@dp.message_handler()
async def echo(message: types.Message):
   await message.answer(message.text)

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)


from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
@dp.message_handler(commands=['start'])

async def send_welcome(message: types.Message):
   kb = [
       [
           types.KeyboardButton(text="Ты че мразь"),
           types.KeyboardButton(text="Но кто он?")
       ],
   ]
   keyboard = types.ReplyKeyboardMarkup(keyboard=kb)

   await message.reply("Добрый день. Готов отвечать на ваши вопросы", reply_markup=keyboard)