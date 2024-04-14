%include "io64.inc"

section .data
    books   dd 450    ; (doubleword) 4 byte
    sum     dq 30
    deneme  dq 0

section .text
    global CMAIN
CMAIN:
    mov rbp, rsp; for correct debugging
    
    ; MOV reg, imm
    MOV rax, -1     ; rax = 0xffffffffffffffff
    MOV al, 20      ; rax = 0xffffffffffffff14
    MOV rdx, 15     ; rdx = 0xf

    ; MOV reg, reg
    MOV rbx, 7      ; rbx = 0x7
    MOV rax, rbx    ; rax = 0x7
    MOV rcx, rax    ; rcx = 0x7
    
    ; MOV reg, mem
    MOV eax, DWORD[books]   ; $eax = 450 (int)
    
    ; MOV mem, reg
    MOV QWORD[sum], rax     ; $sum = 450
    
    ;MOV mem, imm
    MOV DWORD[books], 500   ; $books = 500
    
; --------NOT VALID--------
    ; MOV imm, [reg, imm, mem]
    ;   MOV 10, rax 
    
    ; MOV mem, mem
        ;MOV [deneme], [sum]
        
    ; destination and source operands must be the same size  
        ;MOV rax, r10w  
          ;-> r10w is 16 bit, rax is 64 bit
        ;MOV rax, DWORD[books] 
          ;-> rax is 64 bit, books is 32 bit
; --------NOT VALID--------
    
    
; --------TEST--------
    XOR rax, rax
    MOV rax, -1 ; 0xFFFFFFFFFFFFFFFF    ; rax = 0xFFFFFFFFFFFFFFFF
    MOV eax, 0xF1111111                 ; rax = 0xF1111111, eax = 0xF1111111
    MOV QWORD[deneme], rax              ; $deneme = 0xF1111111
    
    ; Github Copilot Answer
    ;By clearing the upper 32 bits when you write to a 32-bit register, 
    ;the CPU ensures that a negative 32-bit number stays negative when used as a 64-bit number, 
    ;and a positive 32-bit number stays positive. 
; --------TEST--------
    
    
    ; EXIT
    xor rax, rax
    ret