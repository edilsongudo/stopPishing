import requests
from requests_html import HTMLSession
from time import sleep
from random import randint
import random
import threading
import browser_cookie3

from faker import Faker
fake = Faker()

import secrets

secrets.token_hex(nbytes=16)

from random import randint

from fakeCreditNumberGenerator import generate_card


def random_with_N_digits(n):
    range_start = 10**(n - 1)
    range_end = (10**n) - 1
    return randint(range_start, range_end)


n = 1


def hero():
    global n

    cardType = ['mastercard', 'discover',
                'americanexpress', 'visa13', 'visa16']

    payload = {
        "SID": secrets.token_hex(nbytes=16),
        "step": "j2",
        "formdata[tmxid]": "",
        "formdata[firstname]": fake.first_name(),
        "formdata[lastname]": fake.last_name(), "formdata[cc]": str(generate_card(random.choice(cardType))),
        "formdata[exp_m]": str(random.randint(1, 12)),
        "formdata[exp_y]": str(random.randint(21, 30)),
        "formdata[cvv]": str(random.randint(100, 999)),
        "formdata[zip]": str(random.randint(1000, 100000)),
        "xsale_success": "1"
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}

    cookies = {
        'Cookie': 'PHPSESSID=21bfe6fbe190cd2699f7d2649d376f7f; __utma=115632089.1656875090.1622132248.1622132248.1622132248.1; __utmb=115632089.1.10.1622132248; __utmc=115632089; __utmz=115632089.1622132248.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __z_a=3881858030378819689737881'}

    session = HTMLSession()

    r = session.post('https://ndywmr.com/newuser/',
                     data=payload, cookies=cookies, headers=headers)

    if r.status_code == 200:
        n += 1
        print(f'Execution Number: {n} Status Code: {r.status_code}')

    while True:
        try:
            print(hero())
        except Exception as e:
            print(e)


NUMBER_OF_THREADS = 25

threads = []
for i in range(NUMBER_OF_THREADS):
    t = threading.Thread(target=hero)
    t.daemon = True
    threads.append(t)

for i in range(NUMBER_OF_THREADS):
    threads[i].start()

for i in range(NUMBER_OF_THREADS):
    threads[i].join()
