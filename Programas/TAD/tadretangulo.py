#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tadretangulo.py

import tadreta
import tadponto

def criarVtx(xsupE, ysupE, xinfD, yinfD):
	alt = yinfD - ysupE
	larg = xinfD - xsupE
	return [[xsupE, ysupE],[xinfD, yinfD]]
#

def criarDim(xsupE, ysupE, larg, alt):
	return [[xsupE, ysupE],[xsupE + larg,ysupE + alt]]
#

# Recebe como parâmetro um TAD retângulo e retorna uma lista de tad pontos com os cantos superior esquerdo e
# inferior direito, respectivamente.
def getCantos(paramTadRet):
	cse = paramTadRet[0]
	cid = paramTadRet[3]
	
	return [tadponto.criar(cse[0], cse[1]), tadponto.criar(cid[0], cid[1])]
#

def _getLados(paramTadRet):
	base = tadponto.distancia(paramTadRet[0], paramTadRet[1])
	altura = tadponto.distancia(paramTadRet[0], paramTadRet[2])
	return base, altura
#

# Retorna um float com o valor do perímetro.
def perimetro(paramTadRet):
	base, altura = _getLados(paramTadRet)
	return base * 2 + altura * 2
#

def area(paramTadRet):
	base, altura = _getLados(paramTadRet)
	return (base * altura) / 2
#

def igual(paramTadRetA, paramTadRetB):
	for i in range(len(paramTadRetA)):
		if paramTadRetA[i] != paramTadRetB[i]:
			return False
		#
	#
	return True		
#


# Desloca, no plano, o retângulo (sua origem) de dx na coordenada x e
# dy na coordenada y.
def move(paramTadRet, dx, dy):
	paramTadRet[0][0] += dx
	paramTadRet[0][1] += dy
	paramTadRet[1][0] += dx
	paramTadRet[1][1] += dy
	
	#return criarVtx(xsupE, ysupE, xinfD, yinfD)
#

# Função que verifica se um dado ponto está dentro de um retângulo
def ponto_in_ret(retangulo, ponto):
	cse = retangulo[0]
	cid = retangulo[1]
	
	xP = ponto[0]
	yP = ponto[1]
	
	if (cse[0] < xP) and (cse[1] < yP) and (xP < cid[0]) and (yP < cid[1]):
		return True
	else:
		return False
	#
#

def intersec(retA, retB):
	
	cseB = retB[0]
	csdB = [retB[1][0], retB[0][1]]
	cieB = [retB[0][0], retB[1][1]]
	cidB = retB[1]
	
	cseA = retA[0]
	csdA = [retA[1][0], retA[0][1]]
	cieA = [retA[0][0], retA[1][1]]
	cidA = retA[1]
	
	if supEsq(retA, cseB) and supDir(retA, csdB) and infEsq(retA, cieB) and infDir(retA, cidB):
		return retB
	elif infDir(retA, cidB) and infEsq(retA, cieB):
		return [[cseB[0], cseA[1]], cidB]
	elif supEsq(retA, cseB) and supDir(retA, csdB):
		return [cseB, [csdB[0], cieB[1]]]
	elif supEsq(retA, cseB) and infEsq(retA, cieB):
		return [cseB, [csdA[0], cieB[1]]]
	elif supDir(retA, csdB) and infDir(retA, cidB):
		return [[cseA[0], csdB[1]], cidB]
	elif supEsq(retA, cseB):
		return [cseB, cidA]
	elif supDir(retA, csdB):
		return [[cseA[0], csdB[1]],[csdB[0], cidA[1]]]
	elif infDir(retA, cidB):
		return [cseA, cidB]
	elif infEsq(retA, cieB):
		return [[cseB[0], cseA[1]],[csdA[0], cieB[1]]]
	#
#

