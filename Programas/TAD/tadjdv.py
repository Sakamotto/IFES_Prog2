#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tadjdv.py
#

JOGADOR_A = 1
JOGADOR_B = 4
VAZIO = 0
VELHA = 999
EM_ANDAMENTO = 10

# ++++++++++++++++++++++++++++ Construtor ++++++++++++++++++++++++++++ 
def criar():
	return [[VAZIO for i in range(3)] for k in range(3)]
#


# ++++++++++++++++++++++++++++ Destrutor  ++++++++++++++++++++++++++++ 
def destroi():
	return None
#


# ++++++++++++++++++++++++++++ Modificadores ++++++++++++++++++++++++++++
def jogar(param_tadjdv, pos, simbolo):
	param_tadjdv[(pos - 1)//3][(pos - 1) % 3] = simbolo
	print(param_tadjdv)
#

# ++++++++++++++++++++++++++++ Analisadores ++++++++++++++++++++++++++++
def qualJogada(param_tadjdv, pos):
	return param_tadjdv[(pos - 1)//3][(pos - 1) % 3]
#

def status(param_tadjdv):
	lst_soma = [0] * 8
	linha = 0; coluna = 3; diagp = 6; diagsec = 7
	
	for i in range(3):
		for k in range(3):
			lst_soma[linha] += param_tadjdv[i][k]
			lst_soma[coluna] += param_tadjdv[k][i]
			
			if i == k:
				lst_soma[diagp] += param_tadjdv[i][k]
			elif i == (2 - k):
				lst_soma[diagsec] += param_tadjdv[i][k]
			#
		#
		linha += 1
		coluna += 1
	#
	
	lst_aux = [0,1,2,4,5,8]
	
	if 3 in lst_soma:
		return JOGADOR_A
	elif 12 in lst_soma:
		return JOGADOR_B
	else:
		for elem in lst_aux:
			if elem in lst_soma:
				return EM_ANDAMENTO
			#
			print("Passei Aqui!!")
			return VELHA
		#
	#
#
	


def main():
	
	jogo = criar()
	jog_a = input("Digite seu nome: ")	
	
	jog_b = input("Digite seu nome: ")
	
	
	st = status(jogo)
	while st == EM_ANDAMENTO:
		pos_a = int(input(jog_a+ " digite a posição (1-9): "))
		jogar(jogo, pos_a, JOGADOR_A)
		pos_b = int(input(jog_b + " digite a posição (1-9): "))
		jogar(jogo, pos_b, JOGADOR_B)
		st = status(jogo)
		print(st)
	#
	
	jogo = destroi()
	
	
	return 0

if __name__ == '__main__':
	main()

