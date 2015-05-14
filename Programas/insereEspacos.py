"""
Insere Espaços num texto ... 
"""
import libplnbsi

def insereEspacos(pTexto):
	strSeparadores = " .,:;!?(){}[]/\\\n\t>><<"
	textoNovo = ""
	
	for elem in pTexto:
		if elem in strSeparadores:
			if elem != "":
				textoNovo += " " + elem + " "
			else:
				textoNovo += elem
			#
		else:
			textoNovo += elem
		#
	#
	return textoNovo
#


def main():
	
	texto = "Oi, eu sou Goku! 2o"
	
	print(libplnbsi.separaPal(texto))
	
	return 0

if __name__ == '__main__':
	main()

