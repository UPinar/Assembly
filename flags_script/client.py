import asm as asm

def main():

  asm_obj = asm.Asm(8)
  result = asm_obj.SAR(0b10101010, 4)
  print(result)
  
  # output ->
  # result = 11111010
  # flags = {'CF': 1, 'OF': 'Undefined', 'SF': 1, 'ZF': 0}

main()
