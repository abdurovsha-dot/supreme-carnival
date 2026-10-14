import asyncio
import os
from telethon import TelegramClient
from telethon.sessions import StringSession

# Xavfsiz o'qish va tekshirish
raw_api_id = os.environ.get('API_ID', '').strip()
API_HASH = os.environ.get('API_HASH', '').strip()
SESSION_STRING = os.environ.get('SESSION_STRING', '').strip()

print(f"DEBUG - API_ID uzunligi: {len(raw_api_id)}")
print(f"DEBUG - API_HASH mavjudmi: {bool(API_HASH)}")
print(f"DEBUG - SESSION_STRING mavjudmi: {bool(SESSION_STRING)}")

try:
    API_ID = int(raw_api_id) if raw_api_id else 0
except ValueError:
    API_ID = 0

# Guruhlar ID'si (ikkita guruh kiritildi)
CHAT_IDS = [
    -1002171469031,
    -1001662858153,
]

MESSAGE_TEXT = (
    "#muhim\n\n"
    "❗️ <i>\"<b>Mahalla yettiligi</b>\" xodimlari \"<b>Raqamli mahalla xodim</b>\" mobil ilovasi orqali davomatdan o'tishni unutmang.</i>\n\n"
    "📱 <a href=\"https://t.me/c/3271562585/1290\">Mahalla yettiligi uchun mobil ilova</a>\n\n"
    "⭐️ Raqamli \"MAHALLA\" platformasi bo'yicha barcha yangiliklardan xabardor bo'lish uchun kanalga obuna keling!"
)

IMAGE_PATH = 'image.jpg'

async def main():
    if API_ID == 0 or not API_HASH or not SESSION_STRING:
        print("XATOLIK: API_ID, API_HASH yoki SESSION_STRING topilmadi yoki bo'sh!")
        return

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
