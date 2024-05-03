''' Файл'''
from aiogram.fsm.state import State, StatesGroup


class Anketa(StatesGroup):
    ''' Класс нужен для хранения информации из анкеты'''
    name = State()
    sge = State()
    gender = State()
