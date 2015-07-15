#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tadreta.py

import tadponto

# TAD RETA RETORNA UMA TUPLA COM O PONTO A E O PONTO B. LEMBRANDO QUE UM PONTO É UMA LISTA COM X E Y.

# Contrutor
def criar(ponto_a, ponto_b):
	return (ponto_a, ponto_b)
#

# Destrutor
def destroi():
	return None
#

# Modificadoras


# Analisadoras
def ehParalela(reta1, reta2):
	m1 = (reta1[1][1] - reta1[0][1]) / (reta1[1][0] - reta1[0][1])
	m2 = (reta2[1][1] - reta2[0][1]) / (reta2[1][0] - reta2[0][1])
	if m1 == m2:
		return True
	#
	return False
#

def coeficiente_angular(reta):
	return (reta[1][1] - reta[0][1]) / (reta[1][0] - reta[0][1])
#


def main():
	ptxa = float(input("X: "))
	ptya = float(input("Y: "))
	
	ptxb = float(input("X: "))
	ptyb = float(input("Y: "))
	
	ponto_a = tadponto.criar(ptxa,ptya)
	ponto_b = tadponto.criar(ptxb,ptyb)
	
	reta = criar(ponto_a, ponto_b)
	
	print("Reta: ", reta)
	reta = destroi()
	
	
	return 0

if __name__ == '__main__':
	main()

