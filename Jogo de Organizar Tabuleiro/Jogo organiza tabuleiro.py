import random

def jogada():
	variavel=input('Digite qual posição será alterada: ')
	aux=list(variavel)
	for i in range(len(aux)):
		if ord(aux[i]) < 48 or ord(aux[i]) > 57:
			print('='*20)
			print('Digite apenas números')
			print('='*20)
			return jogada()
	for i in range(len(aux)):
		aux[i]=int(aux[i])
		
	vazio=input('Digite para onde deseja mover a posição selecionada: ')
	aux_2=list(vazio)
	for i in range(len(aux_2)):
		if ord(aux_2[i]) < 48 or ord(aux_2[i]) > 57:
			print('='*20)
			print('Digite apenas números')
			print('='*20)
			return jogada()
	for i in range(len(aux_2)):
		aux_2[i]=int(aux_2[i])
		
	return aux, aux_2
	
		
def verifica_jogada(pos1, pos2, nivel, matriz):
	if nivel == 2:
		pos1, pos2=M2x2(pos1, pos2, matriz)
	elif nivel == 3:
		pos1, pos2 = M3x3(pos1, pos2, matriz)
	return pos1, pos2

#facil
def M2x2(pos1, pos2, matriz):
	#linha 1 coluna 1
	if pos1[0] == 1:
		if pos1[1] == 1:
			if pos2[0] == 1:
				if pos2[1] != 2:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M2x2(pos1, pos2, matriz)
			elif pos2[0] == 2:
				if pos2[1] != 1:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M2x2(pos1, pos2, matriz)
			else:
				print('\nJogada inválida\n')
				pos1, pos2 = jogada()
				return M2x2(pos1, pos2, matriz)
		#linha 1 coluna 2	
		elif pos1[1] == 2:
			if pos2[0] == 1:
				 if pos2[1] != 1:
				 	print('\nJogada inválida\n')
				 	pos1, pos2 = jogada()
				 	return M2x2(pos1, pos2, matriz)
			elif pos2[0] == 2:
				if pos2[1] != 2:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M2x2(pos1, pos2, matriz)
			else:
				print('\nJogada inválida\n')
				pos1, pos2 = jogada()
				return M2x2(pos1, pos2, matriz)
		else:
			print('\nJogada inválida\n')
			pos1, pos2 = jogada()
			return M2x2(pos1, pos2, matriz)
	#linha 2 coluna 1	
	elif pos1[0] == 2:
		if pos1[1] == 1:
			if pos2[0] == 1:
				if pos2[1] != 1:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M2x2(pos1, pos2, matriz)
			elif pos2[0] == 2:
				if pos2[1] != 2:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M2x2(pos1, pos2, matriz)
			else:
				print('\nJogada inválida\n')
				pos1, pos2 = jogada()
				return M2x2(pos1, pos2, matriz)
		#linha 2 coluna 2
		elif pos1[1] == 2:
			if pos2[0] == 1:
				if pos2[1] != 2:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M2x2(pos1, pos2, matriz)
			elif pos2[0] == 2:
				if pos2[1] != 1:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M2x2(pos1, pos2, matriz)
			else:
				print('\nJogada inválida\n')
				pos1, pos2 = jogada()
				return M2x2(pos1, pos2, matriz)
	else:
		print('\nJogada inválida\n')
		pos1, pos2 = jogada()
		return M2x2(pos1, pos2, matriz)
	
	if matriz[pos2[0]-1][pos2[1]-1] != 0:
		print('\nJogada inválida\n')
		pos1, pos2 = jogada()
		return M2x2(pos1, pos2, matriz)
	return pos1, pos2

