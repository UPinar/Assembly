%include "io64.inc"

section .data
  var_1   dq 10101010b
  var_2   dq 00001111b

section .text
  global CMAIN
    
CMAIN:
  ; or reg, imm
  mov rax, 11110001b
  or  rax, 11010001b  ; rax = 11110001b
  
  ; or reg, reg
  mov rbx, 11110000b
  mov rcx, 00001111b
  or  rcx, rbx    ; rcx = 11111111b
  
  ; or mem, imm
  or QWORD[var_1], 11110000b    ; $var_1 = 11111010b
  
  ; or reg, mem
  mov rdx, 01010101b
  or  rdx, QWORD[var_2]  ; rdx = 01011111b
  
  ; or mem, reg
  mov r8, 00011000b
  or QWORD[var_2], r8   ; $var_2 = 00011111b
      
      
  ; EXIT
  xor rax, rax
  ret