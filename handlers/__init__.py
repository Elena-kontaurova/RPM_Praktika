''' Пакет с обработчиками событий'''
from aiogram import Dispatcher

from handlers import anketa, start

def include_routers(dp: Dispatcher):
    ''' Функция подключает роутеры'''
    dp.include_router(
        start.router,
        anketa.router
    )
