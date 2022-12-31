from aiogram import types


async def setCommands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("video", "Скачать видео из ютуба"),
            types.BotCommand("audio", "Скачать аудио из ютуба"),
            types.BotCommand("joke", "Получить рандомную цитату с Баша"),
            types.BotCommand("jokebest", "Получить рандомную цитату с Баша из категории рулчшее"),
            types.BotCommand("jokeyop", "Получить цитату с определнной станицы в выбраном колличестве(не более 5)")
        ]
    )