from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading

# Set up webdriver instance
driver = webdriver.Firefox()  

# Navigate to the website
driver.get('https://flippybitandtheattackofthehexadecimalsfrombase16.com/')

# To start the game
start_container = driver.find_element(By.ID, "game-container")
# To send keys to the game
body = driver.find_element(By.TAG_NAME, 'body')
# To eximate nearest time to start the game
logo_container = driver.find_element(By.ID, "logo")
# To get the score and return
score_container = driver.find_element(By.ID, "score")
# To check if the game is over
game_over_container = driver.find_element(By.ID, "game-over")


# converting hex to binary with 0's padding
def hex_to_bin(hex_str):
  int_val = int(hex_str, 16)
  return bin(int_val)[2:].zfill(4)

def check_game_over():
  if game_over_container.is_displayed():
    score = score_container.get_attribute("innerHTML")
    print(f"Score is = {score}")
    driver.quit()
    exit()

def main():
  def keys_list_append(arg_1, arg_2 = None):  
    length = len(arg_1)
    if arg_2 is None:
      for i in range(length):
        if arg_1[i] == '1':
          keys_list.append(hex_2_tuple[i])
    else:
      for i in range(length):
        if arg_1[i] == '1':
          keys_list.append(hex_1_tuple[i])
      for i in range(length):
        if arg_2[i] == '1':
          keys_list.append(hex_2_tuple[i])

  # START GAME
  while True:
    styles = logo_container.get_attribute('style')
    if "block" in styles:
      break

  time.sleep(3)
  start_container.click()

  keys_list = list()
  hex_1_tuple = ('1', '2', '3', '4')
  hex_2_tuple = ('5', '6', '7', '8')

  removed_elements = list()

  # GAME LOOP
  while True:
    while True:
      elements = driver.find_elements(By.XPATH, "//div[starts-with(@id, 'enemy-')]")
      elements = [item for item in elements if item not in removed_elements]
      element_count = len(elements)

      if element_count > 0:
        break

    removed_elements.clear()

    # checking if a hex number is "xx" or "x" format
    for element in elements:
      check_game_over()
      hex_str = element.get_attribute("innerHTML")
      if len(hex_str) == 1:
        keys_list_append(hex_to_bin(hex_str))
      elif len(hex_str) == 2:
        hex_first_digit = hex_str[0]
        hex_second_digit = hex_str[1]
        keys_list_append(hex_to_bin(hex_first_digit), hex_to_bin(hex_second_digit))

      # sending keys to the game
      try:
        for key in keys_list:
          body.send_keys(key)
      finally:
        keys_list.clear()
        removed_elements.append(element)
        time.sleep(0.9) # magic number that works

__name__ == '__main__' and main()
