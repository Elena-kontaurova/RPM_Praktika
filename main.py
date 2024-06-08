''' Файл для запуска бота - анкеты'''
import asyncio

from aiogram import Bot, Dispatcher
from handlers import include_routers
from tok import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    ''' Метод запускает процесс опроса, входящих обновлений для бота. 
Основаная точка входа и запуска бота. '''
    include_routers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
