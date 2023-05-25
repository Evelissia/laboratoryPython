from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

from credentials import check_credentials
from grades import get_grades

bot = Bot(token=os.getenv('TOKEN'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

async def on_startup(_):
    print('Бот вышел в онлайн')

@dp.message_handler(commands=['start'])
async def start(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['/start', '/help']
    keyboard.add(*buttons)
    
    await message.answer('Добро пожаловать! Введите учетные данные вашего ребенка. Сначала введите имя пользователя', reply_markup=keyboard)
    await state.set_state('username')

# ввод имени
@dp.message_handler(state='username') 
async def process_username(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
        
    await message.answer('Теперь введите фамилию:')
    await state.set_state('lastname')

# ввод пароля     
@dp.message_handler(state='lastname')
async def process_password(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['lastname'] = message.text

        # Проверка учетных данных
        response = check_credentials(f"{data['username']} {data['lastname']}")
        await message.answer(response)

        if response == 'Учетные данные верны.':
            grades_info = get_grades(f"{data['username']} {data['lastname']}")
            await message.answer(grades_info)

    await state.finish()
    
       
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['/start', '/help']
    keyboard.add(*buttons)
    
    commands = [
        '/start - Начать диалог',
        '/help - Вывести список команд'
    ]
    await message.answer('\n'.join(commands), reply_markup=keyboard)


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)