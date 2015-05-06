"""
Construa a função removeAcento(<texto>) que retorna uma versão de <texto> com os caracteres acentuados
substituidos por seus equivalentes não acentuados
"""

def removeAcento(pTexto):
	strSemAcento = "aeiou"
	strComAcento = "áàâãéèêẽíìîĩóòôõúùûũ"
	novoTexto = ""; j = 0; i = 0
	divisor = 4
	
	while i < len(pTexto):
		j = 0
		while j < len(strComAcento):
			if i < len(pTexto) and pTexto[i] == strComAcento[j]:
				if((j // divisor) <= 1) and ((j % divisor) != 0):
					pos = j // divisor
					novoTexto += strSemAcento[pos]
				else:
					pos = (j // divisor)
					novoTexto += strSemAcento[pos]
				#
				i += 1
			#
			j += 1
		#
		if i < len(pTexto):
			novoTexto += pTexto[i]
		#
		i += 1
	#
	return novoTexto
#


def main():
	texto = "[...] estão corretas. Porém, os seus significados são diferentes e devem ser usadas em situações diferentes. O substantivo acento se refere a um sinal gráfico e diacrítico que assinala a tonicidade de uma sílaba, bem como ao timbre, tom de voz e sotaque típico de uma região"
	print(removeAcento(texto))
	
	return 0

if __name__ == '__main__':
	main()

