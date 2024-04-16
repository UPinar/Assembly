%include "io64.inc"

section .text
  global CMAIN
CMAIN:
  mov rbp, rsp; for correct debugging
  mov rcx, rsp    ; rcx is holding rsp address
  mov rax, 0xDDEEAADDBBEEAAFF   
  push rax        ; we push rax(8 byte)
  ; rsp = rsp - 0x8
  mov r8d, [rcx - 4]  ; r8d = 0xddeeaadd
  mov r9d, [rcx - 8]  ; r9d = 0xbbeeaaff
  mov r10, [rcx - 8]  ; r10 = 0xddeeaaddbbeeaaff
  pop rbx             ; rbx = 0xddeeaaddbbeeaaff
  ; when we are popping, moving data into register we are using
  ; rsp = rsp + 0x8

  ; EXIT
  xor rax, rax
  ret