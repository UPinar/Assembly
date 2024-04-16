%include "io64.inc"

section .data
  var db 10101111b

section .text
  global CMAIN
CMAIN:
  ; not reg
  mov al, 11110001b   
  not al              ; al = 00001110b
  
  ; not mem
  not BYTE[var]       ; $var = 01010000b
  
  ; EXIT
  xor rax, rax
  ret

  