"""
Construa a função intersec(<texto>, <texto>) que retorna uma lista com o conjunto intersecção das palavras
que acorrem em <texto1> e <texto2>

Construa a função uniao(<texto>, <texto>) que retorna uma lista com o conjunto união das palavras
que acorrem em <texto1> e <texto2>
"""

def separaPal(pTexto):
	strSeparadores = ' ,.:;!?'
	strBuffer = ""
	lstPalavras = []
	
	for i in range(len(pTexto)):
		if pTexto[i] not in strSeparadores:
			strBuffer += pTexto[i]
		elif strBuffer != "":
			lstPalavras.append(strBuffer)
			strBuffer = ""
		#
	#
	if strBuffer != "":
		lstPalavras.append(strBuffer)
	#
	return lstPalavras			
#

def intersec(pTexto1, pTexto2):
	lstTexto1 = separaPal(pTexto1)
	lstTexto2 = separaPal(pTexto2)
	inter = []
	
	for texto1 in lstTexto1:
		for texto2 in lstTexto2:
			if texto1 == texto2:
				if texto1 not in inter:
					inter.append(texto1)
				#
			#
		#
	#
	return inter
#

def uniao(pTexto1, pTexto2):
	lstTexto1 = separaPal(pTexto1)
	lstTexto2 = separaPal(pTexto2)
	u = []
	
	for texto1 in lstTexto1:
		if texto1 not in u:
			u.append(texto1)
		#
	#
	
	for texto2 in lstTexto2:
		if texto2 not in u:
			u.append(texto2)
		#
	#
	
	return u
#	

def main():
	texto1 = "Oi, eu sou Goku e Gohan"
	texto2 = "Mentira, eu sou Gohan!"
	print(intersec(texto1, texto2))
	print(uniao(texto1, texto2))
	
	return 0

if __name__ == '__main__':
	main()

