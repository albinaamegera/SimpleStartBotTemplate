from aiogram import Bot, Dispatcher
from config import get_config

async def main():
    bot = Bot(token=get_config().bot.token)
    dp = Dispatcher()

    await dp.start_polling(bot)