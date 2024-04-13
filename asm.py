# ADD fonksiyonu implemente edilecek
# Sonuc yazdirilacak (HEX)
# Sonucun bit temsili yazdirilacak
# int veya hex degerleriyle argumanlar alinacak.


import sys
from operator import *

FLAGS = {'CF': None, 'OF': None}


class Binary_wrapper:
  def __init__(self, decimal) :
    self.binary_str = self._get_binary_string(decimal)
    self.max_bit = decimal.bit_length()
    self.first_bit_set = True if self.max_bit % 4 == 0 and self.max_bit else False

  def __add__(self, other):
    total_decimal = add(int(self.binary_str, 2), int(other.binary_str, 2))
    total_Binary_wrapper = Binary_wrapper(total_decimal)
    return total_Binary_wrapper
  
  def _get_binary_string(self, decimal : int):
    return bin(decimal).lstrip('0b')
  

def check_argument(input : str):
  decimal = None
  if input.startswith('0x'): 
    decimal = int(input.lstrip('0x'), 16)
  elif input.startswith('0b'):
    decimal = int(input.lstrip('0b'), 2)
  elif isinstance(input, int):
    decimal = input

  fixed_bit = Binary_wrapper(decimal)
  return fixed_bit
 
# script_name = sys.argv[0] -> no need for the script_name

if len(sys.argv) != 4:
  raise ValueError("Provide instruction and 2 values(hex, decimal)")
else:
  instruction = sys.argv[1]

  instructions = ["ADD", "SUM"]
  if instruction not in instructions:
    raise ValueError("Instruction is not valid")
  else:
    first_arg = check_argument(sys.argv[2])
    second_arg = check_argument(sys.argv[3])

    if "ADD" == instruction:
      max_bit_args = max([first_arg.max_bit, second_arg.max_bit] )

      

    # if 'ADD' == instruction:
    #   pass
    # elif 'SUB' == instruction:
    #   pass





hex_str = "FFFFF"
binary_val = int(hex_str, 16)

print(binary_val)
# binary_val = bin(decimal_val)[2:]

# my_int.bit_length() % 4 == 0


