import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

nama = 'Ramadhan Adi Putra'
nik = '61180071'


driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'))  # Optional argument, if not specified will search path.
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSesr7iW4GGYFH5Saw3wGEA0iET3e1TLPIx7liHkAn0PTmyccw/viewform');
time.sleep(1)
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input"))).send_keys(nama)
#driver.find_element_by_class_name('quantumWizTextinputPaperinputInput.exportInput').send_keys(nama)
driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(nik)
driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]").send_keys("Engineer")
driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[1]").send_keys("ETM")
driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys("085718144588")
driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[12]/div/span/div/div/div[1]/input").send_keys("Pebayuran")
driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div").click()
driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]").click()
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("36")
driver.find_element_by_xpath('//*[@id="i102"]/div[3]/div').click()
driver.find_element_by_xpath('//*[@id="i113"]/div[2]').click()
driver.find_element_by_xpath('//*[@id="i136"]/div[2]').click()
#driver.find_element_by_xpath('//*[@id="i152"]/div[3]/div').click()
driver.find_element_by_xpath('//*[@id="i164"]/div[3]/div').click() #off/weekend/holiday
driver.find_element_by_xpath('//*[@id="i189"]/div[3]/div').click()
driver.find_element_by_xpath('//*[@id="i202"]/div[3]/div').click()
driver.find_element_by_xpath('//*[@id="i212"]/div[3]/div').click()
driver.find_element_by_xpath('//*[@id="i222"]/div[3]/div').click()
driver.find_element_by_xpath('//*[@id="i229"]/div[3]/div').click()
driver.find_element_by_xpath('//*[@id="i257"]/div[3]/div').click()
driver.find_element_by_xpath('//*[@id="i267"]/div[3]/div').click()
driver.find_element_by_xpath('//*[@id="i274"]/div[3]/div').click()
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span').click()

"""
from pyautogui import write
option_number = 3 # Choose option number here
# Put this where the program's supposed to select an option
for _ in range(option_number):
    write(['down'])
write(['enter'])
"""