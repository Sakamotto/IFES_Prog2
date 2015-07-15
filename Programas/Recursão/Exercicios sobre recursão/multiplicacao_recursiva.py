#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  multiplicacao_recursiva.py
#  
#  Copyright 2015 Cristian <cristian@cristian>

# 3. Calcular o produto de 2 números, x e y. (pesquise o conceito de produto)

def produto(a, b):
	if b > a:
		a, b = b, a
	#
	if b == 0:
		return 0
	elif b > 0:
		return a + produto(a, b-1)
	else:
		return -produto(a, -b)
	#
#
	

def main():
	a, b = 3, -50
	print(produto(a,b))
	
	return 0

if __name__ == '__main__':
	main()

