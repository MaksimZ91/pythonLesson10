from load import dp
from aiogram import types
from controllers import jokeController

@dp.message_handler(commands=['jokeyop'])      
async def getPageOrYearJoke(message: types.Message):
    for joke in jokeController.PageOrYearJoke(message.get_args().split()):
              await message.answer(text=joke) 