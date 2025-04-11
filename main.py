import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from client import Client
from messages import Message
from settings import TOKEN
from utils import createDir, removeDir, UtilsSettings
from bots_funcs import eventNewChat, eventStartMessage, eventGetDocument


bot = Bot(token=TOKEN)
client = Client()
dp = Dispatcher()
indexes_utils = UtilsSettings()


@dp.message(Command("newchat"))
async def cmd_newchat(message: types.Message):
    await eventNewChat(client, message)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await eventStartMessage(message)


@dp.message(F.photo)
async def get_photo(message: Message):
    await message.bot.download(file=message.photo[-1].file_id, destination=f'pictures/pic_{indexes_utils.photo_id}.jpg')
    client.messages.append(Message(text=message.caption, image=indexes_utils.photo_id))
    indexes_utils.photo_id += 1


@dp.message(F.document)
async def handle_document(message: Message):
    await eventGetDocument(message, bot, client, indexes_utils)


@dp.message(F.text)
async def catch_messages(message: types.Message):
    client.messages.append(Message(text=message.text))


async def main():
    try:
        await createDir()
        await dp.start_polling(bot)
    finally:
        await removeDir()


if __name__ == '__main__':
        asyncio.run(main())

