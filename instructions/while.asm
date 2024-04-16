%include "io64.inc"

; int g_x = 0;
; while(g_x < 5){
;   ++g_x;
;}

section .data
  g_x dd 0

section .text
  global CMAIN
CMAIN:
; WHILE LOOP
REPEAT:
  cmp DWORD[g_x], 5
  jge EXIT
  inc DWORD[g_x]
  jmp REPEAT
EXIT:  
  xor rax, rax
  ret
    
    
