"""
Dada uma entrada, faça a função ehRomano(<texto>) que verifica se a string passada é um número romano
"""
import libProg2
# Em números romanos, um algarismo não pode se repetir mais q três vezes ...
def ehRomano(pTexto):
	strNum = "IVXLCDM"
	
	for alg in pTexto:
		if alg not in strNum:
			return False
		#
	#
	return True
#

def main():
	
	
	num = input("Digite um texto: ")
	s = libProg2.insereEspacos(num)
	print(libProg2.tokenizador(num))
	print(s)
	print(s.split())
	
	return 0

if __name__ == '__main__':
	main()

