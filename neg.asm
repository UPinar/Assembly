%include "io64.inc"

section .data
  num dd 100      ;$num = 0x64(100)

section .text
  global CMAIN

CMAIN:
  ; neg reg
  mov eax, -10    ; eax = 0xfffffff6
  neg eax         ; eax = 0xa
  
  mov rbx, 50     ; rbx = 0x32(50)
  mov rcx, 0      ; rcx = 0x0
  neg rbx         ; rbx = 0xffffffffffffffce(-50)
  neg rcx         ; rcx = 0x0
  
  ; neg mem
  neg DWORD[num]  ; $num = 0xffffff9c(-100)
  
  
  ; EXIT
  xor rax, rax
  ret