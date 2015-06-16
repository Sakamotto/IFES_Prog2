"""
A) A dezena mais frequente
B) A dezena menos frequente
C) Tabela de frequencias de dezenas
D) Tabela de frequencias de duplas dezenas
E) Tabela de frequencias de triplas dezenas
"""

import libplnbsi
from operator import itemgetter

def combina(listaDezenas, qtd, dicDezenas):
	
	i = 0; j = 0
	
	while i < len(listaDezenas):
		j = i + 1
		while j < len(listaDezenas):
			tpDezenas = int(listaDezenas[i]), int(listaDezenas[j])
			tpDezenas = tuple(sorted(tpDezenas))
			if tpDezenas not in dicDezenas:
				dicDezenas[tpDezenas] = 1
			else:
				dicDezenas[tpDezenas] += 1
			#
			j += 1
		#
		i += 1
	#
	return dicDezenas
#

def gravaCombinacoes(lista):
	arquivo = open('arqDuplaSena.txt', 'w')
	for elem in lista:
		arquivo.write(str(elem[0]) + ", " + str(elem[1]) + "\n" )
	#
	arquivo.close()
#

def frequenciaDeDezena(nomeArq):
	
	dicFreq = {}
	dicMais = {}
	
	arq = open(nomeArq, "r")
	resp = open('respostaABC.txt', 'w')
	
	linha = arq.readline()
	dezenas = libplnbsi.tokenizador(linha.strip())[0]
	while linha != "":
		for elem in dezenas:
			if elem not in dicFreq:
				dicFreq[elem] = 1
			else:
				dicFreq[elem] += 1
			#
		#
		
		linha = arq.readline()
		dezenas = libplnbsi.tokenizador(linha.strip())[0]
	#
	
	a = list(dicFreq.values())
	a.sort()
	
	for chave, valor in dicFreq.items():
		if valor == a[len(a) - 1]:
			resp.write("Dezena mais frequente: "+str(chave) + ": " +str(valor) + "\n")
			dicMais[chave] = valor
		#
		
		if valor == a[0]:
			resp.write("Dezena menos frequente: "+str(chave) + ": " +str(valor) + "\n")
			dicMais[chave] = valor
		#
	#
	
	
	for chave, valor in dicFreq.items():		
		resp.write(str(chave) + ": " + str(valor) + "\n")
	#
	
	arq.close()
	resp.close()
#

def main():
	
	dicDezenas = {}
	
	frequenciaDeDezena("megasena.txt")
	
	arqDezenas = open("megasena.txt", "r")
	linha = arqDezenas.readline()
	
	while linha != "":
		dados = libplnbsi.tokenizador(linha.strip())[0]
		combina(dados, 2, dicDezenas)
		
		linha = arqDezenas.readline()
	#
	arqDezenas.close()
	listaDezenas = sorted(dicDezenas.items(), key=itemgetter(1), reverse=True)
	gravaCombinacoes(listaDezenas)
	
	return 0
#

if __name__ == '__main__':
	main()

