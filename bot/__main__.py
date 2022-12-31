from aiogram import executor  
from utils import setComand
import messages
from load import dp


async def on_start(dispatcher):
    await setComand.setCommands(dispatcher)

if __name__ == '__main__':
   executor.start_polling(dp, on_startup=on_start)