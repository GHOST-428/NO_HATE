from colorama import Fore, Back, Style
import requests
import random
import string
import json
import os

cyan = Style.BRIGHT + Fore.CYAN
purple = Style.DIM + Fore.MAGENTA

user_agent = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

def search_phone(phone: str):
    url = f"https://htmlweb.ru/geo/api.php?json&telcod={phone}"
    response = requests.get(url, headers={'User-Agent': user_agent})
    
    try:
        if response.status_code == 200:
            data = json.loads(response.text)
        
            print(Fore.YELLOW + "\nPhone Info📞")
            print(f"Страна: {data['country']['fullname']}")
            print(f"Город: {data['region']['name']}")
            print(f"Оператор: {data['0']['oper_brand']}")
        
    except:
        print(f"Страна: Не найдено")
        print(f"Город: Не найдено")
        print(f"Оператор: Не найдено")
    print("")
        
def search_ip(ip: str):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url, headers={'User-Agent': user_agent})
    data = response.json()
    
    try:
        print(Fore.YELLOW + "\nIP Info🌐")
        print(f"Страна: {data['country']}")
        print(f"Регион: {data['region']}")
        print(f"Город: {data['city']}")
    except:
        print("Страна: Не найдено")
        print("Регион: Не найдено")
        print("Город: Не найдено")
    print("")
    
def main():
    while True:
        Fore.RESET
        print(purple + "╔════════════════════════════════════╗")
        print(purple + "║               ФУНКЦИИ              ║")
        print(purple + "╠════════════════════════════════════╣")
        print(purple + "║         Пробив по номеру: 1        ║")
        print(purple + "║           Пробив по IP: 2          ║")
        print(purple + "║              Выход: 0              ║")
        print(purple + "╚════════════════════════════════════╝")
        
        print()
        select = input("[ENTER THE FUNCTION NUMBER]: ")
        
        if select == "1":
            phone = input(purple + "[ENTER THE PHONE]: ")
            search_phone(phone)
        
        if select == "2":
            ip = input(purple + "[ENTER THE IP]: ")
            search_ip(ip)
        
        if select == "0":
            break

main()
