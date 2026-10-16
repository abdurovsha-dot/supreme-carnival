import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

# Brauzerni fonda ishlashi uchun sozlamalar
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
options.page_load_strategy = 'eager'

driver = webdriver.Chrome(options=options)
driver.set_page_load_timeout(30)

try:
    target_url = "https://mahalla.ijro.uz/attendance/list?region_id=00s0eed0000region000011&district_id=00s0eed0000region000091&page=1&offset=0&limit=20&statuses=5&reason_category=2&positions=1"
    
    print("Saytga ulanish boshlandi...")
    try:
        driver.get(target_url)
    except Exception as e:
        print("Diqqat: Sayt yuklanishida vaqt chegarasi (timeout) oshdi, lekin skrinshot olish davom etadi:", e)
    
    # Sahifadagi ma'lumotlar to'liq chiqishi uchun kutamiz
    time.sleep(12)

    # Skrinshot olib saqlaymiz
    driver.save_screenshot("attendance.png")
    print("Skrinshot muvaffaqiyatli olindi!")

    # Telegram bot orqali yuborish
    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
    CHAT_ID = -1003271562585  # Sizning guruh ID raqamingiz

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
