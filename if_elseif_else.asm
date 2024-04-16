%include "io64.inc"

; if (g_a > 0) {
;    g_a *= 2
; }
; else if (g_a < 0) {
;    --g_a
; }
; else {
;    ++g_a
; }

section .data
    g_a dd

section .text
    global CMAIN
    
CMAIN:
  mov DWORD[g_a], -3  ; set different values
  cmp DWORD[g_a], 0
  jle @1
  jmp @3
@1:
  cmp DWORD[g_a], 0
  je @2
  dec DWORD[g_a]
  jmp EXIT
@2:
  inc DWORD[g_a]
  jmp EXIT
@3:
  shl DWORD[g_a], 1
  jmp EXIT

EXIT:
  xor rax, rax
  ret
    
    
