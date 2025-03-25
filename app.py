from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep

driver = webdriver.Chrome()
driver.get('https://devaprender-play.netlify.app/')
sleep(5)

produtos = driver.find_elements(By.XPATH,"//h3[@class='text-lg font-semibold text-gray-900 group-hover:text-indigo-600']")
precos = driver.find_elements(By.XPATH,"//p [@class='text-2xl font-bold text-indigo-600']")

for produto, preco in zip(produtos,precos):
	with open('preços.csv', 'a',encoding='utf-8') as arquivo:
	    arquivo.write(f'{produto.text},{preco.text}{os.linesep}')

input('')