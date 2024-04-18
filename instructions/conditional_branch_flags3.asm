%include "io64.inc"

section .text
  global CMAIN
CMAIN:
  ; GREATER, LESS -> CMP left operand, right operand(signed)
  ; jg  / jnle  -> left operand >   right operand
  ; jge   / jnl   -> left operand >=  right operand
  ; jl  / jnge  -> left operand <   right operand
  ; jle   / jng   -> left operand <=  right operand
  
  xor r8, r8
  mov rax, 20
  
  cmp rax, -35
  jg left_is_greater
  mov r8, 4   ; r8 = 0
  
left_is_greater:
  cmp rax, 78
  jl left_is_less
  mov r8, 5   ; r8 = 0
  
left_is_less:
  cmp rax, 20
  jge left_is_greater_or_equal
  mov r8, 12   ; r8 = 0
  
left_is_greater_or_equal:  
  xor rax, rax
  ret