import asyncio
from aiogram.types import Message
from aiogram import Bot
from PIL import Image


async def eventNewChat(message: Message):
    await message.answer('Чат начат заново. Напишите Ваш запрос!')


async def eventStartMessage(message: Message):
    await message.answer('Привет! Рад, что ты выбрал моего бота! Если хочешь ознакомиться с исходным кодом, '
                         'посмотри мой Git: https://github.com/Pricolistok/AI_Bot\n'
                         'В боте есть единственная команда: /newchat - команда используется начала нового чата!')


async def eventGetDocument(message: Message, bot: Bot, client):
    document = message.document
    file_info = await bot.get_file(document.file_id)
    file_path = file_info.file_path
    destination = f"documents/doc_{document.file_name}"
    await bot.download_file(file_path, destination)
    file = client.files.upload(file=f"documents/doc_{document.file_name}")

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=[message.caption, file]
    )
    await message.answer(response.text)


async def eventGetPhoto(message: Message, client):
    await message.bot.download(file=message.photo[-1].file_id, destination=f'pictures/pic.png')
    image = Image.open("pictures/pic.png")
    await asyncio.sleep(1)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[image, message.caption]
    )
    await message.answer(response.text)


async def eventGetText(message: Message, client):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[message.text]
    )
    await message.answer(response.text)
