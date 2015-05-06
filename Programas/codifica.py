"""
Entrada: Um texto qualquer
Saida: No lugar de nomes (com letras maiúsculas), retorna M, se  for preposição, retorna p,
se for numeral, retorna N, se for conjunção, retorna c ...
"""
import libProg2

def codifica(pTexto): # pTexto nesse caso, são Tokens
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

def main():
	tokens, pos = libProg2.tokenizador("Tudo tem o seu tempo determinado, e há tempo para todas as coisas debaixo do céu 55/55/55")
	print(codifica(tokens))
	
	
	
	return 0

if __name__ == '__main__':
	main()

