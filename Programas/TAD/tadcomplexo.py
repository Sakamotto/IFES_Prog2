#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tad_complexo.py

import math

RET = 1
POLAR = 2

def criar_ret(r,i):
	return [r,i,RET]
#

def criar_polar(r,i):
	return [r,i,POLAR]
#

def destroi():
	return None
#

#retorna o número complexo no formato polar
def get_polar(num_cx):
	if num_cx[2] == POLAR:
		return num_cx
	else:
		return [(num_cx[0]**2 - num_cx[1]**2)**0.5, math.atan(num_cx[0] / num_cx[1]), POLAR]
	#
#

#retorna o número complexo no formato retangular
def get_retangular(num_cx):
	if num_cx == RET:
		return num_cx
	else:
		return [num_cx[0]*math.cos(num_cx[1]), num_cx[1] * math.sin(num_cx[1]),RET]
	#
#

def soma(param_a, param_b):
	aux_a = get_retangular(param_a)
	aux_b = get_retangular(param_b)
	
	return [aux_a[0] + aux_b[0], aux_a[1] + aux_b[1], RET]
#

def get_real(num_cx):
	return get_retangular(num_cx)[0]
#

def get_imaginario(num_cx):
	return get_retangular(num_cx)[0]
#

def main():
	
	print(get_retangular(criar_ret(5,-3)))
	
	return 0

if __name__ == '__main__':
	main()

