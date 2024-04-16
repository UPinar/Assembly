%include "io64.inc"

section .data
  bin dq  11110101b
  var dq  10110111b

section .text
  global CMAIN
CMAIN:
  ; xor reg, imm
  mov rax, 10110101b
  xor rax, 10010101b  ; rax = 00100000b
  
  ; xor reg, reg
  mov rbx, 10001000b
  mov rcx, 11111111b
  xor rbx, rcx        ; rbx = 01110111b
  
  ; xor mem, imm
  xor QWORD[bin], 0   ; $bin = 11110101b
  ; xor'ing with 0  did not change the value itself 
  
  ; xor reg, mem
  xor rbx, QWORD[var] ; rbx = 11000000b
  ; xor mem, reg
  xor QWORD[var], rax ; $var = 10010111b
  
  ; EXIT
  xor rax, rax
  ret