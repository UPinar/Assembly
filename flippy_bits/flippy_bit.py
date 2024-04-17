from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
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
# score_container = driver.find_element(By.ID, "score")
# game_over_container = driver.find_element(By.ID, "game-over")


BINARY_LENGTH = 8

# --------HELPER FUNCTIONS--------
def hex_to_binary(hex_str):
  int_val = int(hex_str, 16)
  return bin(int_val)[2:].zfill(BINARY_LENGTH)

# def control_game_is_over():
#   if game_over_container.is_displayed():
#     score = score_container.get_attribute("innerHTML")
#     print(f"Score is = {score}")
#   driver.quit()
#   exit()


def main():
  def get_hit_keys_arr(hex_str: str):  
    nonlocal hit_keys
    binary_string = bin(int(hex_str, 16))[2:].zfill(BINARY_LENGTH)

    binary_array = np.array([int(char) for char in binary_string])
    hit_keys = np.array([key for key, bit in zip(keys, binary_array) if bit == 1])
    return hit_keys
  
  # --------CLICK TO START--------
  time.sleep(6)
  game_container.click()


# --------GAME STARTS--------
  enemies_shot = dict()
  keys = ('1', '2', '3', '4','5', '6', '7', '8')
  hit_keys = np.array([])

  while True:

    while True:
      visible_enemies = np.array(driver.find_elements(By.XPATH, "//div[starts-with(@id, 'enemy-')]"))
      enemies_to_hit = np.array([enemy for enemy in visible_enemies if enemy not in enemies_shot])

      if len(enemies_to_hit) > 0:
          break

    for enemy in enemies_to_hit:
      enemy_hex = enemy.get_attribute("innerHTML")
      hit_keys_arr = get_hit_keys_arr(enemy_hex)
      body.send_keys(*hit_keys_arr)
      hit_keys = np.array([])
      enemies_shot[enemy] = True


__name__ == '__main__' and main()
