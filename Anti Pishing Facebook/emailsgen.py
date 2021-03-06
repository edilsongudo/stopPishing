# Instead of using Selenium we can use requests and make things a lot less dependant on user installed software.
import requests

for x in range(1000):
    try:
        src = requests.get('https://emailfake.com').text
        emails = src.split('<span id="email_ch_text">')[1:]
        for email in emails:
            valid = email[:30]
        with open('emails.txt', 'a') as handle:
            # this will include the HTML Headers which I'll need to filter out.
            handle.write(valid + '\n')
    except Exception:
        print("Connection Closed. We've been noticed boys!")
