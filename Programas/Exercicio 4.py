"""
Construa uma função geraTabFreq(<texto>) que recebe como entrada um texto qualquer e retorna uma tabela de 
frequência de palavras. Exemplo
------------------
Casa	|	25	 |
de		|	13	 |
o		|	150	 |
------------------
"""

def separaPal(pTexto):
	strSeparadores = ' ,.:;!?'
	strBuffer = ""
	lstPalavras = []
	
	for i in range(len(pTexto)):
		if pTexto[i] not in strSeparadores:
			strBuffer += pTexto[i]
		elif strBuffer != "":
			lstPalavras.append(strBuffer)
			strBuffer = ""
		#
	#
	if strBuffer != "":
		lstPalavras.append(strBuffer)
	#
	return lstPalavras			
#

# Retorna um dicionário com as palavras e a quantidade de vezes q ela apareceu no texto
def geraTabFreq(pTexto):
	lstPalavras = separaPal(pTexto)
	dicPalavras = {}

	for palavra in lstPalavras:
		if palavra not in dicPalavras:
			dicPalavras[palavra] = 1
		else:
			dicPalavras[palavra] += 1
		#
	#
	return dicPalavras
#

def main():
	texto = "Quando vou enxergar que é o espelho que vou enxergar?"
	result = geraTabFreq(texto) 
	for chave,valor in result.items():
		print(chave,":",valor)
	#
	print()
	
	
	return 0

if __name__ == '__main__':
	main()

