senha = input('Digite sua senha: ')

const_senha = 'python123'

while senha != const_senha:
    print('Senha inválida! Tente novamente.')
    senha = input('Digite sua senha: ')

print('Senha correta! Acesso permitido.')