''' Файл для запуска бота - анкеты'''
import asyncio

from aiogram import Bot, Dispatcher
from handlers import include_routers

bot = Bot(token='7108007861:AAH3T-LI-ruypcxJUHuaSJ9aD5qfI62up2Q')
dp = Dispatcher()

async def main():
    ''' Метод запускает процесс опроса, входящих обновлений для бота. 
Основаная точка входа и запуска бота. '''
    include_routers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
