"""
	Construa um TAD matriz numérica com as seguintes características:

		a) seja implementado utilizando dicionário(s).
		b) elementos iguais a zero não devem ser armazenados.

	Funções do TAD:
		c) criar(linhas, colunas): cria e retorna um TAD matriz de dimensões linhas, colunas dadas. Retorna
None se os valores de dimensões forem inválidas. *Feito
		d) igual(TADMatrizA, TADMatrizB): retorna True se os TADMatrizes passados como argumento são iguais,
False caso contrário. *Feito
		e) determinante(TADMatrizA): retorna o valor do determinante do TADMatriz passado como parâmetro.
Retorna None se o parâmetro não suportar determinante.
		f) inversa(TADMatrizA): pesquise e implemente um algoritmo para o cálculo da inversa de uma matriz.
		g) similarCos(TADMatrizA, TADMatrizB): implemente o método do cosseno (pesquise) para avaliar o nível
de similaridade entre dois tadmatrizes.
		h) similarJac(TADMatrizA, TADMatrizB): implemente o método de Jaccard (pesquise) para avaliar o nível
de similaridade entre dois tadmatrizes.
		i) vizinhos(TADMatrizA, i, j): retorna os 8 vizinhos de uma determinada posição i,j do tadmatriz de
entrada. Vizinhos que não existem devem receber valor None. Ver a explicação do professor.
		j) transposta(TADMatrizA): retorna a matriz transposta do parâmetro de entrada.
		k) similar(TADMatrizA, TADMatrizB): pesquise e implemente um terceiro método de avaliação de
similaridade entre os tadmatrizes de entrada.
		l) multip(TADMatrizA, TADMatrizB): retorna a matriz produto das matrizes de entrada (tads). Retorna
None se as matrizes não puderem ser multiplicadas. *Feito
		m) andMat(TADMatrizA, TADMatrizB): retorna a matriz AND das matrizes de entrada. Cada elemento dessa
matriz é o resultante and lógico dos elementos correspondentes dos tadmatrizes de entrada. Faça o
mesmo para as operações lógicas de NOT, OR e XOR (pesquise as funções/operadores python que executam
essas operações.).
		o) adElem(TADMatriz, elem, i, j): altera a matriz de entrada adicionando o elemento na posição i, j do
tadmatriz. Caso i, j sejam posições invaálidas, retornar None. Retornar a matriz em caso de sucesso. *Feito
		p) getElem(TADMatriz, i, j): retorna o elemento armazenado na posição i, j de TADMatriz. *Feito
		q) extrai(TADMatriz, i, j, alt, larg): extrai uma submatriz (tadmatriz) de dimensões alt, larg a
partir da posição i, j de TADMatriz. Retorna None se a submatriz (tad) não puder ser retornado.
		r) insere(TADMatrizA, TADMatrizB, i, j): insere a matriz B na amtriz A a aprtir da posição i, j.
Retorna None se a matriz B não puder ser inserida.

"""

def criar(linhas, colunas):
	if linhas < 1 or colunas < 1:
		return None
	#
	return {"linha": linhas, "coluna": colunas}
#


# Função para adicionar duas novas colunas à matriz para calcular o determinante.
def _copia_dic(mat):
	linha = mat["linha"]
	coluna = mat["coluna"]
	newMat = mat.copy()
	newMat["coluna"] = mat["coluna"] + 2
	
	for i in range(linha):
		for j in range(coluna - 1):
			newMat[(i,j + coluna)] = mat[(i, j)]
		#
	#
	return newMat
#

def _cofator(mat, col_fixada, linha):
	#~ for linha in range(len(mat["linha"])):
	return (-1)**(linha + col_fixada)
	#
#	


def det_jacobi(mat):
	det = 1; i = 0; j = 0; aux = 0
	dicMat =  _copia_dic(mat)
	linha = dicMat["linha"]
	coluna = dicMat["coluna"]
	soma = 0
	
	for col_i in range(dicMat["coluna"]):
		coluna = col_i
		det = 1
		for linha in range(dicMat["linha"]):
			det *= getElem(dicMat, linha, coluna)
			coluna += 1
		#
		soma += det
	#

	soma_s = 0
	for col_i in range(dicMat["coluna"]):
		coluna = col_i
		det = 1
		for linha in range(dicMat["linha"]):
			det *= getElem(dicMat, linha, coluna)
			coluna -= 1
		#
		soma_s += det
	#
	return soma - (soma_s)
