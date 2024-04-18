%include "io64.inc"

section .text
  global CMAIN
CMAIN:
  mov rbp, rsp; for correct debugging
  ; conditional branching
  
  ; jz    : jump if ZF is set
  ; jnz   
  ; jc    : jump if CF is set
  ; jnc   
  ; jo    : jump if OF is set
  ; jno   
  ; js    : jump is SF is set
  ; jns
  
  xor r8, r8
  xor r9, r9
  
  mov cl, -100
  sub cl, 100         ; OF will be set
  jo overflow_flag_set
  mov r8,10           ; r8 = 0
     
overflow_flag_set: 
  mov dl, 0
  or  dl, 10000000b   ; SF will be set
  js  signed_flag_set
  mov r9, 10          ; r9 = 0

signed_flag_set:
  xor rax, rax
  ret