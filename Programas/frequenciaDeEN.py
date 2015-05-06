"""
Criar um programa que gera a frequência de palavras (tirando as stopwords) e entidades nomeadas ...
"""

import libplnbsi


def main():
	
	texto = "O Tribunal Administrativo Regional (TAR) do Lacio, na Itália, suspendeu nesta quarta-feira (06/05/2015) a extradição do ex-diretor do Banco do Brasil Henrique Pizzolato, condenado no processo do mensalão do PT. A Corte italiana agendou uma audiência para o dia 3 de junho para analisar o recurso protocolado pela defesa do ex-dirigente do banco público."
	
	tokens, pos = libplnbsi.tokenizador(texto)
	print(libplnbsi.codifica(tokens))
	#libplnbsi.extraiPadrao()
	
	#print(tokens)
	
	return 0

if __name__ == '__main__':
	main()

