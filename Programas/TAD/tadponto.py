#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tadponto.py
#

# Contrutor
def criar(x, y):
	return (x,y)
#

# Destrutor
def destroi():
	return None
#

# Modificadoras


# Analisadoras	


def main():
	x = float(input("X: "))
	y = float(input("Y: "))
	
	ponto = criar(x,y)
	print(ponto)
	
	
	ponto = destroi()
	
	return 0

if __name__ == '__main__':
	main()

