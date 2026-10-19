import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

options = Options()
# Yangi headless rejimi va barqarorlik parametrlari
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# Bot sifatida bloklanmasligi uchun haqiqiy User-Agent
options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)

# Brauzer barcha og'ir resurslarni kutmasdan darhol boshqaruvni qaytaradi
options.page_load_strategy = 'none'

driver = webdriver.Chrome(options=options)
driver.set_page_load_timeout(30)

try:
    target_url = (
        "https://mahalla.ijro.uz/attendance/list?"
        "region_id=00s0eed0000region000011&"
        "district_id=00s0eed0000region000091&"
        "page=1&offset=0&limit=20&statuses=5&reason_category=2&positions=1"
    )
    
    print("Saytga ulanish boshlandi...")
    try:
        driver.get(target_url)
    except TimeoutException:
        print("Sahifa to'liq yuklanmadi, ammo mavjud qismi chizilishini kutamiz...")

    # Frontend skriptlari va jadval ma'lumotlari yuklanishi uchun kutish
    time.sleep(15)

    # Skrinshot olish
    screenshot_path = "attendance.png"
    driver.save_screenshot(screenshot_path)
    print("Skrinshot saqlandi.")

# Telegram orqali shaxsiy profildan yuborish
    from telethon.sync import TelegramClient
    from telethon.sessions import StringSession

    api_id = int(os.environ.get("TG_API_ID"))
    api_hash = os.environ.get("TG_API_HASH")
    session_str = os.environ.get("TG_SESSION")
    CHAT_ID = -1003271562585

    print("Shaxsiy profildan Telegramga ulanish...")
    with TelegramClient(StringSession(session_str), api_id, api_hash) as client:
        client.send_file(
            CHAT_ID,
            screenshot_path,
            caption="📊 O'rta Chirchiq tumani: Sababsiz ishga kelmagan Mahalla raislari ro'yxati"
        )
        print("Rasm shaxsiy profilingiz nomidan muvaffaqiyatli yuborildi!")
        # Javobni konsolga chiqarish
        print("Telegram javobi:", res.status_code, res.text)
        
        # AGAR XATOLIK BO'LSA, GITHUB ACTIONS'NI TO'XTATIB KO'RSATISH UCHUN:
        res.raise_for_status()

finally:
    driver.quit()
