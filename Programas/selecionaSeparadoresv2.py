"""

"""

import libplnbsi

# Dado um arquivo de texto, esta função escreve em um arquivo todos os separadores ... 
def selecionaSeparadores(pTexto):
	arquivo = open("separadores.txt",'w')
	strSeparadores = ""
	strSeparadores2 = ""

	for texto in pTexto:
		if not texto.isalnum() and texto not in strSeparadores:
			strSeparadores += texto + "\n"
			strSeparadores2 += texto
			
		#
	#
	
	arquivo.write(strSeparadores)
	
	arquivo.close()
	
	return strSeparadores2
#

def main():
	
	arquivo = open('constituicaoBr.txt', 'r')
	linha = arquivo.read()
	
	
	print(libplnbsi.selecionaSeparadores(linha))	
	
	
	return 0

if __name__ == '__main__':
	main()

