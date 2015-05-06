"""
Criar a função justificar(<texto>, <largura>, <altura>)
"""

def justificar(pTexto, pLargura, pAltura):
	print("-- " * pLargura)
	print("|\n" * pAltura)
#

def main():
	
	texto = ""
	largura = 20
	altura = 10
	justificar(texto, largura, altura)
	
	return 0

if __name__ == '__main__':
	main()

