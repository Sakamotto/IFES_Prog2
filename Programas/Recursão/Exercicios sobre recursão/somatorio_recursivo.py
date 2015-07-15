#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  somatorio_recursivo.py
#  
#  Copyright 2015 Cristian <cristian@cristian>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

# FUNÇÃO RECURSIVA QUE SOMA TODOS OS ELEMENTOS DE UMA LISTA
def somatorio(lista):
	if lista == []:
		return 0
	elif len(lista) == 1:
		return lista[0]
	else:
		return lista[0] + somatorio(lista[1:])
	#
#

def mdc(a, b):
	if a % b == 0:
		return b
	else:
		return mdc(b, a % b)
	#
#

def main():
	
	print(mdc(48, 30)) # CHAMADA DA FUNÇÃO QUE CALCULA O MDC DE FORMA RECURSIVA
	
	l = [1,2,3,-4]
	print(somatorio(l)) # CHAMADA DA FUNÇÃO QUE SOMA OS ELEMENTOS DE UMA LISTA DE FORMA RECURSIVA
	
	return 0

if __name__ == '__main__':
	main()

