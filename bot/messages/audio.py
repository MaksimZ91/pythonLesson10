from load import dp, bot
import os
from aiogram import types
from controllers import videoAudioCntroller


@dp.message_handler(commands=['audio'])
async def getJoke(message: types.Message):
  data = videoAudioCntroller.downoladAudio(message.get_args().split()) 
  if not data: 
    return await message.answer("При загрузке произошла ошибка!")   
  video = open(f'{data}', 'rb')
  await bot.send_audio(message.chat.id, video)
  await bot.send_message(message.chat.id, text="Аудио загруженно!") 
  os.remove(f'{data}')
  