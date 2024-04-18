%include "io64.inc"

section .data
  location dq 0

section .text
  global CMAIN
CMAIN:

  ; jmp label 
  mov rax, 5
  jmp end
  add rax, 10
  
  ; jmp reg
  mov rbx, end
  jmp rbx
   
  ; jmp mem
  mov QWORD[location], end
  jmp QWORD[location]

; end label
end:   
  xor rax, rax
  ret

  
