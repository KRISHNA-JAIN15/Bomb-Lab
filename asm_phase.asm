global _start

section .data
Team_Number dq 101

section .text
_start:
    mov rax, [Team_Number]
    add rax, 1313

    mov rax, 60
    xor rdi, rdi
    syscall
