import random
import string

def gerar_senha(comprimento, caracteres):
    senha = ''
    for _ in range(comprimento):
        senha += random.choice(caracteres)
    return senha

def main():
    comprimento = int(input('Informe o comprimento da senha: '))
    caracteres = ''
    while caracteres != 'sair':
        caracteres = input('Informe os caracteres que deseja usar (letras maiúsculas, letras minúsculas, números, caracteres especiais): ')
        caracteres = caracteres.lower()

        if 'letras maiúsculas' in caracteres:
            caracteres += string.ascii_uppercase
        if 'letras minúsculas' in caracteres:
            caracteres += string.ascii_lowercase
        if 'números' in caracteres:
            caracteres += string.digits
        if 'caracteres especiais' in caracteres:
            caracteres += string.punctuation

        senha = gerar_senha(comprimento, caracteres)
        print(f'Senha gerada: {senha}')

if __name__ == '__main__':
    main()