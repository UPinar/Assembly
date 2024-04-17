from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up webdriver instance
driver = webdriver.Firefox()  # or webdriver.Chrome()

# Navigate to the website
driver.get('https://flippybitandtheattackofthehexadecimalsfrombase16.com/')

container = driver.find_element(By.ID, "game-container")
# time.sleep(10)


body = driver.find_element(By.TAG_NAME, 'body')
game_over = driver.find_element(By.ID, "game-over")

keys_list = list()
hex_1_list = ['1', '2', '3', '4']
hex_2_list = ['5', '6', '7', '8']

def hex_to_bin(hex_str):
  int_val = int(hex_str, 16)
  return bin(int_val)[2:].zfill(4)

def keys_list_append(arg_1, arg_2 = None):  
  if arg_2 is None:
    for i in range(4):
      if arg_1[i] == '1':
        keys_list.append(hex_2_list[i])
  else:
    for i in range(4):
      if arg_1[i] == '1':
        keys_list.append(hex_1_list[i])
    for i in range(4):
      if arg_2[i] == '1':
        keys_list.append(hex_2_list[i])

logo_container = driver.find_element(By.ID, "logo")
while True:
  styles = logo_container.get_attribute('style')
  if "block" in styles:
    break

time.sleep(3)
container.click()
print("clicked")
while True:
  elements = driver.find_elements(By.XPATH, "//div[starts-with(@id, 'enemy-')]")
  for element in elements.copy():
    hex_str = element.get_attribute("innerHTML")
    print(f"element_count = {len(elements)}")
    if len(hex_str) == 1:
      keys_list_append(hex_to_bin(hex_str))
    else:
      hex_1 = hex_str[:1]
      hex_2 = hex_str[1:]
      keys_list_append(hex_to_bin(hex_1), hex_to_bin(hex_2))

    try:
      for key in keys_list:
        body.send_keys(key)
    finally:
      keys_list.clear()

    time.sleep(1.8)



# attack_value = driver.find_element(By.ID, "attackValue")
# while True:
#   time.sleep(1)
#   elements = driver.find_elements(By.XPATH, "//div[starts-with(@id, 'enemy-')]")
#   for element in elements:
#      print(element)
#      hex_str = element.get_attribute("innerHTML")
#      driver.execute_script("arguments[0].innerHTML = arguments[1];", attack_value, hex_str)
#      time.sleep(0.2)




# Number of screenshots to take
num_screenshots = 10

# Time interval between screenshots (in seconds)
interval = 1

# Take screenshots repeatedly
for i in range(num_screenshots):
    # Take a screenshot and save it to a local file
    driver.save_screenshot(f'screenshot{i}.png')

    # Wait for a certain amount of time before taking the next screenshot
    time.sleep(interval)

# Close the browser
