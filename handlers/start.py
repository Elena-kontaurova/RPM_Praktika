''' Модуль обработки команд старт '''
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import BotCommand, Message, CallbackQuery
from keyboards.start import *

router = Router()


@router.message(Command('start'))
async def start_handler(msg: Message):
    ''' Метод используется для обработки команды start. '''
    await msg.bot.set_my_commands([
        BotCommand(command='start', description='Запуск бота'),
        BotCommand(command='anketa', description='Справка'),
        BotCommand(command='delete', description='Отчислиться'),
    ])
    msg.pho

    await msg.answer(text='Страница 1', reply_markup=kb_start_next)


@router.callback_query(F.data == 'next')
async def next_handler(callback_query: CallbackQuery):
    ''' Метод - обрабатыевает next. '''
    await callback_query.message.edit_text(
        'Страница 2', reply_markup= kb_start_back)


@router.callback_query(F.data == 'back')
async def back_handler(callback_query: CallbackQuery):
    ''' Метод обработки back '''
    await callback_query.message.delete()
    await callback_query.message.answer(
        text = "Страница 1",
        reply_markup= kb_start.kb_next)
