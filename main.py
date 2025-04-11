import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from client import Client
from messages import Message
from settings import TOKEN
from shutil import rmtree
from os import mkdir


bot = Bot(token=TOKEN)
client = Client()
dp = Dispatcher()
photo_id = 0
document_id = 0


@dp.message(Command("newchat"))
async def cmd_newchat(message: types.Message):
    client.messages.clear()
    await message.answer('Чат начат заново. Напишите Ваш запрос!')


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer('Привет! Рад, что ты выбрал моего бота! Если хочешь ознакомиться с исходным кодом, '
                         'посмотри мой Git: https://github.com/Pricolistok/AI_Bot\n'
                         'В боте есть единственная команда: /newchat - команда используется начала нового чата!')


@dp.message(F.photo)
async def get_photo(message: Message):
    global photo_id
    await message.bot.download(file=message.photo[-1].file_id, destination=f'pictures/pic_{photo_id}.jpg')
    client.messages.append(Message(text=message.caption, image=photo_id))
    photo_id += 1


@dp.message(F.document)
async def handle_document(message: Message):
    global document_id
    document = message.document
    file_info = await bot.get_file(document.file_id)
    file_path = file_info.file_path
    destination = f"documents/doc_{document_id}_{document.file_name}"
    await bot.download_file(file_path, destination)
    client.messages.append(Message(text=message.caption, file=document_id))
    document_id += 1
    await message.reply(f"Downloaded file to {destination}")


@dp.message(F.text)
async def catch_messages(message: types.Message):
    client.messages.append(Message(text=message.text))


async def main():
    try:
        mkdir('documents')
        mkdir('pictures')
        await dp.start_polling(bot)
    finally:
        rmtree('documents/')
        rmtree('pictures/')


if __name__ == '__main__':
        asyncio.run(main())

