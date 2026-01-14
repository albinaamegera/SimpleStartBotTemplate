from aiogram import Bot, Dispatcher
from config import get_config
from aiogram.types import Message
from aiogram.filters import Command

async def main():
    bot = Bot(token=get_config().bot.token)
    dp = Dispatcher()

    @dp.message(Command('start'))
    async def process_start_command(message: Message):
        await message.answer(
            text="Привет! Это команда /start!"
        )

    @dp.message()
    async def process_echo(message: Message):
        await message.answer(
            text=message.text,
        )

    await dp.start_polling(bot)