#

def diminui_mat(mat, col_fixada, linha_fix):
	linha_fixada = linha_fix
	newDic = criar(mat["linha"] - 1, mat["coluna"] - 1)
	
	lin = 0
	col = 0
	
	for linha in range(mat["linha"]):
		if linha != linha_fix:
			col = 0
			for coluna in range(mat["coluna"]):
				if coluna != col_fixada:
					adElem(newDic, getElem(mat,linha,coluna), lin, col)
					col += 1
				#			
			lin += 1
			#
		#
	#
	return newDic
#
				

def det_laplace(mat):
	col_fixada = 0
	soma = 0
	if mat["linha"] == 3:
		return det_jacobi(mat)
	else:
		for i in range(mat["linha"]):
			soma += mat[(col_fixada, i)]*((-1)**(2+i))*det_laplace(diminui_mat(mat,col_fixada, i))
			#~ print(det_jacobi(diminui_mat(mat,col_fixada, i)), "Passei", end="\n\n")
			#~ print(diminui_mat(mat,col_fixada, i), "Mat", end="\n\n")
		#
	#
	return soma
#
			
		

def igual(matA, matB):
	resp = False
	
	if matA["linha"] != matB["linha"] or matA["coluna"] != matB["coluna"] or len(matA) != len(matB):
		return resp
	else:
		for chaveA in matA.keys():
			for chaveB in matB.keys():
				if chaveA == chaveB:
					if matA[chaveA] == matB[chaveB]:
						resp = True
					else:
						return False
					#
				#
			#
		#
	#
	
	return resp
#
				
def adElem(TADMatriz, elem, i, j):
	if elem != 0 and i <= TADMatriz['linha'] and j <= TADMatriz['coluna']:
		TADMatriz[(i,j)] = elem
	#
#

def getElem(TADMatriz, i, j):
	try:
		return TADMatriz[(i,j)]
	except:
		return 0
	#
#

def multip(matA, matB):
	soma = 0
	if matA['coluna'] == matB['linha']:
		mat_result = criar(matB['linha'],  matA['coluna'])
		for i in range(matA['linha']):
			for j in range(matB['linha']):
				soma = 0
				for k in range(matA['coluna']):
					soma +=  getElem(matA, i, k) * getElem(matB, k, j)
				adElem(mat_result, soma, i, j)
				#
			#
		#
		return mat_result
	else:
		return None
	#
#
	
	

def main():
	a = {"linha": 4, "coluna": 4, (0,0): 1, (0,1): 4, (0,2): 7, (0,3): 2, (1,0): 2, (1,1): 5, (1,2): 8, (1,3): 3, (2,0): 3, (2,1): 6, (2,2): 9, (2,3): 1, (3,0): 1, (3,1): 2, (3,2): 4, (3,3): -2}
	b = {"linha": 3, "coluna": 3, (0,0): 2, (0,1): 8, (0,2): 3, (1,0): 3, (1,1): 9, (1,2): 1, (2,0): 1, (2,1): 4, (2,2): -2}
	c = {"linha": 3, "coluna": 3, (0,0): 2, (0,1): 8, (0,2): 9, (1,0): 4, (1,1): 6, (1,2): 20, (2,0): 10, (2,1): -1, (2,2): -2}
	
	matA = criar(4,3)
	matB = criar(4,3)
	#~ print(len(a), len(b))
	#~ print(igual(a, b))
	#~ 
	print(multip(b, c))
	#~ print(det_jacobi(b))
	#~ diminui_mat(a, 0, 1)
	#~ print(det_laplace(a))
	#~ print(a)
	
	#~ adElem(matA, 4, 0,0)
	#~ print(matA)
	
	
	
	return 0

if __name__ == '__main__':
	main()

