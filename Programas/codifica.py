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
	
	mpTratamentos = ['Sr', 'Sra', 'Srta', 'Srs', 'Sras', 'Srª', 'Srº', 'Srªs', 'Ema']
	pTratamentos = ['A','Ema','Emas','Revma','Ex.a','Mag.a','M.','M.I.','S.','Sra','O.']
	
	strCodificada = ""
	i = 0
	
	for elem in pTexto:
		if elem.isalpha():
			if elem.lower() in preposicoes:
				strCodificada += 'p'
			elif elem.lower() in artigos:
				strCodificada += 'a'
			elif elem.lower() in conjuncoes:
				strCodificada += 'c'
			#elif elem in pTratamentos:
				#strCodificada += 'T'
				#strCodificada = strCodificada[: -2] + 'T'
			elif elem in mpTratamentos:
				strCodificada += 'T'
			elif elem[0].isupper():
				strCodificada += 'M'
			elif elem.islower:
				strCodificada += 'm'
		elif elem.isdigit():
			strCodificada += 'N'# Número
		elif elem.isalnum():
			strCodificada += 'A' #Alfanumérico
		else:
			strCodificada += elem
		#
	return strCodificada
#

def main():
	#arquivo = open("")
	texto = "Srª Cristine ... Tudo tem. O seu MP3 tempo determinado, e há tempo para todas V.Emª Karen coisas debaixo do céu. V.Sra está pronta? 55/55/55"
	texto = libplnbsi.insereEspacos(texto)
	tokens, pos = libplnbsi.tokenizador(texto)
	print(tokens)
	print(libplnbsi.extraiPadrao(tokens, ['V.TM', 'M', 'TM']))
	#~ #print(tokens)
	#~ #print(codifica(tokens))
	
	#~ l = ['Cris','Al','Haha','Teste']
	#~ print(l[:2])
	
	
	return 0

if __name__ == '__main__':
	main()

