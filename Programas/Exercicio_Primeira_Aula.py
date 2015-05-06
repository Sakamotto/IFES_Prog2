"""
Construa a função separaPal(string) que recebe como entrada um texto contendo um documento qualquer.
A função deve retornar uma lista contendo palavras presentes no texto. Uma palavra é uma sequência de 
caracteres entre caracteres chamados de separadores. São considerados separadores os seguintes caracteres:
Ponto, exclamação, interrogação, dois pontos, ponto e vírgula, vírgula e espaço
"""

def retorna_separadores(separadores):
	for i in range(len(separadores)):
		return separadores[i]
	#
#

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

def main():
	
	texto = input("Digite um texto: ")
	print(separaPal(texto))
	
	return 0

if __name__ == '__main__':
	main()

