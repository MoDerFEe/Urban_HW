from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State
import asyncio

api = '7659378126:AAFWQP38bbhJiVpRvOFhstqHflPrrYm4SWM'
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(lambda message: 'calories' in message.text)
async def set_age(message: Message, state: FSMContext):
    await state.set_state(UserState.age)
    await message.answer('Введите свой возраст:')


@dp.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    age = message.text
    await state.update_data(age=int(age))
    await state.set_state(UserState.growth)
    await message.answer('Введите свой рост (в см):')


@dp.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    growth = message.text
    await state.update_data(growth=int(growth))
    await state.set_state(UserState.weight)
    await message.answer('Введите свой вес (в кг):')


@dp.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    weight = message.text
    await state.update_data(weight=int(weight))

    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']

    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f'Ваша норма калорий: {calories}')

    await state.clear()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
