#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  concatena.py
#  
#  Copyright 2015 Cristian <cristian@cristian>

"""
Concatenar n arquivos ... Exemplo:
python3 concatena.py <arq1> <arq2> ... <arq Concatenado>
"""

import sys

def main():
	novoTexto = ""
	
	for i in range(1, len(sys.argv) - 1):
		arquivo = open(sys.argv[i], 'r')
		for texto in arquivo.readlines():
			novoTexto += texto
		#
		print(i)
		arqConcat = open(sys.argv[len(sys.argv) - 1], 'a')
		
		arqConcat.write(novoTexto)
		novoTexto = ""
		
		arquivo.close()
		arqConcat.close()
	#
	
	return 0

if __name__ == '__main__':
	main()

