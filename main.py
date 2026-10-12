import asyncio
import os
from telethon import TelegramClient
from telethon.sessions import StringSession


API_ID = int(os.environ.get('API_ID', 0))
API_HASH = os.environ.get('API_HASH', '')
SESSION_STRING = os.environ.get('SESSION_STRING', '')


CHAT_IDS = [
    -1003719999075, 
]

MESSAGE_TEXT = (
    "#muhim\n\n"
    "❗️ <i>\"<b>Mahalla yettiligi</b>\" xodimlari \"<b>Raqamli mahalla xodim</b>\" mobil ilovasi orqali davomatdan o'tishni unutmang.</i>\n\n"
    "📱 <a href=\"https://t.me/c/3271562585/1290\">Mahalla yettiligi uchun mobil ilova</a>\n\n"
    "⭐️ Raqamli \"MAHALLA\" platformasi bo'yicha barcha yangiliklardan xabardor bo'lish uchun kanalga obuna keling!"
)

IMAGE_PATH = 'image.jpg'

async def main():
    async with TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH) as client:
        for chat_id in CHAT_IDS:
            try:
                await client.send_file(
                    chat_id,
                    IMAGE_PATH,
                    caption=MESSAGE_TEXT,
                    parse_mode='html'
                )
                print(f"Xabar yuborildi: {chat_id}")
                await asyncio.sleep(2)
            except Exception as e:
                print(f"Xatolik {chat_id}: {e}")

if __name__ == '__main__':
    asyncio.run(main())
