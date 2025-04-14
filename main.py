import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from settings import TOKEN, API_KEY, MODEL
from utils import createDir, removeDir, UtilsSettings
from bots_funcs import eventNewChat, eventStartMessage, eventGetDocument, eventGetText, eventGetPhoto
from google import genai


bot = Bot(token=TOKEN)
dp = Dispatcher()
indexes_utils = UtilsSettings()
AI = genai.Client(api_key=API_KEY)
chat = AI.chats.create(model=MODEL)


@dp.message(Command("newchat"))
async def cmd_newchat(message: types.Message):
    chat = AI.chats.create(model=MODEL)
    await eventNewChat(message)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await eventStartMessage(message)


@dp.message(F.photo)
async def get_photo(message: types.Message):
    await eventGetPhoto(message, AI)

@dp.message(F.document)
async def handle_document(message: types.Message):
    await eventGetDocument(message, bot, AI)


@dp.message(F.text)
async def catch_messages(message: types.Message):
    await eventGetText(message, AI)


async def main():
    try:
        await createDir()
        await dp.start_polling(bot)
    finally:
        await removeDir()


if __name__ == '__main__':
        asyncio.run(main())
