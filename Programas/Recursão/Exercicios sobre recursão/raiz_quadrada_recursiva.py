#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  raiz_quadrada_recursiva.py
#  
#  Copyright 2015 Cristian <cristian@cristian>
#  

"""
4. Calcular a raiz quadrada de um número n com tolerância máxima t. (pesquise a definição de raiz
quadrada)
"""

def raiz(n, t):
	if abs(n**2 - t) <= 0.0001:
		return n
	else:
		a0 = n / 2
		t = n / a0 # 4 / 2 = 2
		an = (a0 + t) / 2 # (1 + 2) / 2 = 1.5  ]
		#~ print(raiz(n / a2, t))
		#~ print(raiz(n / a2, a2))
		#~ input()
		return raiz(n / an, an)
	#
#

# Referência do método:
"""
https://books.google.com.br/books?id=I-5hAAAAcAAJ&pg=PR12&dq=easy+square+roots+children&hl=en&sa=X&ei=XgFjVcX8PMLKsAWo1ICQDA&redir_esc=y#v=onepage&q&f=false

"""
def raiz_francois(n, t):
	res = t + (n - t**2) / (2*t)
	rp = res**2
	if abs(rp - n) <= 0.000001 or t == res:
		return res
	else:
		t = res
		return raiz_francois(n, t)
	#
#


def main():
	
	print(raiz_francois(2, 1))
	
	return 0

if __name__ == '__main__':
	main()

