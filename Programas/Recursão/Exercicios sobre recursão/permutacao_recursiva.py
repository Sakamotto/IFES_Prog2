#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  permutacao_recursiva.py
#  
#  Copyright 2015 Cristian <cristian@cristian>

# 6. Pesquisar a existência do elemento e na lista L. Retorna True caso exista, False caso contrário.
def pesquisa(elem, lista):
	if lista != [] and elem == lista[0]:
		return elem == lista[0]
	elif lista == []:
		return False		
	else:
		return pesquisa(elem, lista[1:])
#

#7. Inverter uma string de entrada
def inverte_string(string):
	if string == "":
		return string
	else:
		return string[-1] + inverte_string(string[0:-1]).strip()
	#
#

# 8. Testar se um número n passado como parâmetro é um número natural. (pesquise as propriedadesde um número natural)
def eh_natural(num):
	if num < 0:
		return False
	elif num == 0:
		return True
	else:
		return eh_natural(num - 1)
	#
#

# 9. Calcular o maior valor de uma lista de números fornecida como entrada
def maior_valor(lista):
	if len(lista) == 1:
		return lista[0]
	else:
		if lista[0] > lista[len(lista) -1]:
			lista[0], lista[len(lista)-1] = lista[len(lista)-1], lista[0]
			return maior_valor(lista[1:])
		else:
			return maior_valor(lista[1:])
		#
	#
#

# 10. Calcular o menor valor de uma lista de números fornecida como entrada.

def menor_valor(lista):
	if len(lista) == 1:
		return lista[0]
	else:
		if lista[0] < lista[len(lista) -1]:
			lista[0], lista[len(lista)-1] = lista[len(lista)-1], lista[0]
			return menor_valor(lista[1:])
		else:
			return menor_valor(lista[1:])
		#
	#
#

# 11. Testar se uma string de entrada é um palíndromo. Retorna True caso seja, False caso não seja um palíndromo

def eh_palindromo(string):
	if len(string) == 1:
		return True
	elif len(string) == 2:
		return string[0] == string[1]
	#~ elif len(string) != 2 and string[0] != string[-1]:
		#~ return False
	else:
		return eh_palindromo(string[1: len(string) - 1])
	#
#

#12. É possível construir uma função recursiva para converter um valor em base dez para binário ?
# Tente construir esta função a partir do algoritmo clássico de conversão decimal binário.
''' 
10 / 2 = 5 .. 0
5 / 2 =  2 .. 1
2 / 2 = 1 .. 0
1 / 2 = 0 .. 1

'''
def dec_to_bin(num):
	if num == 1:
		return 1
	elif num == 0:
		return 0
	else:
		return int(str(dec_to_bin(num // 2)) + str(num % 2))
	#
#	

def permutacao(lista):
	if len(lista) == 1:
		return lista
	#
	prim = lista[0]
	outros = lista[1:]
	res = []
	for perm in permutacao(outros):
		print(perm)
		for i in range(len(perm) + 1):
			res += [perm[:i] + prim + perm[i:]]
			print(res)
		#
	#
	return res
#
		

def main():
	
	comb = ['a','b','c']
	num = [11,2,3,0,3,7,3,9]
	
	
	#~ print(permutacao(comb))
	
	#~ print(pesquisa('f', comb))
	#~ print(inverte_string("Oi, eu sou Goku!"))
	#~ print(inverte_string("subi no onibus"))
	#~ print(eh_natural(5))
	#~ print(maior_valor(num))
	#~ print(menor_valor(num))
	#~ print(eh_palindromo("arara"))
	print(dec_to_bin(10))
	return 0

if __name__ == '__main__':
	main()

