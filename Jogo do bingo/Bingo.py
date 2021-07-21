'''
Coluna B -> 1 a 15
Coluna I -> 16 a 30
Coluna N -> 31 a 45
Coluna G -> 46 a 60
Coluna O -> 61 a 75
'''
import random

def gerabingo():
	lista1, lista2, lista3, lista4, lista5=[],[],[],[],[]
	copianum1a75_1 = []
	copianum1a75=list(range(1, 76))
	#aqui gera a tabela completa
	num1a75 = list(range(1, 76))
	for i in range(len(num1a75)):
		if num1a75[i]<=15:
			copianum1a75[i] = 'B ' + str(num1a75[i])
			lista1.append('B ' + str(num1a75[i]))
			if len(lista1)==15:
				copianum1a75_1.append(lista1)
		elif num1a75[i]<=30:
			copianum1a75[i] = 'I ' + str(num1a75[i])
			lista2.append('I ' + str(num1a75[i]))
			if len(lista2)==15:
				copianum1a75_1.append(lista2)
		elif num1a75[i]<=45:
			copianum1a75[i] = 'N ' + str(num1a75[i])
			lista3.append('N ' + str(num1a75[i]))
			if len(lista3)==15:
				copianum1a75_1.append(lista3)
		elif num1a75[i]<=60:
			copianum1a75[i] = 'G ' + str(num1a75[i])
			lista4.append('G ' + str(num1a75[i]))
			if len(lista4)==15:
				copianum1a75_1.append(lista4)
		else:
			copianum1a75[i] = 'O ' + str(num1a75[i])
			lista5.append('O ' + str(num1a75[i]))
			if len(lista5)==15:
				copianum1a75_1.append(lista5)
	return copianum1a75, copianum1a75_1

def geracartela(tabelalistada):
		bingo = tabelalistada.copy()
		cartela=[]
		aux=[]
		for i in bingo:
			aux=i.copy()
			if len(cartela)<5:
				for j in range(5):
					num=random.choice(aux)
					cartela.append(num)
					aux.remove(num)
			elif len(cartela)<10:
				for j in range(5):
					num=random.choice(aux)
					cartela.append(num)
					aux.remove(num)
			elif len(cartela)<15:
				for j in range(5):
					num=random.choice(aux)
					cartela.append(num)
					aux.remove(num)
			elif len(cartela)<20:
				for j in range(5):
					num=random.choice(aux)
					cartela.append(num)
					aux.remove(num)
			elif len(cartela)<25:
				for j in range(5):
					num=random.choice(aux)
					cartela.append(num)
					aux.remove(num)
		return cartela

def sorteio(tabelacompleta):
	tabelacopy=tabelacompleta.copy()
	numsorteados=[]
	boleano=True
	while len(tabelacopy)>0 and boleano:
		num = random.choice(tabelacopy)
		print("BOLA... NÚMERO...")
		print("="*10)
		print(num)
		print('='*10)
		numsorteados.append(num)
		tabelacopy.remove(num)
		while True:
			print('Digite o numero da opção desejada a baixo, ou precione apenas ENTER para continuar:')
			print('1 - Números sorteados    2 - Encerrar o jogo')
			num=input()
			print()
			if num == '1':
				print("*"*10)
				print('Numeros sorteados')
				for i in range (len(numsorteados)):
					print('{}'.format(numsorteados[i]), end=', ')
				print()
				print("*"*10)
				num = input('Digite qualquer tecla pra continuar\n')
				break
			elif num == '2':
				print('Se você sair do jogo agora, perderá todo o seu progresso')
				print('Deseja realmente sair?')
				num=input("S/N\n")
				while num != 's' and num != 'S' and num != 'n' and num != 'N':
					print('Opção inválida')
					print('Deseja realmente sair?')
					num=input("S/N\n")
				if num == 's' or num == "S":
					boleano = False
					break
				else:
					break
			else:
				break
	return numsorteados, tabelacopy
			
	
				
def main():
	 tabelacompleta, tabelalistada, cartela, numsorteados=[],[],[],[]
	 aux=[]
	 num=''
	 tabelacompleta, tabelalistada=gerabingo()
	 boleano = True
	 while boleano:
	 	numint=0
	 	print('Digite o numero da opção desejada:')
	 	print('1 - Gerar cartelas para bingar\t 2 - Iniciar Jogo')
	 	num=input()
	 	print()
	 	if num == '1':
	 		cartela=geracartela(tabelalistada)
	 		for i in range(5):
	 			for j in range(5):
	 				print('{}'.format(cartela[numint]), end= " . ")
	 				numint+=1
	 			print()
	 	elif num == "2":
	 		numsorteados, aux = sorteio(tabelacompleta)
	 		print("NUMEROS RESTANTES")
	 		print(aux)
	 		print('\n\n')
	 		print("NUMEROS SORTEADOS")
	 		print(numsorteados)
	 		print('Deseja jogar novamente?')
	 		num=input("s/n\n")
	 		while num != 's' and num != 'S' and num != 'n' and num != 'N':
	 			print('Opção inválida')
	 			print('Deseja jogar novamente?')
	 			num=input("s/n\n")
	 		if num == 's' or num == "S":
	 			continue
	 		else:
	 			boleano=False
	 	else:
	 		print('Opção inválida\n')
main()
