
; asm_phase.asm
global _start

section .data
Team_Number dq 101  ; Team number inserted dynamically

section .text
_start:
    ; Load team number and add 1313 to create the secret value
    mov rax, [Team_Number]    ; Load team number
    add rax, 1313             ; Add 1313 to get the secret value

    ; Exit syscall
    mov rax, 60               ; syscall: exit
    xor rdi, rdi              ; exit code 0
    syscall
        