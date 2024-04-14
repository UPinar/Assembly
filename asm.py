import sys
import binary_wrapper as bw

FLAGS = {'CF': None, 'OF': None, 'SF': None, 'ZF': None }
REG_SIZES = [8, 16, 32, 64]

def create_wrappers(input_str : str, bit_count : int):
  decimal = None
  if input_str.startswith('0x'): 
    decimal = int(input_str.lstrip('0x'), 16)
  elif input_str.startswith('0b'):
    decimal = int(input_str.lstrip('0b'), 2)
  else:
    decimal = int(input_str)

  fixed_bit = bw.Binary_wrapper(decimal, bit_count)
  return fixed_bit
  
def control_args() :
  if len(sys.argv) != 4:
    print("Provide instruction and 2 values(hex, decimal)")
    exit()
  
def control_instruction(instruction_list, instruction : str):
  if instruction not in instruction_list:
    print(f"Instruction must be one of these : \n {instruction_list}")
    exit()

def create_instruction_list():
  return [f"ADD{i}" for i in REG_SIZES] + [f"SUB{i}" for i in REG_SIZES]
  
def add(arg_1, arg_2, reg_size):
  total = arg_1 + arg_2
  print(f"Result: {total.binary_str}")

  # Checking Carry Flag (unsigned)
  if total.bit_count > reg_size:
    FLAGS['CF'] = 1
  else: 
    FLAGS['CF'] = 0

  # Checking Overflow Flag (signed)
  if not (arg_1.first_bit ^ arg_2.first_bit) and total.first_bit :
    FLAGS['OF'] = 1
  else:
    FLAGS['OF'] = 0

  # Checking Sign Flag
  FLAGS['SF'] = total.first_bit

  # Checking Zero Flag
  FLAGS['ZF'] = 1 if total == bw.Binary_wrapper(0, reg_size) else 0


def sub(arg_1, arg_2, reg_size):
  total = arg_1 - arg_2
  print(f"Result: {total.binary_str}")

  # Checking Carry Flag (unsigned)
  if arg_1 < arg_2:
    FLAGS['CF'] = 1
  else: 
    FLAGS['CF'] = 0

  # Checking Overflow Flag (signed)
  if total.first_bit != arg_1.first_bit:
    FLAGS['OF'] = 1
  else:
    FLAGS['OF'] = 0

  # Checking Sign Flag
  FLAGS['SF'] = total.first_bit

  # Checking Zero Flag
  FLAGS['ZF'] = 1 if total == bw.Binary_wrapper(0, reg_size) else 0

def print_flags() :
  for flag, value in FLAGS.items():
    print(f"{flag} = {value}", end="|")

def main():
  control_args()

  instruction_list = create_instruction_list()

  input_instruction = sys.argv[1]
  control_instruction(instruction_list, input_instruction)

  reg_size = int(input_instruction[3:])
  instuction_type = input_instruction[:3]
  arg_1 = create_wrappers(sys.argv[2], reg_size)
  arg_2 = create_wrappers(sys.argv[3], reg_size)

  print(arg_1, arg_2)

  if "ADD" == instuction_type:
    add(arg_1, arg_2, reg_size)
  elif "SUB" == instuction_type:
    sub(arg_1, arg_2, reg_size)

  print_flags()

if __name__ == "__main__":
  main()
