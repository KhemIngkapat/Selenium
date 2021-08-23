from selenium import webdriver
from selenium.webdriver.common.keys  import Keys
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from msedge.selenium_tools import Edge,EdgeOptions
from time import sleep,time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

options = EdgeOptions()
options.use_chromium = True
driver = Edge(options=options,executable_path=r'./msedgedriver.exe')

driver.get('https://xreading.com/blocks/institution/assignments.php?id=49381')

username = driver.find_element_by_xpath('//input[@type="text"]')

username.send_keys('p00948@plearnpattana.ac.th')

password = driver.find_element_by_xpath('//input[@type="password"]')

password.send_keys('password')

password.send_keys(Keys.RETURN)

word = driver.find_element_by_xpath('//*[@id="region-main"]/div/div[4]/div/div[1]/div[2]/div[2]/div[1]/ul[1]/li[2]').text

convertStrToInt = lambda word : int(''.join(word.split(' ')[-1].split(',')))

totalWord = convertStrToInt(word)

print(f'total Word : {totalWord}')

def rounder(num):
	digit = len(str(num)) -1

	return math.ceil(num/(10**digit))*(10**digit)

roundedWord = rounder(totalWord)

roundedTime = roundedWord/230

roundedTimePerPage = round(roundedTime/5,2)
try:
	continueRead = driver.find_element_by_xpath('//*[@id="region-main"]/div/div[4]/div/div[1]/div[2]/div[2]/div[2]/a')
	continueRead.click()
except Exception as e:
	readAgain = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/section[1]/div/div[4]/div/div[1]/div[2]/div[2]/div[2]/input[1]')
	readAgain.click()
	sleep(1)
	confirmButton = driver.find_element_by_xpath('//*[@id="page-institution"]/div[4]/div/div/div[3]/button[1]')
	confirmButton.click()


print(f'roundedWord : {roundedWord}')
print(f'roundedTime : {roundedTime}')
print(f'roundedTimePerPage : {roundedTimePerPage}')

startTime = time()

print(f'Should Be Working For { math.ceil(roundedTime / (200/60))} Round')

while (time() - startTime  )/60 < roundedTime:
	try:
		for _ in range(5):
			sleep(15)
			page =driver.find_element_by_tag_name('body')
			page.send_keys(Keys.END)
			sleep(5)
			nextButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'next-slide')))
			nextButton.click()
		for _ in range(5):
			sleep(15)
			page =driver.find_element_by_tag_name('body')
			page.send_keys(Keys.HOME)
			sleep(5)
			previousButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'previous-slide')))
			previousButton.click()
		print(f"Working For : {round((time() - startTime  )/60,2)} Minutes")
	except TimeoutException:
		print('Working On One Page AFK')
		for i in range(100):
			page =driver.find_element_by_tag_name('body')
			page.send_keys(Keys.END)
			sleep(20)
			page.send_keys(Keys.HOME)
			sleep(20)
		continue

while True:
	try:
		sleep(5)
		page =driver.find_element_by_tag_name('body')
		page.send_keys(Keys.END)
		nextButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'next-slide')))
		nextButton.click()
	except TimeoutException:
		print('End Of Program')
		closeBook = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'close-book')))
		closeBook.click()
		break









