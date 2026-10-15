import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

# Brauzerni fonda (grafik interfeyssiz) ishlashi uchun sozlash
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

try:
    # Saytdagi filtrlangan tayyor havola
    target_url = "https://mahalla.ijro.uz/attendance/list?region_id=00s0eed0000region000011&district_id=00s0eed0000region000091&page=1&offset=0&limit=20&statuses=5&reason_category=2&positions=1"
    
    driver.get(target_url)
    
    # Angular sahifasi to'liq yuklanib, ma'lumotlarni olib kelishi uchun kutamiz
    time.sleep(8)

    # Skrinshot olib saqlaymiz
    driver.save_screenshot("attendance.png")

    # Telegram bot orqali yuborish
    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
    CHAT_ID = os.environ.get("CHAT_ID")

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
    with open("attendance.png", "rb") as photo:
        files = {"photo": photo}
        data = {
            "chat_id": CHAT_ID,
            "caption": "📊 O'rta Chirchiq tumani: Sababsiz ishga kelmagan Mahalla raislari ro'yxati"
        }
        response = requests.post(url, files=files, data=data)
        print("Telegramga yuborish holati:", response.status_code)

finally:
    driver.quit()
