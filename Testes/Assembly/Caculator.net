section .data
    result db 0
    operator db 0
    num1 db 0
    num2 db 0

section .bss
    buffer resb 10

section .text
    global _start

_start:
    ; Input: Número 1
    mov eax, 3          ; sys_read
    mov ebx, 0          ; fd 0 (entrada padrão)
    mov ecx, buffer
    mov edx, 10         ; tamanho máximo do buffer
    int 0x80            ; chamada de sistema

    mov byte [num1], al ; armazena o primeiro número

    ; Input: Operador
    mov eax, 3
    mov ebx, 0
    mov ecx, buffer
    mov edx, 10
    int 0x80

    mov byte [operator], al ; armazena o operador

    ; Input: Número 2
    mov eax, 3
    mov ebx, 0
    mov ecx, buffer
    mov edx, 10
    int 0x80

    mov byte [num2], al ; armazena o segundo número

    ; Conversão ASCII para inteiro
    sub byte [num1], '0'
    sub byte [num2], '0'

    ; Realiza a operação
    mov al, [operator]
    cmp al, '+'
    je add
    cmp al, '-'
    je sub
    cmp al, '*'
    je mul
    cmp al, '/'
    je div

add:
    add byte [num1], [num2]
    jmp print_result

sub:
    sub byte [num1], [num2]
    jmp print_result

mul:
    mov al, [num1]
    mov bl, [num2]
    mul bl
    mov byte [result], al
    jmp print_result

div:
    xor edx, edx
    mov al, [num1]
    mov bl, [num2]
    div bl
    mov byte [result], al

print_result:
    ; Converte o resultado de volta para ASCII
    add byte [result], '0'

    ; Imprime o resultado
    mov eax, 4          ; sys_write
    mov ebx, 1          ; fd 1 (saída padrão)
    mov ecx, result
    mov edx, 1          ; tamanho do buffer
    int 0x80

exit:
    ; Termina o programa
    mov eax, 1          ; sys_exit
    xor ebx, ebx        ; código de saída
    int 0x80
