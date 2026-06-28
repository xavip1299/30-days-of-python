password = input("Digite a password: ")

def validate_password(password: str) -> dict:
    if len(password) < 10:
        return {"Password deve ter no mínimo 10 caracteres."}
    if not any(char.isupper() for char in password):
        return {"Password deve ter pelo menos uma letra maiúscula."}
    if not any(char.islower() for char in password):
        return {"Password deve ter pelo menos uma letra minúscula."}
    if not any(char.isdigit() for char in password):
        return {"Password deve ter pelo menos um número."}
    if not any(char in "!@#$%^&*()-_=+[{]}|;:',<.>/?`~" for char in password):
        return {"Password deve ter pelo menos um caractere especial."}
    if any(char.isspace() for char in password):
        return {"Password não deve conter espaços em branco."}
    if any(seq in password.lower() for seq in ["123", "abc", "password", "qwerty"]):
        return {"Password não deve conter sequências óbvias como '123', 'abc', 'password' ou 'qwerty'."}
    return {"Senha valida, pontuacao alta e poucas sugestoes"}

print(validate_password(password))