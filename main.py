import os
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import csv
import base64
import time
import urllib.request

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


service = ChromeService(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

SAVE_FOLDER = 'titul/'

GOOGLE_IMAGES = 'https://www.google.com/search?q=titul%20varaqasi&tbm=isch&hl=en&tbs=rimg:CWrZwx1KN5tUYVSpDED7jPWRsgIMCgIIABAAOgQIABAAwAIA&sa=X&ved=0CB4QuIIBahcKEwjAvOeqnf7-AhUAAAAAHQAAAAAQBw&biw=1349&bih=625'

driver.get(GOOGLE_IMAGES)


# Scroll to the end of the page
def scroll_to_end():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    print('scroll done')
# scroll_to_end()
counter = 0
for i in range(2):     
    scroll_to_end()
    image_elements = driver.find_elements(By.CLASS_NAME, "rg_i")
  
    print(len(image_elements))
    for image in image_elements: 
        if (image.get_attribute('src') is not None):
            my_image = image.get_attribute('src').split('data:image/jpeg;base64,')
            filename = SAVE_FOLDER + 'titul_varaq'+str(counter)+'.jpeg'
            
            if(len(my_image) >1): 
                with open(filename, 'wb') as f: 
                    f.write(base64.b64decode(my_image[1]))
                    print(base64.b64decode(my_image[1]))
            else: 
                print(image.get_attribute('src'))
                urllib.request.urlretrieve(image.get_attribute('src'), SAVE_FOLDER + 'wheel'+ str(counter)+'.jpeg')
            counter += 1