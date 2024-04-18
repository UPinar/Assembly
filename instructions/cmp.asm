%include "io64.inc"

section .text
  global CMAIN
CMAIN:
  ; CMP(Compare) instruction
  ; performs substraction like SUB, changes ZF, SF, OF, CF
  ; difference CMP and SUB: CMP is does not modify operands

  ; cmp reg, imm
  ; cmp reg, reg
  ; cmp mem, imm
  ; cmp reg, mem
  ; cmp mem, reg
  
  xor rax, rax
  ret