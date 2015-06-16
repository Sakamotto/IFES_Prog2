"""
essa função vai receber dois parametros: Lista de tokens e lista de padrões e vai devolver as palavras do texto 
que são de acordo com o padrão, ex: MpM vai devolver Banco do Brasil caso tenha no texto. 
E a lista de padrões vc que determina quais são. Ex: MpM, MM, etc
"""
import libplnbsi

def ordenaVetPorTamanho(lista):
	trocas = False
	
	while not trocas:
		trocas = True
		for i in range(len(lista) - 1):
			if len(lista[i]) < len(lista[i + 1]):
				aux = lista[i]
				lista[i] = lista[i+1]
				lista[i+1] = aux
				trocas = False
			#
		#
	#
#
	

def extraiPadrao(lstTokens, lstPadroes):
	tokensCodificados = libplnbsi.codifica(lstTokens)
	newArray = []
	newStr = tokensCodificados
	strPalavra = ""
	ordenaVetPorTamanho(lstPadroes)
	#print(lstTokens, "\n")
	
	for i in range(len(lstPadroes)):
		pos = newStr.find(lstPadroes[i])
		while pos != -1:
			newStr = newStr.replace(lstPadroes[i], "*" * len(lstPadroes[i]), 1)
			for j in range(pos, pos + len(lstPadroes[i])):
				print(lstTokens[j])
				if lstTokens[j].isalpha():
					strPalavra = strPalavra + lstTokens[j] + " "
				else:
					strPalavra = strPalavra + lstTokens[j]
				#
			#
			newArray.append(strPalavra)
			strPalavra = ""
			pos = newStr.find(lstPadroes[i])
		#
	#
		
	return newArray
#

def main():
	
	padroes = ["MpM", "N/N/N", "MM","MMMM", "M", "MpMMpM","MMpMM", "MMpM","MMM","m"]
	texto = "Converter o texto marcado para arquivo de áudio, clicando em Falar >> Converter delineadas texto. O Tribunal Administrativo Regional >> (TAR) do - Lacio, na Itália, suspendeu nesta > quarta-feira (06/05/2015) a extradição do ex-diretor do Banco do Brasil Henrique Pizzolato, condenado no processo do mensalão do PT. A Corte italiana agendou uma audiência para o dia 3 de junho para analisar o recurso protocolado pela defesa do ex-dirigente do banco público. A República Federativa do Brasil, formada pela união indissolúvel dos Estados e Municípios e do Distrito Federal, constitui-se em Estado democrático"
	tokens, pos = libplnbsi.tokenizador(texto)
	print(tokens)
	print("Texto a ser extraido: \n")
	print(texto, "\n")
	#print(libplnbsi.codifica(tokens))
	print(extraiPadrao(tokens, padroes))
	
	return 0

if __name__ == '__main__':
	main()

