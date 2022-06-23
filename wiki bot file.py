"""
 This is a echo bot.
 It echoes any incoming text messages.
 """

import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5133143201:AAFgN3g-p3V4_7WmzUE_uSdQMxTb-Wz_etM'
wikipedia.set_lang('uz')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def vikiBot(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
         await message("bu haqida malumot yoq")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
