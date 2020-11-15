import requests
from bs4 import BeautifulSoup
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import sys
import creds
import pandas as pd

def get_whisky():
    newlist = []
    url = 'https://www.thewhiskyexchange.com/new-products/standard-whisky'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    new_whisky = soup.find('li', {'class': 'np-postlist__item'}).find_all('li', {'class': 'product-list-item'})

    for item in new_whisky:
        new = {
        'name': item.find('p', {'class': 'name'}).text,
        'spec': item.find('p', {'class': 'spec'}).text,
        'desc': item.find('p', {'class': 'description'}).text.strip(),
        'price': item.find('p', {'class': 'price'}).text,
        }
        newlist.append(new)
    
    df = pd.DataFrame(newlist)
    return df


def emailnew(df):
    sender_email = "jdev36289@gmail.com"
    receiver_email = "jw.rooney86@gmail.com"
    password = creds.password
    message = MIMEMultipart("alternative")
    message["Subject"] = "New Whisky Today"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = """\
    New stuff in today!"""
    html = df.to_html(index=False)
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

emailnew(get_whisky())
