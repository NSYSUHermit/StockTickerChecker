# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 15:46:41 2020

@author: Henry4_Lin
"""

from bs4 import BeautifulSoup
import requests
 
class Stock:
    #建構式
    def __init__(self, *stock_numbers):
        self.stock_numbers = stock_numbers
    
    #爬取
    def scrape(self):
    	result = list()  #最終結果
    	for stock_number in self.stock_numbers:
    		response = requests.get(
    			"https://tw.stock.yahoo.com/q/q?s=" + stock_number)
    		soup = BeautifulSoup(response.text.replace("加到投資組合", ""), "lxml")	
    		stock_date = soup.find(
    			"font", {"class": "tt"}).getText().strip()[-9:]  #資料日期
    		tables = soup.find_all("table")[2]  #取得網頁中第三個表格(索引從0開始計算)
    		tds = tables.find_all("td")[0:11]  #取得表格中1到10格
    		result.append((stock_date,) +
    			tuple(td.getText().strip() for td in tds))		
    	return result
		
if __name__ == '__main__':
    ticker = input('Input tw ticker：')
    while float(ticker) >= 1000:
        stock = Stock(str(ticker))  #建立Stock物件
        print("date, ticker, time, deal, buy, sell, up&dw, volume, ytd-closing, open, highest, lowest")
        print(stock.scrape())  #印出爬取結果
        ticker = input('Input tw ticker：')
    input('Press any key to leave')
  
