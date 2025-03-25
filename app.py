from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep

driver = webdriver.Chrome()
driver.get('https://clone-olx-devaprender.netlify.app/')
sleep(5)

produtos = driver.find_elements(By.XPATH,"//h3[@class='text-base text-gray-900 line-clamp-2 mb-1 hover:text-[#6E0AD6]']")
precos = driver.find_elements(By.XPATH,"//span [@class='text-2xl font-bold text-gray-900']")

for produto, preco in zip(produtos,precos):
	with open('preços.csv', 'a',encoding='utf-8') as arquivo:
	    arquivo.write(f'{produto.text},{preco.text}{os.linesep}')

input('')