from random import randint
import emoji

sorteio = randint(1,100)
cont_jog=1
max_jog=6

def escolha():
	entrada = list(input('\033[0;36mChute um número entre 1 e 100: \033[m'))
	for i in entrada:
		if ord(i) < 48 or ord(i) > 57:
			print('Digite apenas números')
			return escolha()
	converte=''.join(entrada)
	num=int(converte)
	if num > 100 or num < 1:
		return escolha()
	return num

def verifica(num):
	global sorteio, cont_jog, max_jog
	while True:
		if cont_jog>=max_jog:
			if num != sorteio:
				print('jogada {}/{}\n'.format(cont_jog, max_jog))
				print('Fim das jogadas')
				print(emoji.emojize('Você perdeu:disappointed_relieved:', use_aliases=True))
				print('Número sorteado {}'.format(sorteio))
				break
			else:
				print(emoji.emojize(':tada:\033[34m!!!Você venceu, parabéns!!!\033[m:tada:', use_aliases=True))
				print('\033[34mVocê jogou {} vezes\033[m'.format(cont_jog))
				break
		elif num < sorteio:
			cont_jog+=1
			print('jogada {}/{}'.format(cont_jog-1, max_jog))
			print('\033[0;31m!!!Chute mais alto!!!\033[m')
			num=escolha()
			return verifica(num)
		elif num > sorteio:
			cont_jog+=1
			print('jogada {}/{}'.format(cont_jog-1, max_jog))
			print('\033[31m!!!Chute mais baixo!!!\033[m')
			num=escolha()
			return verifica(num)
		else:
			cont_jog+=1
			print(emoji.emojize(':tada:\033[34m!!!Você venceu, parabéns!!!\033[m:tada:', use_aliases=True))
			print('\033[34mVocê jogou {} vezes\033[m'.format(cont_jog -1))
			break

def main():
	global sorteio, cont_jog
	num=escolha()
	verifica(num)
	print('\nDeseja jogar novamente?')
	var=input('Digite (-1) para jogar novamente\nDigite qualquer tecla para encerrar\n')
	if var == "-1":
		sorteio = randint(1,100)
		cont_jog=1
		main()
	else:
		print()
		print('Jogo finalizado...')
main()
