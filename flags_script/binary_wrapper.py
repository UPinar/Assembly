class Binary_wrapper:
  def __init__(self, operand : int, bit_length : int): 
    self.operand = operand
    self.bit_length = bit_length
    self.binary_str = self._get_binary_string()
    self.sign_bit = int(self.binary_str[0])

  def __repr__(self) -> str:
    binary_str_with_spaces = ' '.join(self.binary_str[i:i+4] for i in range(0, len(self.binary_str), 4))
    return binary_str_with_spaces

  def __add__(self, other):
    total_val = self.operand + other.operand

    total_bit_length = total_val.bit_length()
    if total_bit_length > self.bit_length:
      total_val = total_val & ((1 << self.bit_length) - 1)

    result_obj = Binary_wrapper(total_val, self.bit_length)
    return result_obj, total_bit_length
  
  def __sub__(self, other):
    total_val = self.operand - other.operand
    
    result_obj = Binary_wrapper(total_val, self.bit_length)
    return result_obj
  
  def __lshift__(self, shift_count):
    if shift_count > 0:
      total_val = self.operand << shift_count
      result_obj = Binary_wrapper(total_val, self.bit_length)
      return result_obj
    elif shift_count == 0:
      return self
    else:
      raise ValueError("Shift count must be a non-negative integer")
    
  def __rshift__(self, shift_count):
    if shift_count > 0:
      total_val = self.operand >> shift_count
      result_obj = Binary_wrapper(total_val, self.bit_length)
      return result_obj
    elif shift_count == 0:
      return self
    else:
      raise ValueError("Shift count must be a non-negative integer")
      
  def __lt__(self, other):
    return self.operand < other.operand
  
  def __eq__(self, other):
    return self.operand == other.operand and self.bit_length == other.bit_length
  
  def _get_binary_string(self):
    if self.operand < 0:
      return bin(self.operand & (1 << self.bit_length) - 1)[2:].zfill(self.bit_length)
    else :
      binary_str = bin(self.operand)[2:]
      if len(binary_str) > self.bit_length:
        return binary_str[-self.bit_length:]
      else:
        return binary_str.zfill(self.bit_length)