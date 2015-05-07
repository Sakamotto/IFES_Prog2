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
		


def main():
	
	texto = "O Tribunal Administrativo Regional (TAR) do Lacio, na Itália, suspendeu nesta na Itália quarta-feira (06/05/2015) a extradição do ex-diretor do Banco do Brasil Henrique Pizzolato, condenado no processo do mensalão do PT. A Corte italiana agendou uma audiência para o dia 3 de junho para analisar o recurso protocolado pela defesa do ex-dirigente do banco público."
	texto2 = "Agora a NVIDIA anunciou oficialmente a sua saída do mercado de modens LTE, com o encerramento da produção da linha Icera no segundo trimestre fiscal de 2016. Nos últimos anos, o objetivo de integrar esses componentes aos processadores Tegra nunca produziu resultados satisfatórios e teve como fruto somente o malsucedido Tegra 4i. A companhia afirma estar aberta para vender sua tecnologia ou operações."
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
	
	# rotina para salvar listaEN em arquivo ... 
	
	
	#~ tokens, pos = libplnbsi.tokenizador(texto2)
	#~ padroes = ["MpM", "N/N/N", "MM","MMMM", "M", "MMM"]
	#~ 
	print(listaEN)
	nvidia.close()
	#~ 
	#~ extraidos = libplnbsi.extraiPadrao(tokens, padroes)
	#~ print(extraidos, "\n")
	#~ print(geraTabFreqEm(extraidos))
	#~ bibliaCat.close()
	
	return 0

if __name__ == '__main__':
	main()

