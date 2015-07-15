

import tkinter
import tadretangulo
import time

def movimentar(retangulo, cv, dx, dy, cor):
	cv.create_rectangle(retangulo, fill= cor,outline="black")
	
	tadretangulo.move(retangulo, dx, dy)
	#~ cv.update()
	cv.create_rectangle(retangulo, fill=cor,outline="black")
	
	cv.update()
	
	#~ return None
#
	

def main():
	w = 800
	h = 600
	dx = 10; da = 25
	dy = 10; db = 25
	x1, y1, x2, y2 = 10, 10, 100, 100
	xa, ya, xb, yb = 500, 100, 700, 300
	
	retangulo1 = tadretangulo.criarVtx(x1, y1, x2, y2)
	retangulo2 = tadretangulo.criarVtx(xa, ya, xb, yb)
	
	raiz = tkinter.Tk()
	canvas = tkinter.Canvas(raiz, width = w, height = h, cursor="X_cursor", bg="white")
	canvas.pack()
	
	while True:		
		movimentar(retangulo1, canvas, dx, dy, "")
		movimentar(retangulo2, canvas, da, db, "")
		
		inte1 = tadretangulo.intersec(retangulo1, retangulo2)
		inte2 = tadretangulo.intersec(retangulo2, retangulo1)
		
		if inte1 != None:
			canvas.create_rectangle(inte1[0], inte1[3], fill="black", outline="black")
			canvas.update()
		elif inte2 != None:
			canvas.create_rectangle(inte1[0], inte1[3], fill="black", outline="black")
			canvas.update()
		#
		
		canvas.update()
		
		time.sleep(0.10)
		
		if retangulo2[3][1] >= h - 3:
			db *= -1
		if retangulo2[3][0] >= w - 3:
			da *= -1
		if retangulo2[0][1] == 0:
			db *= -1
		if retangulo2[0][0] == 0:
			da *= -1
		#
		
		if retangulo1[3][1] >= h - 3:
			dy *= -1
		if retangulo1[3][0] >= w - 3:
			dx *= -1
		if retangulo1[0][1] == 0:
			dy *= -1
		if retangulo1[0][0] == 0:
			dx *= -1
		#
		canvas.delete("all")
	#
	
	raiz.mainloop()
	
	
	return 0

if __name__ == '__main__':
	main()

