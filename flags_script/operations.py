import binary_wrapper as bw

FLAGS = {'CF': None, 'OF': None, 'SF': None, 'ZF': None }

def add(operand1, operand2, bit_length):
    arg_1 = bw.Binary_wrapper(operand1, bit_length)
    arg_2 = bw.Binary_wrapper(operand2, bit_length)
    result_obj, total_bit_length = arg_1 + arg_2

    # Checking Carry Flag (unsigned)
    if total_bit_length > bit_length:
      FLAGS['CF'] = 1
    else: 
      FLAGS['CF'] = 0

    # Checking Overflow Flag (signed)
    # If both operands have the same sign and the result has a different sign, then the overflow flag is set.
    if not (arg_1.sign_bit ^ arg_2.sign_bit) and arg_1.sign_bit != result_obj.sign_bit:
      FLAGS['OF'] = 1
    else:
      FLAGS['OF'] = 0

    # Checking Sign Flag
    FLAGS['SF'] = result_obj.sign_bit
    # Checking Zero Flag
    FLAGS['ZF'] = 1 if result_obj == bw.Binary_wrapper(0, bit_length) else 0

    return result_obj, FLAGS

def sub(operand1, operand2, bit_length):
    arg_1 = bw.Binary_wrapper(operand1, bit_length)
    arg_2 = bw.Binary_wrapper(operand2, bit_length)
    result_obj = arg_1 - arg_2

    # Checking Carry Flag (unsigned)
    if arg_1 < arg_2:
      FLAGS['CF'] = 1
    else: 
      FLAGS['CF'] = 0

    # Checking Overflow Flag (signed)
    if arg_1.sign_bit != arg_2.sign_bit and arg_1.sign_bit != result_obj.sign_bit:
      FLAGS['OF'] = 1
    else:
      FLAGS['OF'] = 0

    # Checking Sign Flag
    FLAGS['SF'] = result_obj.sign_bit
    # Checking Zero Flag
    FLAGS['ZF'] = 1 if result_obj == bw.Binary_wrapper(0, bit_length) else 0

    return result_obj, FLAGS

def shl(operand1, shift_count, bit_length):
    arg_1 = bw.Binary_wrapper(operand1, bit_length)
    result_obj = arg_1 << shift_count

    # Checking Overflow Flag
    if shift_count == 0:
      FLAGS['OF'] = 'Not affected'
    elif shift_count == 1:
      FLAGS['OF'] = arg_1.sign_bit ^ result_obj.sign_bit
    else:
      FLAGS['OF'] = "Undefined"
      

    # Checking Carry Flag
    if shift_count == 0:
      FLAGS['CF'] = 'Not affected'
    elif shift_count <= bit_length:
      FLAGS['CF'] = int(arg_1.binary_str[shift_count - 1])
    else:
      FLAGS['CF'] = 0

    # Checking Sign Flag
    FLAGS['SF'] = result_obj.sign_bit

    # Checking Zero Flag
    FLAGS['ZF'] = 1 if result_obj == bw.Binary_wrapper(0, bit_length) else 0

    return result_obj, FLAGS

def sar(operand1, shift_count, bit_length):
  arg_1 = bw.Binary_wrapper(operand1, bit_length)

  if arg_1.sign_bit == 0:
    result_obj = arg_1 >> shift_count
  else:
    if shift_count >= bit_length:
      result_obj = bw.Binary_wrapper(-1, bit_length)
    else:
      sar_object = arg_1 >> shift_count

      result_obj_operand = sar_object.operand
      mask = ((1 << shift_count) - 1) << (bit_length - shift_count)
      result_obj_operand |= mask
      result_obj = bw.Binary_wrapper(result_obj_operand, bit_length)

  # SAR, OF is set to the high-order bit of the original operand.
  if shift_count == 0:
    FLAGS['OF'] = 'Not affected'
  elif shift_count == 1:
    FLAGS['OF'] = arg_1.sign_bit
  else:
    FLAGS['OF'] = "Undefined"
    
  # Checking Carry Flag
  if shift_count == 0:
    FLAGS['CF'] = 'Not affected'
  elif shift_count >= bit_length :
    if arg_1.sign_bit == 0:
      FLAGS['CF'] = 0
    else:
      FLAGS['CF'] = 1
  else:
    FLAGS['CF'] = int(arg_1.binary_str[bit_length - shift_count])

  # Checking Sign Flag
  FLAGS['SF'] = result_obj.sign_bit

  # Checking Zero Flag
  FLAGS['ZF'] = 1 if result_obj == bw.Binary_wrapper(0, bit_length) else 0

  # want to return the total and the flags
  return result_obj, FLAGS

