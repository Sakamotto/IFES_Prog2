"""

"""


def main():
	
	arquivo = open("bibliotecas_geo.csv", 'r', encoding = "latin2")
	logWrite = open("geoLog.txt", "w")
	dicIndex = {}
	pos = 0
	
	linha = arquivo.readline()
	linha = arquivo.readline()
	
	while linha != "":
		chave = linha.split("|")
		dicIndex[(chave[1], chave[2])] = pos
		logWrite.write(chave[1] + "," + chave[2] + "," + str(pos) + "\n")
		
		pos = arquivo.tell()
		sk = arquivo.seek(pos)
		
		
		linha = arquivo.readline()
	#
	
	#~ for chave, valor in dicIndex.items():
		#~ logWrite.write(float(chave) + "," + str(valor) + "\n")
	#~ #
	logWrite.close()
	arquivo.close()
	
	return 0

if __name__ == '__main__':
	main()

