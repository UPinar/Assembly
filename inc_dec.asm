%include "io64.inc"

section .data
  counter db 30   ; BYTE[counter] = 0x1e

section .text
  global CMAIN
  
CMAIN:
  ;inc reg
  mov r8, 10      ; r8 = 0xa
  inc r8          ; r8 = 0xb
  mov rdx, 100    ; rdx = 0x64
  inc rdx         ; rdx = 0x65
  
  ;inc mem
  inc BYTE[counter]   ; BYTE[counter] = 0x1f
  
  ;dec reg
  dec r8          ; r8 = 0xa
  dec rdx         ; rdx = 0x64
  
  ;dec mem
  dec BYTE[counter]   ; BYTE[counter] = 0x1e
  

  ; EXIT
  xor rax, rax
  ret