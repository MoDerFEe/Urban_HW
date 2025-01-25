from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
import asyncio

api = '7659378126:AAFWQP38bbhJiVpRvOFhstqHflPrrYm4SWM'
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(Command('start'))
async def start_command_handler(message: Message):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message()
async def start_command_handler(message: Message):
    print('Введите команду /start, чтобы начать общение.')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
