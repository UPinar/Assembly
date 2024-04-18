%include "io64.inc"

section .text
  global CMAIN
CMAIN:
  ; ABOVE, BELOW  -> CMP left operand, right operand(unsigned)
  ; ja    / jnbe      -> left operand >   right operand
  ; jae   / jnb       -> left operand >=  right operand
  ; jb    / jnae      -> left operand <   right operand
  ; jbe   / jna       -> left operand <=  right operand
      
  xor r8, r8
  mov rax, 5
  
  cmp rax, 1
  ja left_is_above        ; left > right
  mov r8, 10  ; r8 = 0
    
left_is_above:
  cmp rax, 11
  jb left_is_below        ; left < right
  mov r8, 12  ; r8 = 0
    
left_is_below:
  cmp rax, 5
  jae left_above_or_equal ; left >= right
  mov r8, 13  ; r8 = 0

left_above_or_equal:
  cmp rax, 5
  jbe left_below_or_equal  ; left <= right 
  mov r8, 7    ; r8 = 0
  
left_below_or_equal: 
  xor rax, rax
  ret