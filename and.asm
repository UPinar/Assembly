%include "io64.inc"

section .data
  number  dq 11001000b
  var     dq 11010111b
section .text
  global CMAIN
    
CMAIN:
  ; and reg, imm
  mov rax, 10010001b  ; rax = 10010001b
  and rax, 01110011b  ; rax = 00010001b
  
  ; and reg, reg
  mov rbx, 10001110b
  mov rcx, 11111111b
  and rbx, rcx        ; rbx = 10001110b
  
  ; and mem, imm
  and QWORD[number], 0    ; $number = 0b
  
  ; and reg, mem
  and rax, QWORD[var]     ; rax = 00010001b
  
  ; and mem, reg
  and QWORD[var], rbx     ; $var = 10000110b
  
  
  ; EXIT
  xor rax, rax
  ret