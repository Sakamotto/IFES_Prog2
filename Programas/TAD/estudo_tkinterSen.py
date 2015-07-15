#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  estudo_tkinterSen.py
#  

import math
import tkinter

def mapeiaCoord(lstpontos, janelaO, janelaD):
	lstNovasCoords = []

	lO = janelaO[2] - janelaO[0]
	aO = janelaO[3] - janelaO[1]
	lD = janelaD[2] - janelaD[0]
	aD = janelaD[3] - janelaD[1]
	
	for t in lstpontos:
		xlinha = round(janelaD[0] + (lD * t[0]) / lO)
		ylinha = round((aD // 2 + janelaD[1]) + (aD * t[1]) / aO)
		lstNovasCoords.append((xlinha, ylinha))
	#
	
	return lstNovasCoords
#


def main():
	
	raiz = tkinter.Tk()
	canvas = tkinter.Canvas(raiz, width=800, height=600, cursor="X_cursor", bg="white")
	canvas.pack()
	
	canvas.create_rectangle(50, 50, 350, 100, fill="white", outline="red")
	#~ canvas.create_rectangle(150, 150, 200, 300, fill="white", outline="red")
	
	#~ canvas.create_line((10,20), (60,70))
	
	
	lstseno = []
	angulo = 0.0
	for a in range(722):
		seno = math.sin(math.radians(angulo))
		lstseno.append((math.radians(angulo), seno))
		angulo += 0.5
	#
	
	#~ lstViewport = []
	#~ janelaD = (50, 50, 350, 100)
	#~ janelaO = (0, 1, 6.3, -1)
	
	#~ for t in lstseno:
		#~ xlinha = round(50 + ((350 - 50) * t[0]) / (2 * math.pi))
		#~ ylinha = round(75 + ((100 - 50) * t[1]) / 2)
		#~ lstViewport.append((xlinha, ylinha))
		#~ lstViewport = mapeiaCoord(lstseno,janelaO, janelaD)
	#~ #
	
	#~ lstViewport = mapeiaCoord(lstseno,janelaO, janelaD)
	#~ canvas.create_line(lstViewport)
	#~ 
	#~ janelaD = (150, 150, 200, 300)
	#~ janelaO = (0, 1, 6.3, -1)
	#~ lstViewport = mapeiaCoord(lstseno,janelaO, janelaD)
	#~ 
	#~ canvas.create_line(lstViewport)
	
	#~ lstViewport = []
	#~ 
	#~ 
	#~ for t in lstseno:
		#~ xlinha = round(150 + ((200 - 150) * t[0]) / (2 * math.pi))
		#~ ylinha = round(225 + ((300 - 150) * t[1]) / 2)
		#~ lstViewport.append((xlinha, ylinha))
	#~ #
	#~ 
	#~ canvas.create_line(lstViewport)
	
	# Criando gráfico na tela inteira
	pontoX = math.radians(35)
	pontoY = math.sin(math.radians(35))
	lstPontoAngulo = [(pontoX, pontoY)]
	
	tjanelaO = (0, 1, 6.3, -1)
	tjanelaD = (51, 51, 349, 99)
	a = mapeiaCoord(lstseno, tjanelaO, tjanelaD)
	canvas.create_line(a)
	
	lstPontoCanvas = mapeiaCoord(lstPontoAngulo, tjanelaO, tjanelaD)
	canvas.create_oval(lstPontoCanvas[0][0] -5, lstPontoCanvas[0][0] -5,lstPontoCanvas[0][1] -5,lstPontoCanvas[0][1] -5, fill="green", outline="green")
	
	tkinter.mainloop()
	
	return 0

if __name__ == '__main__':
	main()

