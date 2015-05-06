#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  removeAcentos.py
#  
#  Copyright 2015 Cristian <cristian@cristian>

import sys
import libplnbsi

"""
Remover acentos de um texto
Exemplo: python3 removeAcentos.py <arquivo original> <arquivo sem acentos>
"""

def main():
	
	PARAMETROS = 3
	
	copiaArquivo = ""

	if len(sys.argv) == PARAMETROS:
		arquivo = open(sys.argv[1], 'r')
		
		for texto in arquivo.readlines():
			copiaArquivo += libplnbsi.removeAcento(texto)
		#
		
		novoArquivo = open(sys.argv[2], 'w')
		novoArquivo.write(copiaArquivo)
		
		novoArquivo.close()		
		arquivo.close()
		
	else:
		print("\nA função precisa receber dois parâmetros!\n")
	#	
	
	return 0

if __name__ == '__main__':
	main()

