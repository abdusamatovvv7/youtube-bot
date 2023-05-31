import logging

from aiogram import Bot, Dispatcher, executor, types
from test import video_yukla
API_TOKEN = ''

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Bu bot orqali siz: You tube REELS videolar skachat qilishingiz mumkin!!!")

@dp.message_handler()
async def echo(message: types.Message):
    mes_text = message.textk
    video_link = video_yukla(mes_text)
    await message.answer("Video yuklanmoqda♻️")
    await message.answer_video(video_link,caption="Murojat uchun: @instagram_saverr_robot")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)