# Dia 01 - Validador de senhas

Cria um programa que valida a forca de uma senha.

## Requisitos

- A senha deve ter pelo menos 10 caracteres.
- Deve conter letras minusculas, letras maiusculas, numeros e simbolos.
- Nao pode conter espacos.
- Nao pode conter sequencias obvias como `123`, `abc`, `password` ou `qwerty`.
- O programa deve devolver uma pontuacao de 0 a 100 e uma lista de melhorias.

## Extra

Cria uma funcao `validate_password(password: str) -> dict` e escreve 5 testes simples.

## Exemplo

Entrada: `Python123!`

Saida esperada: senha valida, pontuacao alta e poucas sugestoes.
