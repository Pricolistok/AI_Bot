from utils import UtilsSettings
from client import Client
from aiogram.types import Message
from aiogram import Bot


async def eventNewChat(client: Client, message: Message):
    client.messages.clear()
    await message.answer('Чат начат заново. Напишите Ваш запрос!')


async def eventStartMessage(message: Message):
    await message.answer('Привет! Рад, что ты выбрал моего бота! Если хочешь ознакомиться с исходным кодом, '
                         'посмотри мой Git: https://github.com/Pricolistok/AI_Bot\n'
                         'В боте есть единственная команда: /newchat - команда используется начала нового чата!')


async def eventGetDocument(message: Message, bot: Bot, client: Client, indexes_utils: UtilsSettings):
    document = message.document
    file_info = await bot.get_file(document.file_id)
    file_path = file_info.file_path
    destination = f"documents/doc_{indexes_utils.document_id}_{document.file_name}"
    await bot.download_file(file_path, destination)
    client.messages.append(Message(text=message.caption, file=indexes_utils.document_id))
    indexes_utils.document_id += 1
    await message.reply(f"Downloaded file to {destination}")