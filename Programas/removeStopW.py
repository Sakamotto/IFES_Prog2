#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  removeStopW.py
#  
#  Copyright 2015 Cristian <cristian@cristian>

"""
Construir a função removeStopW(<texto>,<lista de stopwords>). A função devolve um a texto sem stopwords.
"""
import libplnbsi

def removeStopW(pTexto, listaStopWords):
	
	resultado = []
	if type(pTexto) != "list":
		texto = libplnbsi.separaPal(pTexto)
	#
	if type(listaStopWords) != "list":
		stopWords = libplnbsi.separaPal(listaStopWords)
	#
	
	for palavra in texto:
		if palavra not in stopWords:
			resultado.append(palavra + " ")
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
	
	#~ a = "a"
	#~ print(type(a))
	
	return 0

if __name__ == '__main__':
	main()

