# Project #2 send a automatic birthday message on Whatsapp using Selenium

import csv
import time
from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


BIRTHDAYS_CSV = "birthdays.csv"
MESSAGE_TEMPLATE = "Happy birthday, {name}!"



def load_today_birthdays(csv_path: str):
    today = datetime.now()
    m, d = today.month, today.day
    results = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if int(row["month"]) == m and int(row["day"]) == d:
                results.append(row)
    return results


def make_driver():
    # Use a persistent Chrome profile so you don't need to scan QR every time
    profile_dir = str(Path.cwd() / "chrome_profile")

    options = Options()
    options.add_argument(f"--user-data-dir={profile_dir}")
    options.add_argument("--profile-directory=Default")
    # options.add_argument("--headless=new")  # WhatsApp Web often breaks headless; start non-headless first.

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def send_whatsapp_message(driver, chat_name: str, message: str):
    wait = WebDriverWait(driver, 30)

    driver.get("https://web.whatsapp.com/")

    # Wait until WhatsApp Web loads (search box appears)
    search_box = wait.until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
    )

    # Search for the chat
    search_box.click()
    search_box.send_keys(chat_name)
    time.sleep(1)

    # Click the chat result
    chat = wait.until(
        EC.element_to_be_clickable((By.XPATH, f'//span[@title="{chat_name}"]'))
    )
    chat.click()

    # Find message box and send
    msg_box = wait.until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
    )
    msg_box.click()
    msg_box.send_keys(message)
    msg_box.send_keys(Keys.ENTER)


def main():
    if not Path(BIRTHDAYS_CSV).exists():
        print(f"Missing {BIRTHDAYS_CSV}. Create it first.")
        return

    today_people = load_today_birthdays(BIRTHDAYS_CSV)
    if not today_people:
        print("No birthdays today.")
        return

    driver = make_driver()
    try:
        for person in today_people:
            name = person["name"]
            chat = person["chat"]
            msg = MESSAGE_TEMPLATE.format(name=name)
            print(f"Sending to {chat}: {msg}")
            send_whatsapp_message(driver, chat, msg)
            time.sleep(2)  # small delay between sends
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
