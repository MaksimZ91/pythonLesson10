from load import dp
from aiogram import types
from controllers import jokeController

@dp.message_handler(commands=['joke'])
async def getJoke(message: types.Message):    
      await message.answer(text=jokeController.randomJoke())



      
