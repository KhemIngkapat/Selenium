#import
from selenium import webdriver
from selenium.webdriver.common.keys  import Keys
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from msedge.selenium_tools import Edge,EdgeOptions
from time import sleep,time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from dotenv import dotenv_values

#define the driver

options = EdgeOptions()
options.use_chromium = True
driver = Edge(options=options,executable_path=r'./msedgedriver.exe')

driver.get('https://xreading.com/login/index.php')

config = dotenv_values('.env')

#login

username = driver.find_element_by_xpath('//input[@type="text"]')

username.send_keys(config['XREADINGEMAIL'])

password = driver.find_element_by_xpath('//input[@type="password"]')

password.send_keys(config['XREADINGPASSWORD'])

password.send_keys(Keys.RETURN)

#get the total word

word = driver.find_element_by_xpath('//*[@id="region-main"]/div/div[4]/div/div[1]/div[2]/div[2]/div[1]/ul[1]/li[2]').text

#function to strNum to num
convertStrToInt = lambda word : int(''.join(word.split(' ')[-1].split(',')))

totalWord = convertStrToInt(word)

print(f'total Word : {totalWord}')

#round int function
def rounder(num):
	digit = len(str(num)) -2

	return math.ceil(num/(10**digit))*(10**digit)

roundedWord = rounder(totalWord)

roundedTime = roundedWord/230 #word per minutes

#click the continue reading or read again(it wont work with read again)
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

#get the start time

startTime = time()

#estimated round of working

print(f'Should Be Working For { math.ceil(roundedTime / (200/60))} Round')

#loop clicking

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
		print('TimeoutException')
		continue

#get to the last page and quit the book

input('Continue to the final page?')

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









