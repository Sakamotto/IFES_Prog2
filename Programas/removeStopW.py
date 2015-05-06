#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  removeStopW.py
#  
#  Copyright 2015 Cristian <cristian@cristian>

"""
Construir a função removeStopW(<texto>,<lista de stopwords>). A função devolve um a texto sem stopwords.
"""

def removeStopW(pTexto, listaStopWords):
	
	resultado = ""
	
	for palavra in pTexto:
		if palavra not in listaStopWords:
			resultado += palavra
			#print(resultado)
		#
	#
	return resultado
#


def main():
	
	texto = open("constituicaoBr.txt", 'r')
	stopWords = open("stopwordspt.txt", 'r')
	pTexto = texto.read()
	pStopWords = stopWords.read()

	print(removeStopW(pTexto, pStopWords))
	
	texto.close()
	stopWords.close()
	
	return 0

if __name__ == '__main__':
	main()