#medio
def M3x3(pos1, pos2, matriz):
	#linha 1 coluna 1
	if pos1[0] == 1:
		if pos1[1] == 1:
			if pos2[0] == 1:
				if pos2[1] != 2:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M3x3(pos1, pos2, matriz)
			elif pos2[0] == 2:
				if pos2[1] != 1:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M3x3(pos1, pos2, matriz)
			else:
				print('\nJogada inválida\n')
				pos1, pos2 = jogada()
				return M3x3(pos1, pos2, matriz)
		#linha 1 coluna 2
		elif pos1[1] == 2:
			if pos2[0] == 1:
				if pos2[1] != 1 and pos2[1] != 3:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M3x3(pos1, pos2, matriz)
			elif pos2[0] == 2:
				if pos2[1] != 2:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M3x3(pos1, pos2, matriz)
			else:
				print('\nJogada inválida\n')
				pos1, pos2 = jogada()
				return M3x3(pos1, pos2, matriz)
		#linha 1 coluna 3
		elif pos1[1] == 3:
			if pos2[0] == 1:
				if pos2[1] != 2:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M3x3(pos1, pos2, matriz)
			elif pos2[0] == 2:
				if pos2[1] != 3:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M3x3(pos1, pos2, matriz)
			else:
				print('\nJogada inválida\n')
				pos1, pos2 = jogada()
				return M3x3(pos1, pos2, matriz)
		else:
			print('\nJogada inválida\n')
			pos1, pos2 = jogada()
			return M3x3(pos1, pos2, matriz)
	#linha 2 coluna 1
	elif pos1[0] == 2:
		if pos1[1] == 1:
			if pos2[0] == 1:
				if pos2[1] != 1:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M3x3(pos1, pos2, matriz)
			elif pos2[0] == 2:
				if pos2[1] != 2:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M3x3(pos1, pos2, matriz)
			elif pos2[0] == 3:
				if pos2[1] != 1:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M3x3(pos1, pos2, matriz)
			else:
				print('\nJogada inválida\n')
				pos1, pos2 = jogada()
				return M3x3(pos1, pos2, matriz)
		#linha 2 coluna 2
		elif pos1[1] == 2:
			if pos2[0] == 1:
				if pos2[1] != 2:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M3x3(pos1, pos2, matriz)
			elif pos2[0] == 2:
				if pos2[1] != 1 and pos2[1] != 3:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M3x3(pos1, pos2, matriz)
			elif pos2[0] == 3:
				if pos2[1] != 2:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M3x3(pos1, pos2, matriz)
			else:
				print('\nJogada inválida\n')
				pos1, pos2 = jogada()
				return M3x3(pos1, pos2, matriz)
		#linha 2 coluna 3
		elif pos1[1] == 3:
			if pos2[0] == 1:
				if pos2[1] != 3:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M3x3(pos1, pos2, matriz)
			elif pos2[0] == 2:
				if pos2[1] != 2:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M3x3(pos1, pos2, matriz)
			elif pos2[0] == 3:
				if pos2[1] != 3:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M3x3(pos1, pos2, matriz)
			else:
				print('\nJogada inválida\n')
				pos1, pos2 = jogada()
				return M3x3(pos1, pos2, matriz)
		else:
			print('\nJogada inválida\n')
			pos1, pos2 = jogada()
			return M3x3(pos1, pos2, matriz)
	#linha 3 coluna 1
	elif pos1[0] == 3:
		if pos1[1] == 1:
			if pos2[0] == 2:
				if pos2[1] != 1:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M3x3(pos1, pos2, matriz)
			elif pos2[0] == 3:
				if pos2[1] != 2:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M3x3(pos1, pos2, matriz)
			else:
				print('\nJogada inválida\n')
				pos1, pos2 = jogada()
				return M3x3(pos1, pos2, matriz)
		#linha 3 coluna 2
		elif pos1[1] == 2:
			if pos2[0] == 2:
				if pos2[1] != 2:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M3x3(pos1, pos2, matriz)
			elif pos2[0] == 3:
				if pos2[1] != 1 and pos2[1] != 3:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M3x3(pos1, pos2, matriz)
			else:
				print('\nJogada inválida\n')
				pos1, pos2 = jogada()
				return M3x3(pos1, pos2, matriz)
		#linha 3 coluna 3
		elif pos1[1] == 3:
			if pos2[0] == 2:
				if pos2[1] != 3:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M3x3(pos1, pos2, matriz)
			elif pos2[0] == 3:
				if pos2[1] != 2:
					print('\nJogada inválida\n')
					pos1, pos2 = jogada()
					return M3x3(pos1, pos2, matriz)
			else:
				print('\nJogada inválida\n')
				pos1, pos2 = jogada()
				return M3x3(pos1, pos2, matriz)
		else:
			print('\nJogada inválida\n')
			pos1, pos2 = jogada()
			return M3x3(pos1, pos2, matriz)
	else:
		print('\nJogada inválida\n')
		pos1, pos2 = jogada()
		return M3x3(pos1, pos2, matriz)

	if matriz[pos2[0]-1][pos2[1]-1] != 0:
		print('\nJogada inválida\n')
		pos1, pos2 = jogada()
		return M3x3(pos1, pos2, matriz)
	
	return pos1, pos2


def geraMatriz(nivel, sequencia):
	lista=list(range(sequencia))
	matriz=[]
	for i in range(nivel):
		linha=[]
		for j in range(nivel):
			num=random.choice(lista)
			linha.append(num)
			lista.remove(num)
		matriz.append(linha)
	return matriz	


def geraMatrizCopia3(nivel):
	matriz=[]
	num=0
	for i in range(nivel):
		linha=[]
		for j in range(nivel):
			linha.append(num)
			num+=1
		matriz.append(linha)
	return matriz	

def trocaElemento(pos1, pos2, matriz):
	elemento1=matriz[pos1[0]-1][pos1[1]-1]
	elemento2=matriz[pos2[0]-1][pos2[1]-1]
	matriz[pos1[0]-1][pos1[1]-1]=elemento2
	matriz[pos2[0]-1][pos2[1]-1]=elemento1


def imprimeMatriz(matriz):
	for lista in matriz:
		aux = lista.copy()
		for linha in range(len(lista)):
				print('{}  '.format(aux[linha]), end = ' ')
		print('\n')


def main():
		sequencia=0
		pos1=[]
		pos2=[]
		nivel = int(input('Escolha o nivel do jogo,\nDIGITE (1) para Fácil\nDIGITE (2) para médio\n'))
		while nivel != 1 and nivel != 2:
			print('\nOPÇÃO INVÁLIDA\n') 
			nivel = int(input('Escolha o nivel do jogo,\nDIGITE (1) para Fácil\nDIGITE (2) para médio\n'))
		if nivel == 1:
			sequencia = 4
			nivel = 2
		else:
			sequencia = 9
			nivel = 3

		aux=[]
		matriz=geraMatriz(nivel, sequencia)
		aux=geraMatrizCopia3(nivel)
		imprimeMatriz(matriz)
		while aux != matriz:
			pos1, pos2=jogada()
			pos1, pos2=verifica_jogada(pos1, pos2, nivel, matriz)
			trocaElemento(pos1, pos2, matriz)
			imprimeMatriz(matriz)
			if aux != matriz:
				a = input('Deseja continuar?\nDigite (-1) para sair\n')
				if a == "-1":
					print('='*20)
					print('!!!FIM DE JOGO!!!')
					print('='*20)
					break
		if aux == matriz:
			print("*"*20)
			print("!!!PARABÉNS, VOCÊ VENCEU!!!")
			print("*"*20)
main()
