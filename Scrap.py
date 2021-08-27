import requests
from bs4 import BeautifulSoup
import time
from mail import sending_email
import csv
from datetime import date

today = str(date.today()) + '.csv'
# for creating a csv file using csv modu;e
csv_file = open(today , 'w')
csv_writer = csv. writer(csv_file) 
csv_writer.writerow(['Stock Name', 'Current Value', 'Previous Close', 'Open', 'Bid', 'Ask' , "Day's Range", '52 Week Rage', 'Volume', 'Avg. Volume'])

#web scrapping using beautiful soup module
urls = ['https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch', 'https://finance.yahoo.com/quote/FB?p=FB&.tsrc=fin-srch' , 'https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch']

for url in urls:
    
    stock = []
    #for getting rquests mimicking as as a browser
    header = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4)AppleWebKit/600.7.12 (KHTML, like Gecko)Version/8.0.7 Safari/600.7.12'}


    html_page = requests.get(url, header)

    soup = BeautifulSoup(html_page.content, 'lxml' )



    stock_header = soup.find_all('div', id = "quote-header-info")
    stock_title = (stock_header[0].find('h1').get_text())
    stock_value = (stock_header[0].find('span', class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").get_text())
    
    stock.append(stock_title)
    stock.append(stock_value)

    stock_table = soup.find_all('div', class_= "D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)" )



    for i in range(0,8):
        data = stock_table[0].find_all('td', class_ ="C($primaryColor) W(51%)" )
        value = stock_table[0].find_all('td', class_ = "Ta(end) Fw(600) Lh(14px)")
        stock.append(value[i].get_text())
        
    
    csv_writer.writerow(stock)
    
    time.sleep(2)

sending_email(filename=today)

  

