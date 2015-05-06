"""
Um n-grama é uma sequência de caracteres de tamanho n, por exemplo:
"goiaba" --> 1-grama: g, o, i, a, b, a
			 2-grama: go, oi, ia, ab, ba
			 3-grama: goi, oia, iab, aba
			 ...
Construa a função ngrama(<texto>, <tam>) que retorna uma  lista contendo os n-gramas de tamanho <tam> de <texto>
"""

def nGrama(pTexto, tam):
	ngramas = []
	
	for i in range(len(pTexto)):
		if i <= len(pTexto) - tam:
			ngramas.append(pTexto[i: tam + i])
		#
	#
	return ngramas
#	


def main():
	
	texto = "goiaba"
	print(nGrama(texto, 3))
	
	return 0

if __name__ == '__main__':
	main()

