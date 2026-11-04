import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

tg_bot_token = "9096492239:AAE7BsEIJs_k21IzY4zHJMiH-2ZiKHFQCK4"

dp = Dispatcher()


@dp.message(F.text=="/start")
async def command_start(message: Message) -> None:
    await message.answer("Привет! Это первое сообщение бота! Оно высвечивается, когда пользователь вводит команду /start")

@dp.message(F.text == "/donat")
async def donat(m: Message):
    await m.answer("Донат сюда: +79991234567")


@dp.message(F.text.startswith("/better"))
async def command_better(message: Message):
    splited_message_text = message.text.split(" ")
    number1 = int(splited_message_text[1])
    number2 = int(splited_message_text[2])
    
    if number1 > number2:
        await message.answer(str(number1))
    elif number2 > number1:
        await message.answer(str(number2))
    else:
        await message.answer("Числа одинаковые!")


async def main():
    bot = Bot(token=tg_bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

