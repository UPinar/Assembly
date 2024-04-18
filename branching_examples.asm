%include "io64.inc"

section .data
  size    dd  0
  x       dd  0
  y       dd  0
  z       dd  10

section .text
  global CMAIN
CMAIN:

EXAMPLE_1:
  ; --------------------------
  ; if ( size == 0)
  ;    size = 1;
  ; --------------------------
  
  cmp DWORD[size], 0
  jnz EXAMPLE_2 ; or jne EXIT 
  mov DWORD[size], 1

EXAMPLE_2:  
  ; -------------------------- 
  ; if ( x > y )
  ;    x = 100;
  ; else
  ;   y = 200;
  ; --------------------------
  
  ; x and y are signed integers
  
  mov DWORD[x], 10
  mov DWORD[y], 5
  
  mov eax, DWORD[x]
  cmp eax, DWORD[y]
  jle ELSE
  mov DWORD[x], 100
  jmp EXAMPLE_3
    
ELSE: 
  mov DWORD[y], 200 
    
EXAMPLE_3:
  ; --------------------------
  ; if ( x > y and y > z)
  ;   x = 100;
  ; --------------------------
  
  mov DWORD[x], 80
  mov DWORD[y], 50
  mov DWORD[z], -30

; CONDITION_1
  mov eax, DWORD[x]
  cmp eax, DWORD[y]
  jle EXAMPLE_4

; CONDITION_2
  mov eax, DWORD[y]
  cmp eax, DWORD[z]
  jle EXAMPLE_4
  mov DWORD[x], 100

EXAMPLE_4:
  ; --------------------------
  ; while ( x <= y)
  ;   ++x;
  ; --------------------------
  
  mov DWORD[x], 95
  mov DWORD[y], 100

  mov eax, DWORD[y]
WHILE:    
  cmp DWORD[x], eax
  jg  EXAMPLE_5
  
  inc DWORD[x]
  jmp WHILE
    
    
EXAMPLE_5:  
  ; --------------------------
  ; do
  ;   ++x;
  ; while ( x <= y);
  ; --------------------------  
  ; better using `cmp reg, reg` instead of 
  ; `cmp reg, mem` or `cmp mem, reg` 
  ; accessing registers are much more faster than 
  ; accessing memory
  
  mov DWORD[x], -2
  mov DWORD[y], 5


  mov eax, DWORD[x]
  mov ebx, DWORD[y]
DO_WHILE:    
  inc eax
  cmp eax, ebx    
  jle DO_WHILE

  mov DWORD[x], eax 
    
EXIT:
  xor rax, rax
  ret