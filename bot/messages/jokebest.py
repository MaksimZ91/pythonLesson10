from load import dp
from aiogram import types
from controllers import jokeController

@dp.message_handler(commands=['jokebest'])      
async def getBJoke(message: types.Message):    
      await message.answer(text=jokeController.BestRandomJoke())