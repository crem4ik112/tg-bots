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
    waiting_number1 = State()
    waiting_number2 = State()

@dp.message(F.text=='/start')
async def start_command(message: Message, state: FSMContext):
    await message.answer("Введите имя")
    # Устанавливаем состояние на ожидание имени
    await state.set_state(States.waiting_name)


@dp.message(States.waiting_name)
async def process_name(message: Message, state: FSMContext):
    await message.answer(f"Приятно познакомиться, {message.text}!")
    await message.answer(f"Сколько тебе лет?")
    await state.set_state(States.waiting_age)

@dp.message(States.waiting_age)
async def process_age(message: Message, state: FSMContext):
    await message.answer(f"Регистрация в боте завершена!")
    await state.clear()  

@dp.message(F.text== "/sum")
async def sum_command(message: Message, state: FSMContext):
    await message.answer("Введите первое число")
    await state.set_state(States.waiting_number1)

@dp.message(States.waiting_number1)
async def process_number1(message: Message, state: FSMContext):
    await message.answer("Введите второе число")
    await state.set_state(States.waiting_number2)

@dp.message(States.waiting_number2)
async def process_number2(message: Message, state: FSMContext):
    await message.answer("СУММА")
    await state.clear() 


    
async def main():
    bot = Bot(token=tg_bot_token)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())