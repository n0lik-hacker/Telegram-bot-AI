# Подключение библиотек
import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import config

openai.api_key = config.OPENAI_TOKEN
token = config.TOKEN

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])  # Функция, обрабатывающая команду /start
async def welcome(message: types.Message):
    await message.answer(
        "Добро пожаловать!✋🏻\nЯ бот который поможет вам с домашним заданием!\nБлагодаря мне, вы сможете решать различные задачи!")
    await message.answer(
        "Можешь присылать задачу и я ее решу)")


@dp.message_handler()  # Функция - обработчик, возвращает ответ от AI
async def gpt_answer(message: types.Message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message.text},
        ]
    )

    await message.answer(response["choices"][0]["message"]["content"])


if __name__ == "__main__":  # Запускаем бота
    executor.start_polling(dp, skip_updates=True)
