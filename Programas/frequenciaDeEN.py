"""
Criar um programa que gera a frequência de palavras (tirando as stopwords) e entidades nomeadas ...
"""

import libplnbsi

def geraTabFreqEm(entidades):
	dicFrequencia = {}
	for elem in entidades:
		if elem not in dicFrequencia:
			dicFrequencia[elem] = 1
		else:
			dicFrequencia[elem] += 1
		#
	#
	
	return dicFrequencia
#

def salvar(pListaParam, pNomeArq):
	arquivo = open(pNomeArq, 'w')
	
	for elem in pListaParam:
		arquivo.write(elem + "\n")
	#
	
	arquivo.close()	
#

def salvarDic(pDicParam, pNomeArq):
	arquivo = open(pNomeArq, 'w')
	
	for elem,valor in pDicParam.items():
		arquivo.write(str(elem) + ', ' + str(valor) + "\n")
	#
	
	arquivo.close()	
#

def main():
	
	nvidia = open('nvidia.txt', 'r')
	linha = nvidia.readline()
	listaEN = []
	padroes = ["MpM", "N/N/N", "MM","MMMM", "M", "MMM"]
	
	while linha != "":
		linha = linha.strip()
		tokens, pos = libplnbsi.tokenizador(linha)
		extraidos = libplnbsi.extraiPadrao(tokens, padroes)
		listaEN += extraidos
		
		linha = nvidia.readline()
	#
	print(listaEN)
	# rotina para salvar listaEN em arquivo ...
	
	salvar(listaEN, 'PadroesEM.txt')
	salvarDic(geraTabFreqEm(listaEN), 'frequenciasEM.txt')
	
	
	#~ tokens, pos = libplnbsi.tokenizador(texto2)
	#~ padroes = ["MpM", "N/N/N", "MM","MMMM", "M", "MMM"]
	#~ 
	#print(listaEN)
	nvidia.close()
	#~ 
	#~ extraidos = libplnbsi.extraiPadrao(tokens, padroes)
	#~ print(extraidos, "\n")
	#~ print(geraTabFreqEm(extraidos))
	#~ bibliaCat.close()
	
	return 0

if __name__ == '__main__':
	main()

