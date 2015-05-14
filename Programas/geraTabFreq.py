#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  geraTabFreq.py
#  
#  Copyright 2015 Cristian <csanterio@gmail.com>

"""
6. Construa a tabela de frequencias de palavras das bíblias católica e protestante, novo e velho testamento.
Salve as tabelas em arquivos separados. Em seguida, use a planilha eletrônica para criar um gráfico de pizza de cada tabela.
Compare os dois gráficos. (obs: não incluir stopwords na tabela de frequencia. Incluir entidades nomeadas).
"""

"""
Ideia:
Criar uma base de dados (arquivo txt) com separadores
"""

import libplnbsi

# arqEntrada: nome do arquivo para leitura
# arqSaida: nome do arquivo de saida
def geraTabFreq(arqEntrada, arqSaida):
	
	dicFrequencia = {}
	
	dados = open(arqEntrada, 'r')
	saida = open(arqSaida, 'w')
	# a variável texto, esté recebendo todo o conteúdo do arquivo, o que não é muito legal, se esse arquivo ocupar
	# muito espaço de memória ... A solução mais viável é criar um novo separaPal, e passar como parâmetro um arquivo ...
	texto = dados.read()
	b = ["MpM", "N/N/N", "MM","MMMM", "M", "MpMMpM","MMpMM", "MMM","m"]
	lista = []
	
	separadores = libplnbsi.selecionaSeparadores(texto)
	texto = libplnbsi.insereEspacos(texto)
	#print(texto)
	
	tokens, posit = libplnbsi.tokenizadorv2(texto, separadores)
	#print(tokens)
	listaPalavras = libplnbsi.extraiPadrao(tokens, b)
	
	print(listaPalavras)
	
	#~ while texto == '\n' or texto != '':
		#~ tokens, posit = libplnbsi.tokenizadorv2(texto, separadores)
		#~ 
		#~ listaPalavras = libplnbsi.extraiPadrao(tokens, b)
		#~ lista += listaPalavras
		#~ print("Lista: ", tokens)
		#~ input()
		#~ texto = dados.readline()
	#~ #
	
	for elem in listaPalavras:
		if elem not in dicFrequencia:
			dicFrequencia[elem] = 1
		elif elem in dicFrequencia:
			dicFrequencia[elem] += 1
		#
	#
	
	
	for chave, valor in dicFrequencia.items():
		#print(chave, ": ", valor)
		saida.write(str(chave) + "," + str(valor) + "\n")
	#
	
	dados.close()
	saida.close()
#

#~ def geraFreq():
	#~ 
	#~ dicFrequencia = {}
	#~ 
	#~ texto = "Converter o texto marcado para arquivo de áudio MP3, clicando em Falar >> Converter delineadas texto. O Tribunal Administrativo Regional (TAR) do Lacio, na Itália, suspendeu nesta quarta-feira 06/05/2015 a extradição do ex-diretor do Banco do Brasil Henrique Pizzolato, condenado no processo do mensalão do PT. A Corte italiana agendou uma audiência para o dia 3 de junho para analisar o recurso protocolado pela defesa do ex-dirigente do banco público."
	#~ 
	#~ 
	#~ a = libplnbsi.tokenizador(texto)[0]
	#~ 
	#~ a = libplnbsi.insereEspacos(a)
	#~ b = ["MpM", "N/N/N", "MM","MMMM", "M", "MMM", "MpMMpM","MMpMM", "m"]
	#~ 
	#~ listaPalavras = libplnbsi.extraiPadrao(a, b)
	#~ print(listaPalavras,"\n\n")
	#~ 
	#~ for elem in listaPalavras:
		#~ if elem not in dicFrequencia:
			#~ dicFrequencia[elem] = 1
		#~ elif elem in dicFrequencia:
			#~ dicFrequencia[elem] += 1
		#~ #
	#~ #
	#~ 
	#~ for chave, valor in dicFrequencia.items():
		#~ print(chave, " ", valor)
	#~ #
#~ #
	
def main():
	
	geraTabFreq('constituicaoBr.txt', 'FrequenciaDePalavras.txt')
	
	return 0

if __name__ == '__main__':
	main()

