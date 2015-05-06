"""
Biblioteca criada com todas as funções criadas em Programação 2
"""

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

def insereEspacos(pTexto):
	strSeparadores = " .,:;!?(){}[]/\\"
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

def tokenizador(txt):
	lstTokens = []
	strbuffer = ''
	lstposicoes = []
	pos = 0
	separador = ' ,!?.:;/-_\\()[]{}'
	
	for pos in range(len(txt)):
		if txt[pos] not in separador:
			strbuffer += txt[pos]
		else:
			if strbuffer != '':
				lstTokens.append(strbuffer)
				lstposicoes.append(pos-len(strbuffer))
				strbuffer = ''
			if txt[pos] not in [' ','\t']:
				lstTokens.append(txt[pos])
				lstposicoes.append(pos)
	if strbuffer != '':
		lstTokens.append(strbuffer)
		lstposicoes.append(pos-len(strbuffer))
	
	return lstTokens, lstposicoes
#
	
def separaPal(pTexto):
	strSeparadores = ' ,!?.:;/-_\\()[]{}'
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

def separaPal2(pTexto):
	textoAux = insereEspacos(pTexto)
	lstPals = textoAux.split()
	pos = 0
	
	for pos in range(len(lstPals)):
		if not pos.isalpha():
			del(pos)
		else:
			pos += 1
		#
	#
	return lstPals
#

def codifica(pTexto):
	preposicoes = ['a', 'ante', 'até', 'após', 'com', 'contra','de', 'desde','em','entre','para','per',
	'perante','por','sem','sob','sobre','trás']
	conjuncoes = ['e', 'nem', 'mas também', 'como também', 'bem como', 'mas ainda','mas', 'porém', 'todavia', 'contudo', 'antes']
	artigos = ['o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas']
	strCodificada = ""
	
	for elem in pTexto:
		if elem.lower() in preposicoes:
			strCodificada += 'p'
		elif elem.lower() in artigos:
			strCodificada += 'a'
		elif elem.lower() in conjuncoes:
			strCodificada += 'c'
		elif elem[0].isupper():
			strCodificada += 'M'
		elif elem.isdigit():
			strCodificada += 'N'
		elif elem.islower:
			strCodificada += 'm'
		else:
			strCodificada += elem
		#
	return strCodificada
#

