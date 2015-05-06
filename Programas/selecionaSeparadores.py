#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  selecionaSeparadores.py
#  
#  Copyright 2015 Cristian <cristian@cristian>

"""
Construir um programa que seleciona todos os separadores de um texto entrada. Um separador é qualquer caracter que não seja
letra. O arquivo deverá ser salvo como separadores.txt
"""

import sys

def selecionaSeparadores(nomeArquivo, nomeArqSaida):
	arquivo = open(nomeArquivo,'r')
	lstSeparadores = []
	
	linha = arquivo.readline()
	while linha != '':
		for texto in linha:
			if not texto.isalpha() and not texto.isdigit():
				if texto not in lstSeparadores:
					lstSeparadores.append(texto)
				#
			#
		#
		linha = arquivo.readline()
	#
	separadores = open(nomeArqSaida, 'w')
	separadores.write(str(lstSeparadores))
	
	separadores.close()
	arquivo.close()
	return lstSeparadores
#

def main():
	
	selecionaSeparadores(sys.argv[1], sys.argv[2])
	
	return 0

if __name__ == '__main__':
	main()