def shr(operand1, shift_count, bit_length):
  arg_1 = bw.Binary_wrapper(operand1, bit_length)
  result_obj = arg_1 >> shift_count

  # For SHR, OF is set to 0 for all single shifts.
  if shift_count == 0:
    FLAGS['OF'] = "Not affected"
  elif shift_count == 1:
    FLAGS['OF'] = 0
  else:
    FLAGS['OF'] = "Undefined"

  # Checking Carry Flag
  if shift_count == 0:
    FLAGS['CF'] = 'Not affected'
  elif shift_count <= bit_length:
    FLAGS['CF'] = int(arg_1.binary_str[bit_length - shift_count])
  elif shift_count > bit_length:
    FLAGS['CF'] = 0

  # Checking Sign Flag
  FLAGS['SF'] = result_obj.sign_bit
  # Checking Zero Flag
  FLAGS['ZF'] = 1 if result_obj == bw.Binary_wrapper(0, bit_length) else 0

  # want to return the total and the flags
  return result_obj, FLAGS

def mul(operand1, operand2, bit_length):
  arg_1 = bw.Binary_wrapper(operand1, bit_length)
  arg_2 = bw.Binary_wrapper(operand2, bit_length)
  result_obj = arg_1 * arg_2

  # INTEL MANUAL
  # The OF and CF flags are set to 0 if the upper half of the result is 0; 
  # otherwise, they are set to 1. 
  # The SF, ZF, AF, and PF flags are undefined.

  # Checking Carry Flag and Overflow Flag
  if result_obj.operand >> bit_length == 0:
    FLAGS['CF'] = 0
    FLAGS['OF'] = 0
  else:
    FLAGS['CF'] = 1
    FLAGS['OF'] = 1

  FLAGS['SF'] = "Undefined"
  FLAGS['ZF'] = "Undefined"

  return result_obj, FLAGS

def imul(operand1, operand2, bit_length):
  arg_1 = bw.Binary_wrapper(operand1, bit_length)
  arg_2 = bw.Binary_wrapper(operand2, bit_length)
  result_obj = arg_1.imul(arg_2)

  # INTEL MANUAL
  # CF and OF flags are set when the result must be truncated to fit in the destination operand size and cleared when the result fits exactly in the destination operand size. 
  # The SF, ZF, AF, and PF flags are undefined.

  if result_obj.operand.bit_length() > bit_length:
    FLAGS['CF'] = 1
    FLAGS['OF'] = 1
  else:
    FLAGS['CF'] = 0
    FLAGS['OF'] = 0


  FLAGS['SF'] = "Undefined"
  FLAGS['ZF'] = "Undefined"

  return result_obj, FLAGS

def div(operand1, operand2, bit_length):
  arg_1 = bw.Binary_wrapper(operand1, bit_length)
  arg_2 = bw.Binary_wrapper(operand2, bit_length // 2)

  if arg_2.operand == 0:
    raise ZeroDivisionError("Division by zero")

  result_obj = arg_1 // arg_2

  # INTEL MANUAL
  # The CF, OF, SF, ZF, AF, and PF flags are undefined.

  FLAGS['CF'] = "Undefined"
  FLAGS['OF'] = "Undefined"
  FLAGS['SF'] = "Undefined"
  FLAGS['ZF'] = "Undefined"

  return result_obj, FLAGS

def idiv(operand1, operand2, bit_length):
  arg_1 = bw.Binary_wrapper(operand1, bit_length)
  arg_2 = bw.Binary_wrapper(operand2, bit_length // 2)

  if arg_2.operand == 0:
    raise ZeroDivisionError("Division by zero")

  result_obj = arg_1.idiv(arg_2)

  # INTEL MANUAL
  # The CF, OF, SF, ZF, AF, and PF flags are undefined.

  FLAGS['CF'] = "Undefined"
  FLAGS['OF'] = "Undefined"
  FLAGS['SF'] = "Undefined"
  FLAGS['ZF'] = "Undefined"

  return result_obj, FLAGS