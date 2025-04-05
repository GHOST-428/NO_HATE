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

def report(phone, ip, site):
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
    if phone:
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

    if ip:
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

    if site:
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
    with open('report.html', 'w', encoding='utf-8') as file:
        file.write(html)

    webbrowser.open('report.html')

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

        if select == "-report":
            phone = input(Style.DIM + Fore.WHITE + "[ENTER THE PHONE?]: ")
            ip = input(Style.DIM + Fore.WHITE + "[ENTER THE IP?]: ")
            domen = input(Style.DIM + Fore.WHITE + "[ENTER THE DOMEN?]: ")

            report(bool(phone), bool(ip), bool(domen))


os.system("clear")
main()
