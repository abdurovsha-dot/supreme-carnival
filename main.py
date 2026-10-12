import asyncio
from telethon import TelegramClient

# Telegram API ma'lumotlari (my.telegram.org saytidan olinadi)
API_ID = 33493524  # O'zingizning API_ID raqamingizni yozing
API_HASH = 'sizning_api_hash_ingiz'
SESSION_NAME = 'my_session'

# Guruhlar ID'si (yoki username'lari)
CHAT_IDS = [
    -1003719999075,  # 1-guruh
    # Boshqa guruhlar...
]

MESSAGE_TEXT = (
    "#muhim\n\n"
    "❗️ <i>\"<b>Mahalla yettiligi</b>\" xodimlari \"<b>Raqamli mahalla xodim</b>\" mobil ilovasi orqali davomatdan o'tishni unutmang.</i>\n\n"
    "📱 <a href=\"https://t.me/c/3271562585/1290\">Mahalla yettiligi uchun mobil ilova</a>\n\n"
    "⭐️ Raqamli \"MAHALLA\" platformasi bo'yicha barcha yangiliklardan xabardor bo'lish uchun kanalga obuna bo'ling!"
)

IMAGE_PATH = 'image.jpg' # GitHub'ga yuklagan rasm nomi

async def main():
    async with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
        for chat_id in CHAT_IDS:
            try:
                await client.send_file(
                    chat_id,
                    IMAGE_PATH,
                    caption=MESSAGE_TEXT,
                    parse_mode='html'
                )
                print(f"Xabar yuborildi: {chat_id}")
                await asyncio.sleep(2) # Guruhlar orasida 2 soniya pauza
            except Exception as e:
                print(f"Xatolik {chat_id}: {e}")

if __name__ == '__main__':
    asyncWorker = main()
    asyncio.run(asyncWorker)
