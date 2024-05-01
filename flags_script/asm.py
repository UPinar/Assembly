from typing import Callable, Literal
import operations as op

class AsmResult:
  def __init__(self, result_obj, **kwargs):
    self.result_int = result_obj.operand
    self.result_str = ' '.join(result_obj.binary_str[i:i+4] for i in range(0, len(result_obj.binary_str), 4))
    self.flags = kwargs

  def __str__(self):
    return f"result = {self.result_str} \nresult_hex = {self.hex()} \nflags = {self.flags}"
  
  def hex(self):
    return hex(self.result_int)
  
class Asm:
  def __init__(self, reg_size: Literal[8, 16, 32, 64]):
    self.reg_size = reg_size

  def perform_operation(self, operation: Callable, operand1, operand2_or_shift_count):
    result, flags_dict = operation(operand1, operand2_or_shift_count, self.reg_size)

    asm_result = AsmResult(result, **flags_dict)
    return asm_result

  def ADD(self, operand1, operand2):
    return self.perform_operation(op.add, operand1, operand2)

  def SUB(self, operand1, operand2):
    return self.perform_operation(op.sub, operand1, operand2)

  def SHL(self, operand1, shift_count):
    return self.perform_operation(op.shl, operand1, shift_count)

  def SAL(self, operand1, shift_count):
    return self.perform_operation(op.shl, operand1, shift_count)

  def SHR(self, operand1, shift_count):
    return self.perform_operation(op.shr, operand1, shift_count)

  def SAR(self, operand1, shift_count):
    return self.perform_operation(op.sar, operand1, shift_count)
  
  def MUL(self, operand1, operand2):
    return self.perform_operation(op.mul, operand1, operand2)
  
  def IMUL(self, operand1, operand2):
    return self.perform_operation(op.imul, operand1, operand2)
  
  def DIV(self, operand1, operand2):
    return self.perform_operation(op.div, operand1, operand2)
  
  def IDIV(self, operand1, operand2):
    return self.perform_operation(op.idiv, operand1, operand2)