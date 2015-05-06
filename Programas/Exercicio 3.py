"""

"""

def corrente(pTexto, pPosicao):
	strSeparadores = " ,.:;!?"
	esquerda = pPosicao; direita = pPosicao; palavra = "Não tem nada aqui :/"
	
	if pTexto[esquerda] not in strSeparadores:
		while esquerda >= 0 and pTexto[esquerda] not in strSeparadores:
			esquerda -= 1
		#
		while direita < len(pTexto) and pTexto[direita] not in strSeparadores:
			direita += 1
		#
		palavra = pTexto[esquerda + 1:direita]
	else:
		palavra = "None"
	#
	return palavra
#

def anterior(pTexto, pPosicao):
	strSeparadores = " ,.:;!?"
	aux = pPosicao
	
	if pTexto[aux] not in strSeparadores:
		while aux >= 0 and pTexto[aux] not in strSeparadores:
			aux -= 1
		#
	#
	if pTexto[aux] in strSeparadores:
		while aux >= 0 and pTexto[aux] in strSeparadores:
			aux -= 1
		#
	#
	
	if aux < 0:
		return "None"
	else:
		return corrente(pTexto, aux)
	#
#

def proximo(pTexto, pPosicao):
	strSeparadores = " ,.:;!?"
	aux = pPosicao
	
	if pTexto[aux] not in strSeparadores:
		while aux < len(pTexto) and pTexto[aux] not in strSeparadores:
			aux += 1
		#
	#
	
	if pTexto[aux] in strSeparadores:
		while aux < len(pTexto) and pTexto[aux] in strSeparadores:
			aux += 1
		#
	#
	
	if aux >= len(pTexto):
		return "None"
	else:
		return corrente(pTexto, aux)
	#
#

def main():
	
	texto = "Oi Eu sou Goku!"
	print(corrente(texto, 7))
	print(anterior(texto, 7))
	print(proximo(texto, 7))
	
	return 0

if __name__ == '__main__':
	main()

