#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  copia.py
#  
#  Copyright 2015 Cristian <cristian@cristian>
#  
"""
Escreva um programa que cria uma cópia de um arquivo via CLI. Exemplo:
python3 copia.py <arquivo original> <arquivo copia>
"""

import sys

def copia(nomeArquivo, nomeNovoArquivo):
	PARAMETROS = 3
	
	copiaArquivo = ""

	if len(sys.argv) == PARAMETROS:
		arquivo = open(nomeArquivo, 'r')
		
		for texto in arquivo.readlines():
			copiaArquivo += texto
		#
		
		novoArquivo = open(nomeNovoArquivo, 'w')
		novoArquivo.write(copiaArquivo)
		
		novoArquivo.close()		
		arquivo.close()
		
	else:
		print("\nA função precisa receber dois parâmetros!\n")
	#
#

def main():
	
	copia(sys.argv[1], sys.argv[2])
	
	return 0

if __name__ == '__main__':
	main()

