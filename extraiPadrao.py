"""
essa função vai receber dois parametros: Lista de tokens e lista de padrões e vai devolver as palavras do texto 
que são de acordo com o padrão, ex: MpM vai devolver Banco do Brasil caso tenha no texto. 
E a lista de padrões vc que determina quais são. Ex: MpM, MM, etc
"""
import libProg2

def extraiPadrao(lstTokens, lstPadroes):
	tokensCodificados = libProg2.codifica(lstTokens[0])
	
	for i in range(len(lstPadroes)):
		nGrama = libProg2.nGrama(tokensCodificados, len(lstPadroes[i]))
		for ngrama in nGrama:
			if ngrama == lstPadroes[i]:
				print("Achei igual o/")
			#
		#
	#
#

def main():
	
	padroes = ["MpM", "NmNmN"]
	tokens, pos = libProg2.tokenizador("Banco do Brasil, no dia 15/09/2013 faliu!")
	print(extraiPadrao((tokens, pos), padroes))
	
	return 0

if __name__ == '__main__':
	main()

