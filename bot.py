from aiogram import Bot, Dispatcher, executor, types
import re
dataset = {'Какие условия труда?':'С кайфом', 'Какие рабочие часы':'С 9:00 до 18:00, как и у всех рабов'}
API_TOKEN = '6696572953:AAHpYkC4vyhhAOlPcUppafKpkOv-YAzk-3o'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

@dp.message_handler()
async def hr_bot(message: types.Message):
    user_question = message.text
    found_answer = None

    # Поиск ответа в датасете
    for question, answer in dataset.items():
        if re.search(question, user_question, re.IGNORECASE):
            found_answer = answer
            break

    if found_answer:
        await message.answer(found_answer)
    else:
        await message.answer("Извините, я не могу ответить на ваш вопрос.")
        
    
        
   #  await message.reply("Добрый день. Готов отвечать на ваши вопросы", reply_markup=kb)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)