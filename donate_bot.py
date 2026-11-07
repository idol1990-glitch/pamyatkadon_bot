import os
import asyncio
from telegram import Bot
from telegram.constants import ParseMode

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

MESSAGE = """Братья и сестры! Правблог существует благодаря вашим пожертвованиям. Если наши интервью, лекции и посты вам близки — поддержите проект любой суммой.

СБП: +7 911 219 5481 (ТБанк), Марина Николаевна Д.
ВК Donut: https://vk.com/donut/pravblog_ru
Из-за рубежа: https://boosty.to/pravblog_ru/donate"""

async def publish():
    bot = Bot(TOKEN)
    await bot.send_photo(
        chat_id=CHAT_ID,
        photo=open("donate.jpg", "rb"),
        caption=MESSAGE,
        parse_mode=ParseMode.HTML
    )

if __name__ == "__main__":
    asyncio.run(publish())
