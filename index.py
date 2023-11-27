from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

Private = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="My Name"),
            KeyboardButton(text="Username")
        ],
        [
            KeyboardButton(text='My id'),
            KeyboardButton(text='saved message')
        ]
    ],
    resize_keyboard=True
)

token="6879323148:AAHi7RglFgJja_LjaGjIpvIjMbAvYEjl8Kc"

token=token
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(f"Hello {message.from_user.full_name}", reply_markup=Private)

@dp.message_handler(text='My Name')
async def fullname(message: types.Message):
    await message.reply(f'Name: {message.from_user.full_name}')

@dp.message_handler(text='Username')
async def User_name(message: types.Message):
    await message.reply(f'Username: @{message.from_user.username}')

@dp.message_handler(text='My id')
async def User_ID(message: types.Message):
    await message.reply(f'Your ID: {message.from_user.id}')

@dp.message_handler(text='saved message')
async def Saved_message(message: types.Message):
    # Create an inline keyboard with a button that opens a URL
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Saved Message", url="https://t.me/valchunbot")
    keyboard.add(url_button)

    # Send the message with the inline keyboard
    await message.reply("Saved Message", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp)

