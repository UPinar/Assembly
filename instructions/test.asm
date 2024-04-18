%include "io64.inc"

section .text
  global CMAIN
CMAIN:
  ; TEST instruction : 
  ; performs AND operation in 2 operands, sets ZF and SF.
  ; Difference between TEST and AND is, 
  ; test does not modifies the destination operand
  
  mov al,  10101011b
  test al, 10001000b
  ; result : 10001000b
  ; ZF will be cleared, SF will be set
  
  ; want to check if bit 0 and 3 are both 0 
  mov bl,  10001100b
  test bl, 00001001b
  ; if result will be 00001000 so ZF will be cleared and
  ; we are now sure that bl's 0 and 3rd bits are both not 0
  
  ; TYPES
  ; test reg, imm
  ; test reg, reg
  ; test mem, imm
  ; test reg, mem
  ; test mem, reg
     
  xor rax, rax
  ret