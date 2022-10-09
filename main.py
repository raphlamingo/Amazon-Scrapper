import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
my_mail = 'igwerapheal2222@gmail.com'
password = '123PZass.'
send_to= 'igerapheal2@gmail.com'
url='https://www.amazon.com/Apple-MacBook-Touch-Intel-Quad-Core/dp/B082J572X8/ref=sr_1_3?keywords=macbook+pro&qid=1652543447&sprefix=macb%2Caps%2C1495&sr=8-3'
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
'Accept-Language':'en-US,en;q=0.9'
}
response=requests.get(url=url,headers=headers)
soup= BeautifulSoup(response.content, 'lxml')
#print(soup.prettify())
x=soup.find(name='span',class_='a-offscreen').get_text()
price= x.split('$')
new_price=float(price[1])
if new_price< 500:
    server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
    server.login(my_mail, password)
    server.sendmail(my_mail, send_to, f'Subject:New price alert\n\n the price of the Mac book is {new_price}')
