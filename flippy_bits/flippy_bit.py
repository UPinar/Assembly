from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import StaleElementReferenceException
import numpy as np
import time

# --------SETUP--------
mute_option = Options()
mute_option.set_preference("media.volume_scale", "0.0")
driver = webdriver.Firefox(options=mute_option)
driver.get('https://flippybitandtheattackofthehexadecimalsfrombase16.com/')
driver.execute_script("""
    var elements = document.querySelectorAll('td[width="60%"]');
    if (elements.length > 1) {
        elements[1].removeAttribute('width');  // Remove the width attribute from the second td
    }
    if (elements.length > 0) {
        elements[0].remove();  // Remove the first td
    }
""")

screen_width = driver.execute_script("return screen.width")
screen_height = driver.execute_script("return screen.height")
driver.set_window_size(screen_width // 2, screen_height)
driver.set_window_position(0, 0)

game_container = driver.find_element(By.ID, "game-container")
body = driver.find_element(By.TAG_NAME, 'body')
score_container = driver.find_element(By.ID, "score")

BINARY_LENGTH = 8

# --------HELPER FUNCTIONS--------
def game_over():
  score = score_container.get_attribute("innerHTML")
  print(f"Score is = {score}")
  driver.quit()
  exit()

def start_game():
  time.sleep(6)
  game_container.click()


# --------MAIN FUNCTION--------
def main():
  def set_hit_keys_arr(hex_str: str):  
    nonlocal hit_keys
    
    binary_string = bin(int(hex_str, 16))[2:].zfill(BINARY_LENGTH)
    binary_array = np.array([int(char) for char in binary_string])
    hit_keys = np.array([key for key, bit in zip(keys, binary_array) if bit == 1])
  
  start_game()

  enemies_shot = dict()
  keys = ('1', '2', '3', '4','5', '6', '7', '8')
  hit_keys = np.array([])

  # --------GAME LOOP--------
  while True:
    while True:
      visible_enemies = np.array(driver.find_elements(By.XPATH, "//div[starts-with(@id, 'enemy-')]"))
      enemies_to_hit = np.array([enemy for enemy in visible_enemies if enemy not in enemies_shot])
      if len(enemies_to_hit): 
        break

    for enemy in enemies_to_hit:
      try:
        enemy_hex = enemy.get_attribute("innerHTML")
        set_hit_keys_arr(enemy_hex)
        body.send_keys(*hit_keys)
        hit_keys = np.array([])
        enemies_shot[enemy] = True
      except StaleElementReferenceException:
          game_over()

      
__name__ == '__main__' and main()
