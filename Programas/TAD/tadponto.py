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
def distancia(ponto_a, ponto_b):
	return ((ponto_b[0] - ponto_a[0])**2 + (ponto_b[1] - ponto_a[1])**2)**0.5
#



def main():
	x = float(input("X: "))
	y = float(input("Y: "))
	
	ponto = criar(x,y)
	print(ponto)
	print("Distância entre os pontos: ", distancia(ponto, (1,1)))
	
	
	ponto = destroi()
	
	return 0

if __name__ == '__main__':
	main()

