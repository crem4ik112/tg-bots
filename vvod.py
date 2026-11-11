import asyncio
import random
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

tg_bot_token = "9096492239:AAE7BsEIJs_k21IzY4zHJMiH-2ZiKHFQCK4"
# Небольшое изменение dp
dp = Dispatcher(storage=MemoryStorage())

# Определяем, какие состояния будут у пользователей
class States(StatesGroup):
    waiting_name = State()
    waiting_age = State()


@dp.message(F.text=='/start')
async def start_command(message: Message, state: FSMContext):
    await message.answer("Введите имя")
    # Устанавливаем состояние на ожидание имени
    await state.set_state(States.waiting_name)

# Здесь фильтр будет срабатывать на любое сообщение пользователя,
# если его состояние waiting_name
@dp.message(States.waiting_name)
async def process_name(message: Message, state: FSMContext):
    # В сообщении пользователя содержится его имя. Можно проверить, что он не написал
    # белиберду и сохранить имя, например, в БД
    await message.answer(f"Приятно познакомиться, {message.text}!")
    await message.answer(f"Сколько тебе лет?")
    # Устанавливаем состояние на ожидание возраста
    await state.set_state(States.waiting_age)

# Здесь фильтр будет срабатывать на любое сообщение пользователя,
# если его состояние waiting_age
@dp.message(States.waiting_age)
async def process_age(message: Message, state: FSMContext):
    # В сообщении пользователя содержится его возраст. Можно проверить, что он не написал
    # белиберду и сохранить возраст, например, в БД
    await message.answer(f"Регистрация в боте завершена!")
    # Сбрасываем состояние
    await state.clear()  

async def main():
    bot = Bot(token=tg_bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())