#~ def intersec(paramTadRetA, paramTadRetB):
	#~ cseA = paramTadRetA[0]; cseB = paramTadRetB[0]
	#~ csdA = paramTadRetA[1]; csdB = paramTadRetB[1]
	#~ cieA = paramTadRetA[2]; cieB = paramTadRetB[2]
	#~ cidA = paramTadRetA[3]; cidB = paramTadRetB[3]
	#~ tp = 0
	#~ 
	#~ if (supEsq(paramTadRetA, paramTadRetB) and supDir(paramTadRetA, paramTadRetB) 
	#~ and infEsq(paramTadRetA, paramTadRetB) and infDir(paramTadRetA, paramTadRetB)):
		#~ #print(cseA)
		#~ tp = paramTadRetB
		#~ print("1 o/")
	#~ elif (infDir(paramTadRetA, paramTadRetB) and not supDir(paramTadRetA, paramTadRetB) and not infEsq(paramTadRetA, paramTadRetB)
	#~ and not supEsq(paramTadRetA, paramTadRetB)):
		#~ tp = criarVtx(cseA[0], cseA[1], cidB[0], cidB[1]) # (cidB, cseA)
		#~ print("2")
	#~ elif (infEsq(paramTadRetA, paramTadRetB) and not infDir(paramTadRetA, paramTadRetB) and not supDir(paramTadRetA, paramTadRetB)
		#~ and not supEsq(paramTadRetA, paramTadRetB)):
		#~ xsupE = cieB[0]
		#~ ysupE = csdA[1]
		#~ 
		#~ larg = csdA[0] - xsupE; alt = cieB[1] - ysupE
		#~ 
		#~ xinfD = larg + xsupE
		#~ yinfD = alt + ysupE
		#~ 
		#~ tp = criarVtx(xsupE, ysupE, xinfD, yinfD) #(cieB, csdA)
		#~ print("3")
	#~ elif (supDir(paramTadRetA, paramTadRetB) and not infEsq(paramTadRetA, paramTadRetB) and not infDir(paramTadRetA, paramTadRetB)
		#~ and not supEsq(paramTadRetA, paramTadRetB)):
		#~ xsupE = cieA[0]
		#~ ysupE = csdB[1]
		#~ 
		#~ larg = csdB[0] - xsupE; alt = cieA[1] - ysupE
		#~ 
		#~ xinfD = larg + xsupE
		#~ yinfD = alt + ysupE
		#~ 
		#~ tp = criarVtx(xsupE, ysupE, xinfD, yinfD) #(csdB, cieA)
		#~ print("4")
	#~ elif (supEsq(paramTadRetA, paramTadRetB) and not infEsq(paramTadRetA, paramTadRetB) and not infDir(paramTadRetA, paramTadRetB)
		#~ and not supDir(paramTadRetA, paramTadRetB)):
		#~ tp = criarVtx(cseB[0], cseB[1], cidA[0], cidA[1]) #(cseB, cieA)
		#~ print("5")
	#~ elif supEsq(paramTadRetA, paramTadRetB) and not infDir(paramTadRetA, paramTadRetB) and not supDir(paramTadRetA, paramTadRetB):
		#~ tp = criarVtx(cseB[0], cseB[1], cidA[0], cidB[1])
		#~ #print(tp)
		#~ tp = criarVtx(cseB[0], cseB[1], csdA[0], cieB[1])
		#~ print("HAHAHAHAH")
	#~ elif supDir(paramTadRetA, paramTadRetB) and infDir(paramTadRetA, paramTadRetB): # and not infEsq(paramTadRetA, paramTadRetB):
		#~ tp = criarVtx(cseA[0], csdB[1], cidB[0], cidB[1])
		#~ print("LALALAL")
	#~ return tp
#~ #
	
