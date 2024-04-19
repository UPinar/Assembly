from typing import Callable, Literal
import operations as op

class AsmResult:
  def __init__(self, result_obj, **kwargs):
    self.result_int = result_obj.operand
    self.result_str = result_obj.binary_str
    self.flags = kwargs

  def __str__(self):
    return f"result = {self.result_str} \nflags = {self.flags}"
  
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