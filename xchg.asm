%include "io64.inc"

section .data
    var     dq  12
    m_ex1   dd  7  
    m_ex2   dd  -1

section .text
    global CMAIN
CMAIN:
    mov rbp, rsp; for correct debugging
    
    ; xchg reg, reg
    mov rax, 5          ; rax = 0x5
    mov rdx, 100        ; rdx = 0x64
    xchg rax, rdx       ; rax = 0x64, rdx = 0x5
    
    mov bx, 20          ; bx = 0x14
    mov cx, 3           ; cx = 0x3
    xchg bx, cx         ; bx = 0x3, cx = 0x14
    ; bx and cx are 2 byte registers -> bh:bl, ch:cl        
    
    
    ; xchg reg, mem
    xor rcx, rcx            ; rcx = 0x0
    mov rcx, 90             ; rcx = 0x5A
    xchg rcx, QWORD[var]    ; rcx = 0xC, QWORD[var] = 0x5A
    
    
    ; xchg reg, mem
    ; xchg mem, reg
    xor rcx, rcx            ; rcx = 0x0
    mov rcx, 90             ; rcx = 0x5A
    xchg rcx, QWORD[var]    ; rcx = 0xC, QWORD[var] = 0x5A
    xchg QWORD[var], rcx    ; QWORD[var] = 0xC, rcx = 0x5A
    
    
    ; xchg mem, mem
    ; NOT VALID, WE NEED A REGISTER TO CARRY THOSE VALUES IN VARIABLES
    ; xchg QWORD[var], QWORD[var_2] ; QWORD[var] = 0x64, QWORD[var_2] = 0xC
    
    
; ----------EXAMPLE---------- 
    ; 1. assign 7 to m_ex1 
    ; 2. assign -1 to m_ex2
    ; 3. exchange m_ex1 and m_ex2
    
    mov     DWORD[m_ex1], 7
    mov     DWORD[m_ex2], -1
    xor     rax, rax
    mov     eax, DWORD[m_ex1]       ; eax = 0x7, 
    xchg    eax, DWORD[m_ex2]       ; DWORD[m_ex2] = 0x7, eax = 0xFFFFFFFF
    mov     DWORD[m_ex1], eax       ; DWORD[m_ex1] = 0xFFFFFFFF
; ----------EXAMPLE----------   
    
    ; EXIT
    xor rax, rax
    ret