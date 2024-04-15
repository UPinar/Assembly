class Binary_wrapper:
  def __init__(self, decimal : int, bit_count : int): 
    self.bit_count = bit_count
    self.binary_str = self._get_binary_string(decimal)
    self.first_bit = int(self.binary_str[0])
    self.is_negative = self.first_bit == 1

  def __repr__(self) -> str:
    binary_str_with_spaces = ' '.join(self.binary_str[i:i+4] for i in range(0, len(self.binary_str), 4))
    return binary_str_with_spaces

  def __add__(self, other):
    total_val = int(self.binary_str, 2) + int(other.binary_str, 2)

    total_bitlength = total_val.bit_length()
    if total_bitlength > self.bit_count:
      total_val = total_val & ((1 << self.bit_count) - 1)

    result_obj = Binary_wrapper(total_val, self.bit_count)
    return result_obj, total_bitlength
  
  def __sub__(self, other):
    total_decimal = int(self.binary_str, 2) - int(other.binary_str, 2)
    total_Binary_wrapper = Binary_wrapper(total_decimal, self.bit_count)
    return total_Binary_wrapper
  
  def __lt__(self, other):
    return int(self.binary_str, 2) < int(other.binary_str, 2)
  
  def _get_binary_string(self, decimal : int):
    if decimal < 0:
      return self._get_twos_complement(decimal, self.bit_count)
    else :
      return bin(decimal)[2:].zfill(self.bit_count)

  def _get_twos_complement(self, value, bits):
    return bin(value & (1 << bits) - 1)[2:].zfill(bits)