
def criar(strData):
	lstdata = strData.split("/")
	for i in range(len(lstdata)):
		lstdata[i] == int(lstdata[i])
	#
	return {'dia': int(lstdata[0]), 'mes': int(lstdata[1]), 'ano' : int(lstdata[2])}
#

def igualData(paramDataA, paramDataB):
	return paramDataA == paramDataB
#

def validaData(paramData):
	if paramData['ano'] > 0 and paramData['dia'] > 0 and paramData['mes'] > 0:
		if paramData['dia'] < 31 and paramData['mes'] < 13:
			return True
		#
	#
	return False
#

def dateToYear(paramData):
	return paramData['ano'] * 365 + paramData['mes'] * 30 + paramData['dia']
#

#~ def DaysToDate(dias):

def soma(paramDataA, dias):
	dataA = dateToYear(paramDataA)
	soma = dataA + dias
#	

def main():
	
	strData = input("Data A: ")
	dataA = criar(strData)
	strData = input("Data B: ")
	dataB = criar(strData)
	
	if validaData(dataA) and validaData(dataB):
		if igualData(dataA, dataB):
			print("Datas Iguais!")
		else:
			print("Datas Diferentes!")
		#
	else:
		print("Uma das datas são inválidas!")
	#
	return 0

if __name__ == '__main__':
	main()

