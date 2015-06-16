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
	
	texto = dados.read()
	b = ["MpM", "N/N/N", "MM","MMMM", "M", "MpMMpM","MMpMM", "MMM","m",'V.TM',"TM","V.TMM", 'TMM', "T.M"]
	lista = []
	
	separadores = libplnbsi.selecionaSeparadores(texto)
	texto = libplnbsi.insereEspacos(texto)
	
	tokens, posit = libplnbsi.tokenizadorv2(texto, separadores)
	print(tokens)
	listaPalavras = libplnbsi.extraiPadrao(tokens, b)
	
	#~ stopW = open("stopwordspt.txt", "r")
	#~ s = stopW.read()
	#~ listaPalavras = libplnbsi.removeStopW(listaPalavras, s)
	#~ stopW.close()
	
	for elem in listaPalavras:
		if elem not in dicFrequencia:
			dicFrequencia[elem] = 1
		elif elem in dicFrequencia:
			dicFrequencia[elem] += 1
		#
	#
	
	
	for chave, valor in dicFrequencia.items():
		saida.write(str(chave) + "," + str(valor) + "\n")
	#
	
	dados.close()
	saida.close()
#
	
def main():
	
	geraTabFreq('constituicaoBr.txt', 'FrequenciaDePalavras.txt')
	
	return 0

if __name__ == '__main__':
	main()

