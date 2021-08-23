from selenium import webdriver
from msedge.selenium_tools import Edge,EdgeOptions
from time import sleep
import threading


def bot():
	options = EdgeOptions()
	options.use_chromium = True
	driver = Edge(options=options,executable_path=r'./msedgedriver.exe')

	driver.get('https://popcat.click/')


	element = driver.find_element_by_class_name('cat-img')

	while True:
		element.click()
		sleep(.0375)

for _ in range(10):
	x = threading.Thread(target = bot)
	x.start()