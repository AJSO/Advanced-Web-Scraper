import requests
from bs4 import BeautifulSoup
import smtplib
import timeit

URL = 'https://www.amazon.ae/Apple-iPhone-Pro-without-FaceTime/dp/B07XTJ9RT2/ref=sr_1_2?crid=I4T38B4ZTND2&keywords=iphone+11+pro+max&qid=1571268485&sprefix=iphone%2Caps%2C320&sr=8-2'
headers = { "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36' }


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    #print(soup.prettify())
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[4:12])

    if (converted_price < 1700.0) :
        send_mail()
    print(title.strip())
    print(converted_price.strip())

    if (converted_price > 1700.0) :
        send_mail()

def send_mail():
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.ehlo()
     server.starttls()
     server.ehlo()

     server.login('your-email','password')

     subject = 'Price fell down'
     body = 'Check the amazon link ' + URL + ' the price just dropped.'

     msg = f"Subject:{subject}\n\n{body}"
    #from
    #to
    #message
     server.sendmail(
         'your-email',
         'reciever-email',
         msg
     )
     print('Email has been sent!!')
     server.quit()
     
while True:
    check_price()
    timeit.Timer(60*60)
