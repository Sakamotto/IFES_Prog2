#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  estudo_tkinter.py

import tkinter
import time

def main():
	
	raiz = tkinter.Tk()
	canvas = tkinter.Canvas(raiz, width=600, height=400, cursor="X_cursor", bg="black")
	canvas.pack()
	
	bx1 = 50
	by1 = 25
	bx2 = bx1 + 10
	by2 = by1 + 10
	
	
	for i in range(0, 400, 10):		
		canvas.create_rectangle(bx1 + i, by1 + i, bx2 + i, by2 + i, fill="blue", outline="white")
		canvas.update()
		time.sleep(0.10)
		canvas.create_rectangle(bx1 + i, by1 + i, bx2 + i, by2 + i, fill="white", outline="white")
		canvas.update()
	#
	
	tkinter.mainloop()
	
	return 0

if __name__ == '__main__':
	main()

