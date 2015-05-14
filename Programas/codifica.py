"""
Entrada: Um texto qualquer
Saida: No lugar de nomes (com letras maiúsculas), retorna M, se  for preposição, retorna p,
se for numeral, retorna N, se for conjunção, retorna c ...
"""
import libplnbsi

#Codifica recebe um texto tokenizado
def codifica(pTexto):
	preposicoes = ['a', 'ante', 'após', 'com', 'contra','de','do', 'desde','em','entre','para','per',
	'perante','por','sem','sob','sobre','trás']
	conjuncoes = ['e', 'nem', 'mas também', 'como também', 'bem como', 'mas ainda','mas', 'porém', 'todavia', 'contudo', 'antes']
	artigos = ['o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas']
	
	pTratamentos = ['V. A.','V. Ema.','V. Emas.','V. Revma.','V. Ex.ª','V. Mag.ª','V. M.','V. M. I.','V. S.','V. S.ª','V. O.']
	
	strCodificada = ""
	
	for elem in pTexto:
		if elem.isalpha():
			if elem.lower() in preposicoes:
				strCodificada += 'p'
			elif elem.lower() in artigos:
				strCodificada += 'a'
			elif elem.lower() in conjuncoes:
				strCodificada += 'c'
			elif elem.lower() in pTratamentos:
				strCodificada += 'T'
			elif elem[0].isupper():
				strCodificada += 'M'
			elif elem.islower:
				strCodificada += 'm'
		elif elem.isdigit():
			strCodificada += 'N'
		elif elem.isalnum():
			strCodificada += "AL"
		else:
			strCodificada += elem
		#
	return strCodificada
#

def main():
	tokens, pos = libplnbsi.tokenizador("Tudo tem. O seu MP3 tempo determinado, e há tempo para todas as coisas debaixo do céu 55/55/55")
	print(codifica(tokens))
	
	#~ pTratamentos = ['V.A.','V.Ema.','V.Emas.','V.Revma.','V.Ex.a','V.Mag.','V.M.','V.M.I.','V.S.','V.Sra','V.O.']
	#~ 
	#~ palavra = ""
	#~ 
	#~ texto = "V. Sra pretende sair hoje. Você já falou com V.M Alexander?"
	#~ 
	#~ for elem in pTratamentos:
		#~ palavra += libplnbsi.insereEspacos(elem)
	#~ #
	#~ tokens = libplnbsi.tokenizador(texto)[0]
	#~ 
	#~ for i in range(len(tokens)):
		#~ if tokens[i] == ".":
			#~ tokens[i] = "0"
		#~ #
	#~ #
	#~ 
	#~ print(tokens)
	#~ 
	#~ print(tokens)
	#~ palavra = palavra.split()
	#~ print(palavra)
	#~ 
	#~ lenPalavra = len(palavra)
	#~ lenTokens = len(tokens)
	#~ 
	#~ i = 0
	#~ while i < lenPalavra:
		#~ j = 0
		#~ while j < lenTokens:
			#~ if palavra[i] == tokens[j]:
				#~ 
	#~ 
	
	
	return 0

if __name__ == '__main__':
	main()

