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
	# a variável texto, esté recevendo todo o conteúdo do arquivo, o que não é muito legal, se esse arquivo ocupar
	# muito espaço de memória ... A solução mais viável é criar um novo separaPal, e passar como parâmetro um arquivo ...
	texto = dados.read()
	
	separadoresDoContexto = libplnbsi.selecionaSeparadores(arqEntrada)
	listaPalavras = libplnbsi.separaPalComParametro(texto, separadoresDoContexto)
	
	for elem in listaPalavras:
		if elem.lower() not in dicFrequencia:
			dicFrequencia[elem.lower()] = 1
		elif elem.lower() in dicFrequencia:
			dicFrequencia[elem.lower()] += 1
		#
	#
	
	for chave, valor in dicFrequencia.items():
		saida.write(str(chave) + "," + str(valor) + "\n")
	#
	
	dados.close()
	saida.close()
#

def main():
	
	geraTabFreq('constituicaoBr.txt','FrequenciaDePalavras.txt')
	
	return 0

if __name__ == '__main__':
	main()

