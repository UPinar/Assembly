%include "io64.inc"

section .data
  sum dq 20   ; $sum = 0x14

section .text
  global CMAIN
  
CMAIN:
  ; add/sub reg, imm
  mov rax, 10 ; rax = 0xa
  add rax, 5  ; rax = 0xf
  sub rax, 4  ; rax = 0xb
  
  ; add/sub reg, reg
  mov rbx, 10     ; rbx = 0xa
  mov rcx, 20     ; rcx = 0x14
  add rbx, rcx    ; rcx = 0x1e   
  sub rcx, rbx    ; rcx = 0xfffffffffffffff6(-10)
  
  ; add/sub mem, imm
  add QWORD[sum], 8   ; $sum = 0x1c
  sub QWORD[sum], 20  ; $sum = 0x8
  
  ; add/sub reg, mem
  ; add/sub mem, reg
  mov rdx, 100            ; rdx = 0x64            
  mov rcx, 5              ; rcx = 0x5 
  add rdx, QWORD[sum]     ; rdx = 0x6c
  sub QWORD[sum], rcx     ; $sub = 0x3
  
    
  ; EXIT
  xor rax, rax
  ret