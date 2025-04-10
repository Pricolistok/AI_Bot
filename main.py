import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from client import Client
from messages import Message
from settings import TOKEN


bot = Bot(token=TOKEN)
client = Client()
dp = Dispatcher()
photo_id = 0


@dp.message(Command("newchat"))
async def cmd_newchat(message: types.Message):
    await message.answer('Напишите Ваш запрос')


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer('Привет')


@dp.message(F.photo)
async def get_photo(message: Message):
    global photo_id
    await message.bot.download(file=message.photo[-1].file_id, destination=f'pictures/pic_{photo_id}.jpg')
    print(message.caption)
    photo_id += 1


@dp.message()
async def catch_messages(message: types.Message):
    print("OK")
    print(message.text)



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
