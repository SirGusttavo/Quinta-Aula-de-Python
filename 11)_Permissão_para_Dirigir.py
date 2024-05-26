idade = int(input('Digite sua idade: '))
carteira = str(input('Você possui carteira da motorista? Digite sim ou não: '))
lower = carteira.lower ()
if idade >= 18 and lower == 'sim':
    print('Você pode digirir!')
else:
    print('Você não pode digirir!')