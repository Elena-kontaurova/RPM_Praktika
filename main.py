''' Файл для запуска бота - анкеты'''
import asyncio

from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, BotCommand, \
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

bot = Bot(token='7108007861:AAH3T-LI-ruypcxJUHuaSJ9aD5qfI62up2Q')
dp = Dispatcher()
router = Router()


class Anketa(StatesGroup):
    ''' Класс нужен для хранения информации из анкеты'''
    name = State()
    age = State()
    gender = State()


@router.message(Command("anketa"))
async def anketa_handler(msg: Message, state: FSMContext):
    '''Метод - обработчик команды anketa. Метод отправляет сообщение пользователю 
с запросом ввести свое имя и предоставляет кнопку 'Отмена', для отмены опроса'''
    await state.set_state(Anketa.name)
    markup = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text = 'Отмена', callback_data='cancel_anketa')]])
    await msg.answer('Введите Ваше имя', reply_markup=markup)


@router.callback_query(F.data == 'cancel_anketa')
async def cancel_handler(callback_query: CallbackQuery, state: FSMContext):
    ''' Метод -  обработчик callback-запроса, с данными анкеты. 
Используется для отмены регистрации. Бот уведомляет пользователя 
сообщением 'Регистрация отменена'. '''
    await state.clear()
    await callback_query.message.answer('Регистрация отменена')


@router.message(Anketa.name)
async def set_name_by_anketa_handler(msg: Message, state: FSMContext):
    ''' Метод - обработки сообщения, в котором пользователь должен 
указать своё имя. Предоствляет кнопки 'Назад', и 'Отмена'. 
И после, пользователь долджен ввести свой возраст'''
    await state.update_data(name=msg.text)
    await state.set_state(Anketa.age)
    markup = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text='Назад', callback_data='set_name_anketa'),
        InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa'),]])
    await msg.answer('Введите Ваш возраст', reply_markup=markup)


@router.callback_query(F.data == 'set_name_anketa')
async def set_name_anketa_handler(callback_query: CallbackQuery, state: FSMContext):
    ''' Метод для '''
    await anketa_handler(callback_query.message, state)


@router.message(Anketa.age)
async def set_age_by_anketa_handler(msg: Message, state: FSMContext):
    ''' Метод для ввода'''
    try:
        await state.update_data(age=int(msg.text))
    except ValueError:
        await msg.answer('Вы не верно ввели возраст!')
        markup = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text = 'Назад', callback_data='set_name_anketa'),
            InlineKeyboardButton(text = 'Отмена', callback_data='cancel_anketa'),]])
        await msg.answer('Введите Ваш возраст', reply_markup=markup)
        return


    await state.set_state(Anketa.gender)
    markup = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text='Назад', callback_data='set_age_anketa'),
        InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa'),]])
    await msg.answer('Введите Ваш пол', reply_markup=markup)


@router.callback_query(F.data == 'set_age_anketa')
async def set_age_anketa_handler(callback_query: CallbackQuery, state: FSMContext):
    ''' Метод для '''
    await state.set_state(Anketa.age)
    markup = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text = 'Назад', callback_data='set_name_anketa'),
        InlineKeyboardButton(text = 'Отмена', callback_data='cancel_anketa'),]])
    await callback_query.message.answer('Введите Ваш возраст', reply_markup=markup)


@router.message(Anketa.gender)
async def set_age_by_anketa_two_handler(msg: Message, state: FSMContext):
    ''' Метод для '''
    await state.update_data(gender=msg.text)
    await msg.answer(str(await state.get_data()))
    await state.clear()


@router.message(Command('start'))
async def start_handler(msg: Message):
    ''' Метод для '''
    await bot.set_my_commands([
        BotCommand(command='start', description='Запуск бота'),
        BotCommand(command='anketa', description='Справка'),
        BotCommand(command='delete', description='Отчислиться'),
    ])


    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Вперед', callback_data='next')]
    ])
    await msg.answer(text='Страница 1', reply_markup=inline_markup)


@router.callback_query(F.data == 'next')
async def next_handler(callback_query: CallbackQuery):
    ''' Метод для '''
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ])
    await callback_query.message.edit_text(
        'Страница 2', reply_markup=inline_markup)



@router.callback_query(F.data == 'back')
async def back_handler(callback_query: CallbackQuery):
    ''' Метод для '''
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Вперед', callback_data='next')]
    ])
    await callback_query.message.delete()
    await callback_query.message.answer(
        text = 'Страница 1',
        reply_markup=inline_markup)


async def main():
    ''' Что то'''
    await dp.start_polling(bot)


dp.include_routers(router)

if __name__ == '__main__':
    asyncio.run(main())
