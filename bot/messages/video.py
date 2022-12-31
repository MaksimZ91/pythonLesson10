from load import dp, bot
import os
from aiogram import types
from controllers import videoAudioCntroller


@dp.message_handler(commands=['video'])
async def getJoke(message: types.Message):
  data = videoAudioCntroller.downoladVideo(message.get_args().split()) 
  if not data: 
    return await message.answer("При загрузке произошла ошибка!")  
  print(data)    
  video = open(f'{data}', 'rb')
  await bot.send_video(message.chat.id, video)
  await bot.send_message(message.chat.id, text='Видео загруженно!') 
  os.remove(f'{data}')
  

    

