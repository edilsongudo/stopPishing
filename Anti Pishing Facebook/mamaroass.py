import requests
from requests_html import HTMLSession
from time import sleep
from random import randint
import random
import threading
import browser_cookie3


NUMBER_OF_THREADS = 1


n = 1


def hero():
    global n

    cookiejar = browser_cookie3.chrome(
        domain_name='veeejaaagoraa-org.preview-domain.com')
    listcookies = list(cookiejar)
    for c in listcookies:
        print(c)

    with open('nomes.txt', 'r') as f:
        emails = f.readlines()
        email = emails[random.randint(0, len(emails) - 1)]
        email2 = emails[random.randint(0, len(emails) - 1)]
        email = email.strip() + email2.strip() + '@gmail.com'

    num = str(randint(0, 100))

    with open('7776palavras.txt', 'r') as f:
        palavras = f.readlines()
        palavra = palavras[random.randint(0, len(palavras) - 1)]
        palavra = palavra.strip() + num

    payload = {
        'email': email,
        'senha': palavra
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
    cookies = {'Cookie': 'autorizado=true25b; __cfduid=d2fb496a8b213b33e4720594440b263b51617672297; PHPSESSID=eea4e406d49924b956f548d9dbfe5628; _ga=GA1.2.1655179627.1617672471; _gid=GA1.2.1675302718.1617672471; cf_chl_2=1684b70b6e51f6e; cf_chl_prog=a23; cf_clearance=1833958a6cf12774b3375b628a0be79484392321-1617674303-0-150; _gat_gtag_UA_105583237_1=1'}
    session = HTMLSession()
    # r = session.post('https://veeejaaagoraa-org.preview-domain.com/cadastrar2/login/?get=cookies',
                     # data=payload, cookies=cookies, headers=headers)
    r = session.post('https://veeejaaagoraa-org.preview-domain.com/cadastrar2/login/?get=cookies',
                     data=payload, cookies=cookies, headers=headers)
    n += 1
    print(n, r.status_code, email, palavra)

    while True:
        try:
            print(hero())
        except Exception as e:
            print(e)


threads = []
for i in range(NUMBER_OF_THREADS):
    t = threading.Thread(target=hero)
    t.daemon = True
    threads.append(t)

for i in range(NUMBER_OF_THREADS):
    threads[i].start()

for i in range(NUMBER_OF_THREADS):
    threads[i].join()
