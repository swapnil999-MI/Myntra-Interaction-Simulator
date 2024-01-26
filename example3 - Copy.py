from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

op = webdriver.ChromeOptions()
op.add_experimental_option('detach',True)

driver = webdriver.Chrome(options = op)

driver.get("https://www.myntra.com/")

search = driver.find_element(By.XPATH, value = '//*[@id="desktop-header-cnt"]/div[2]/div[3]/input')

search.send_keys("pants")

search.send_keys(Keys.ENTER)

wait = WebDriverWait(driver, 15)
element = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="desktopSearchResults"]/div[2]/section/ul')))
#element = driver.find_element(By.XPATH,value='//*[@id="desktopSearchResults"]/div[2]/section/ul')
list = element.find_elements(By.TAG_NAME,value="li")
match = list[6]
match.click()

new_window_handle = driver.window_handles[1]
driver.switch_to.window(new_window_handle)


size = driver.find_element(By.XPATH,value='//*[@id="sizeButtonsContainer"]/div[2]/div[1]')
size.click()
addtocart = driver.find_element(By.XPATH,value='//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[2]/div[2]/div/div[1]')
addtocart.click()


wait = WebDriverWait(driver, 40)
tocart = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="desktop-header-cnt"]/div[2]/div[2]/a[2]/span[1]')))
#tocart= driver.find_element(By.XPATH,value='//*[@id="desktop-header-cnt"]/div[2]/div[2]/a[2]')
tocart.click()

new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

remove1 = driver.find_element(By.XPATH,value='//*[@id="cartItemsList"]/div[1]/div/div/div[2]/div[1]/div/div[1]')
remove1.click()

remove = driver.find_element(By.XPATH,value='//*[@id="appContent"]/div/div/div/div[2]/div[1]/div[4]/div[3]/div[1]/button')
remove.click()

finalremove = driver.find_element(By.XPATH,value='//*[@id="appContent"]/div/div/div/div[2]/div[1]/div[4]/div[4]/div/div/div[2]/div[1]/button')
finalremove.click()
