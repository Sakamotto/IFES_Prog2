#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  divisao_recursiva.py
#  
#  Copyright 2015 Cristian <cristian@cristian>

def divisao(a, b):
	if a < b:
		return 0
	elif b > 0:
		return 1 + divisao(a - b, b)
	else:
		return -divisao(a, -b)
	#	
#

def main():
	
	a, b = 100, -2
	
	print(divisao(a, b))
	
	return 0

if __name__ == '__main__':
	main()

