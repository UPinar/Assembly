%include "io64.inc"

section .data
  control dq 0    ; set this variable 0 or 1

section .text
  global CMAIN
CMAIN:
  cmp QWORD[control], 1
  je  STACK_OVERFLOW
  jmp STACK_UNDERFLOW
        
STACK_OVERFLOW:
  push rax 
  jmp STACK_OVERFLOW
    
STACK_UNDERFLOW:
  pop rax ; rsp is in the top(address)

EXIT: 
  xor rax, rax
  ret