#~ def intersec(paramTadRetA, paramTadRetB):
	#~ cseA = paramTadRetA[0]; cseB = paramTadRetB[0]
	#~ csdA = paramTadRetA[1]; csdB = paramTadRetB[1]
	#~ cieA = paramTadRetA[2]; cieB = paramTadRetB[2]
	#~ cidA = paramTadRetA[3]; cidB = paramTadRetB[3]
	#~ tp = -1
	#~ 
	#~ if (supEsq(paramTadRetA, paramTadRetB) and supDir(paramTadRetA, paramTadRetB) 
	#~ and infEsq(paramTadRetA, paramTadRetB) and infDir(paramTadRetA, paramTadRetB)):
		#~ print(cseA)
		#~ print("1 o/")
		#~ return [paramTadRetB[0], paramTadRetB[3]]
	#~ elif (infDir(paramTadRetA, paramTadRetB) and not infEsq(paramTadRetA, paramTadRetB) and not supEsq(paramTadRetA, paramTadRetB)
	#~ and not supDir(paramTadRetA, paramTadRetB)):
		#~ print("2")
		#~ return [paramTadRetA[0], paramTadRetB[3]] # (cidB, cseA)
	#~ elif (infEsq(paramTadRetA, paramTadRetB) and not infDir(paramTadRetA, paramTadRetB) and not supEsq(paramTadRetA, paramTadRetB)
	#~ and not supDir(paramTadRetA, paramTadRetB)):
		#~ xsupE = cieB[0]
		#~ ysupE = csdA[1]
		#~ 
		#~ larg = csdA[0] - xsupE; alt = cieB[1] - ysupE
		#~ 
		#~ xinfD = larg + xsupE
		#~ yinfD = alt + ysupE
		#~ 
		#~ return [paramTadRetB[2], paramTadRetA[1]] #(cieB, csdA)
		#~ print("3")
	#~ elif (cieA[0] < csdB[0] and cieA[1] > csdB[1]) and (cieB[0] < cieA[0] and cieB[1] > cieA[1]):
		#~ xsupE = cieA[0]
		#~ ysupE = csdB[1]
		#~ 
		#~ larg = csdB[0] - xsupE; alt = cieA[1] - ysupE
		#~ 
		#~ xinfD = larg + xsupE
		#~ yinfD = alt + ysupE
		#~ 
		#~ return criarVtx(xsupE, ysupE, xinfD, yinfD) #(csdB, cieA)
		#~ print("4")
	#~ elif (cidA[0] > cseB[0] and cidA[1] > cseB[1]) and (cidA[0] < cidB[0] and cidA[1] < cidB[1]):
		#~ return criarVtx(cseB[0], cseB[1], cidA[0], cidA[1]) #(cseB, cieA)
		#~ print("5")
	#~ elif supEsq(paramTadRetA, paramTadRetB) and not infDir(paramTadRetA, paramTadRetB) and not supDir(paramTadRetA, paramTadRetB):
		#~ tp = criarVtx(cseB[0], cseB[1], cidA[0], cidB[1])
		#~ #print(tp)
		#~ return criarVtx(cseB[0], cseB[1], csdA[0], cieB[1])
		#~ print("HAHAHAHAH")
	#~ elif supDir(paramTadRetA, paramTadRetB) and infDir(paramTadRetA, paramTadRetB): # and not infEsq(paramTadRetA, paramTadRetB):
		#~ return criarVtx(cseA[0], csdB[1], cidB[0], cidB[1])
		#~ print("LALALAL")
	#~ else:
		#~ return None
	#
#

# VERIFICA SE O CANTO SUPERIOR ESQUERDO DE B ESTÁ DENTRO DO RETÂNGULO A
def supEsq(retA, ponto):
	return ponto_in_ret(retA, ponto)
#

# VERIFICA SE O CANTO SUPERIOR DIREITO DE B ESTÁ DENTRO DO RETÂNGULO A
def supDir(retA, ponto):
	return ponto_in_ret(retA, ponto)
#

# VERIFICA SE O CANTO INFERIOR ESQUERDO DE B ESTÁ DENTRO DO RETÂNGULO A 
def infEsq(retA, ponto):
	return ponto_in_ret(retA, ponto)
#


# VERIFICA SE O CANTO INFERIOR DIREITO DE B ESTÁ DENTRO DO RETÂNGULO A 
def infDir(retA, ponto):
	return ponto_in_ret(retA, ponto)
#
	
		


def main():
	ret = criarVtx(10,10,20,20)
	ret2 = criarVtx(0,0,15,15)
	#~ print(getCantos(ret))
	#~ print(igual(ret, ret2))
	#~ print((30,30) > (20,30))
	#~ print(ret)
	#~ print(ret2)
	print(intersec(ret, ret2))
	
	print("Perímetro: ", perimetro(ret))
	print("Área: ", area(ret))
	
	return 0

if __name__ == '__main__':
	main()

