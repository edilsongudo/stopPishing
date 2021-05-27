from selenium import webdriver
from time import sleep
from random import randint, choice
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
import os
import json
import datetime
import requests
from time import sleep
from bs4 import BeautifulSoup as bs4
# from telethon.sync import TelegramClient, events

while True:
    try:
        print('Launching Browser')
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', 'pt')
        profile.set_preference('general.useragent.override',
                               'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0')
        navegador = webdriver.Firefox(
            executable_path=r'/Program Files/Instagram2/geckodriver.exe', firefox_profile=profile)
        break
    except Exception as e:
        print(e)
        continue

navegador.get(
    'https://vejaaagoraaa2-online.preview-domain.com/cadastrar2/?entrar')
print('...')
