from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from load import dp



@dp.message_handler(CommandHelp())
async def helper(message: types.Message):
      text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/joke - Получить рандомную цитату с Баша",
            "/jokebest - Получить рандомную цитату с Баша из категории рулчшее",
            "/jokeeyop [страница] [колличестве цитат] - Получить цитату с определнной станицы в выбраном колличестве(не более 5)",
            "/video [ссылка на видео] - это команда для скачивания видео",
            "/audio [ссылка на видео] - это команда для скачивания аудио")
      await message.answer("\n".join(text))