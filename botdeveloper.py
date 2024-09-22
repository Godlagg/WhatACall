from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command
from aiogram import Router
import asyncio

# Создание бота с токеном
bot = Bot(token="7216680715:AAHtmdTaNAwqLDM7EFGX6goZKAO-MNuMB_Y")
dp = Dispatcher()
router = Router()  # Создаем роутер для регистрации хэндлеров

# Обработчик команды /start
@router.message(Command("start"))
async def start(message: types.Message):
    # Создаем инлайн-клавиатуру с кнопкой
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Открыть YouTube', web_app=WebAppInfo(url='https://www.youtube.com'))]
    ])
    
    # Отправляем сообщение с клавиатурой
    await message.answer('Привет! Нажми на кнопку, чтобы открыть YouTube!', reply_markup=markup)

# Добавляем роутер в диспетчер
dp.include_router(router)

# Основная асинхронная функция для запуска бота
async def main():
    await dp.start_polling(bot)  # Запуск long-polling для обработки сообщений

# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())