#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tadeq2g.py

def criar(a,b,c):
	return {'a': a,'b': b, 'c': c}
#

def destroi():
	return None
#

def delta(eq):
	return (eq['b']**2) - (4*eq['a']*eq['c'])
#

def getA(eq):
	return eq['a']
#

def getB(eq):
	return eq['b']
#

def getC(eq):
	return eq['c']
#
	

def raiz1(eq):
	d = delta(eq)
	if d >= 0:
		raiz1 = (-eq['b'] + (d)**0.5) / 2*eq['a']
		return raiz1
	else:
		# Calcular a raiz complexa com o tadcomplexo
		return None
	#
#

def raiz2(eq):
	d = delta(eq)
	if d >= 0:
		raiz2 = (-eq['b'] - (d)**0.5) / 2*eq['a']
		return raiz2
	else:
		# Calcular a raiz complexa com o tadcomplexo
		return None
	#
#

def main():
	
	a = 1; b = -2; c = -3
	
	equacao = criar(a,b,c)
	print(raizes(equacao))
	
	return 0

if __name__ == '__main__':
	main()

