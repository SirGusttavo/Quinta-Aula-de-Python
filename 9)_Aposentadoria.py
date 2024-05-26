idade = int(input('Digite sua idade: '))
sexo = str(input('Qual o seu sexo: '))
lower = sexo.lower ()
if idade >= 60 and lower == 'feminino':
    print('Você pode se aposentar!')
elif idade >= 65 and lower == 'masculino':
    print('Você pode se aposentar!')
else:
    print('Você ainda não pode se aposentar!')