
from bisect import bisect_left 
from collections import namedtuple
from bitstream import BitStream
from numpy import *

def insertionSort(alist):

   for i in range(1,len(alist)):

       #element to be compared
       current = alist[i]

       #comparing the current element with the sorted portion and swapping
       while i>0 and alist[i-1]>current:
          alist[i] = alist[i-1]
          i = i-1
          alist[i] = current

       #print(alist)

   return alist


class nodo_btree:

	def __init__(self, ordem, chave, offset, raiz, folha, arquivo):
		self.offset=0 #4 bytes
		self.ordem = ordem #4 bytes
		self.numero_chaves =1 #2 bytes
		self.folha= folha #1 bit
		self.raiz=raiz #1bit
		self.array_chaves_offsets = [(chave, offset)] #8 bytes
		self.array_nodos= [] #4 bytes
		self.arquivo =arquivo

	def isfull(self):
		if(self.numero_chaves > self.ordem*2):
			print(self.numero_chaves)
			print(self.ordem*2)
			return True
		else:
			return False

	def insert_raiz(self, nodo, chave, offset, arquivo) :
		pos = bisect_left(nodo.array_chaves_offsets, (chave, offset))
		if nodo.folha:
			nodo.array_chaves_offsets.insert(pos, (chave,offset))
			nodo.numero_chaves=nodo.numero_chaves+1
			if nodo.isfull():
				print("ele entra aqui por acaso?")
				nodo.split_raiz()
		else:			
			returno =  nodo.insert_key(nodo.array_nodos[pos], chave, offset, nodo.arquivo)
			if returno == -1:
				return True
			else:
				novo_pos = bisect_left(nodo.array_chaves_offsets, second(returno))
				nodo.array_chaves_offsets.insert(novo_pos,second(returno))
				nodo.array_nodos.insert(novo_pos,first(returno))
				if(nodo.isfull()):
					nodo.split_raiz()


	def insert_key(self, nodo, chave, offset, arquivo):
		pos = bisect_left(nodo.array_chaves_offsets, (chave, offset))
		if nodo.folha:
			nodo.array_chaves_offsets.insert(pos,(chave, offset))
			nodo.numero_chaves=nodo.numero_chaves +1
			if nodo.isfull():
				return split_node
			else:
				return -1
		else:
			returno = insert_key(nodo.array_nodos[pos], chave, offset)
			if returno == -1:
				return returno
			else:
				novo_pos = bisect_left(nodo.array_chaves_offsets, second(returno))
				nodo.array_chaves_offsets.insert(novo_pos,second(returno))
				nodo.array_nodos.insert(novo_pos,first(returno))
				if(nodo.isfull()):
					novo_returno = nodo.split_node()
					return novo_returno
				else:
					return -1



	def split_raiz(self):
		meio = int(self.numero_chaves/2)
		nodo_esquerdo = nodo_btree(self.ordem ,first(self.array_chaves_offsets[0]), second(self.array_chaves_offsets[0]), False, self.folha, self.arquivo)
		nodo_direito = nodo_btree(self.ordem ,first(self.array_chaves_offsets[meio+1]), second(self.array_chaves_offsets[meio+1]), False, self.folha,self.arquivo)		
		for i in self.array_chaves_offsets[1:meio] :
			nodo_esquerdo.array_chaves_offsets.append(i)
		for i in self.array_nodos[:meio+1]:
			nodo_esquerdo.array_nodos.append(i)
		for i in self.array_chaves_offsets[meio+2:]:
			nodo_direito.array_chaves_offsets.append(i)
		for i in self.array_nodos[meio+1:]:
			nodo_direito.array_nodos.append(i)
		self.array_chaves_offsets= [self.array_chaves_offsets[meio]]
		for i in self.array_chaves_offsets:
			print(i)
		self.array_nodos =[nodo_esquerdo, nodo_direito]
		self.folha=False
		self.numero_chaves=0

	def split_node(self):
		meio = int(self.numero_chaves/2)
		nodo_esquerdo = nodo_btree(self.ordem ,first(self.array_chaves_offsets[0]), second(self.array_chaves_offsets[0]), False,self.folha, self.arquivo)
		nodo_direito = nodo_btree(self.ordem ,first(self.array_chaves_offsets[meio+1]), second(self.array_chaves_offsets[meio+1]), False,self.folha, self.arquivo)

		for i in self.array_chaves_offsets[1:meio] :
			nodo_esquerdo.array_chaves_offsets.append(i)
		
		for i in self.array_chaves_offsets[meio+2:]:
			nodo_direito.array_chaves_offsets.append(i)
		if not self.folha:
			for i in self.array_nodos[:meio+1]:
				nodo_esquerdo.array_nodos.append(i)
			for i in self.array_nodos[meio+1:]:
				nodo_direito.array_nodos.append(i)
		volta = (self.array_chaves_offsets[meio])
		self = nodo_esquerdo
		return (nodo_direito,(volta))

	def Escreve_nodo_bin(self):
			total_impresoes = self.ordem*2
			parte_zero = total_impresoes - self.numero_chaves
			if self.folha :
				impresoes_ponteiros = self.ordem*2 +1
				ponteiros_zero = 0
			else:
				impresoes_ponteiros = self.numero_chaves +1
				ponteiros_zero = self.ordem*2 +1 - impresoes_ponteiros
			arquivo_btree = open(self.arquivo, 'ab+')
			self.offset = arquivo_btree.tell()
			stream_btree = BitStream()
			bitarray_btree = stream_btree.write(self.offset, uint32)
			bitarray_btree = stream_btree.write(self.ordem, uint16)
			bitarray_btree = stream_btree.write(self.numero_chaves, uint16)
			bitarray_btree = stream_btree.write(self.folha, bool)
			bitarray_btree = stream_btree.write(self.raiz, bool)
			
			for i in range(0 , self.numero_chaves):
				bitarray_btree = stream_btree.write(first(self.array_chaves_offsets[i]), uint32)
				bitarray_btree = stream_btree.write(second(self.array_chaves_offsets[i]),uint32)
			for i in range(0,parte_zero):
				bitarray_btree = stream_btree.write(0, uint32)
				bitarray_btree = stream_btree.write(0, uint32)
			for i in range(0,impresoes_ponteiros):
				bitarray_btree = stream_btree.write(self.offset, uint32)
			for i in range(0,ponteiros_zero):
				bitarray_btree = stream_btree.write(0, uint32)
			print(stream_btree)

def first( tupla):
	return tupla[0]

def second(tupla):
	return tupla[1]

btree_matchs= "btree_matchs"
stream = BitStream()
raiz = nodo_btree(2,13 , 6, True, True, btree_matchs)
print("inicio")
for i in raiz.array_chaves_offsets:
	print(i)
print("inicio1")
raiz.insert_raiz(raiz, 33, 6,btree_matchs)
for i in raiz.array_chaves_offsets:
	print(i)
print("inicio2")
raiz.insert_raiz(raiz, 55, 6,btree_matchs)
for i in raiz.array_chaves_offsets:
	print(i)
print("inicio3")
raiz.insert_raiz(raiz, 66 , 6,btree_matchs)
for i in raiz.array_chaves_offsets:
	print(i)
print("inicio3")
raiz.insert_raiz(raiz, 40 , 6,btree_matchs)
print( "fim das insercoes")
for i in raiz.array_chaves_offsets:
	print(i)

raiz.insert_raiz(raiz, 15 , 6,btree_matchs)
print("testando filho esquerda")
filho_esquerda = raiz.array_nodos[0]
for i in filho_esquerda.array_chaves_offsets:
	print(i)
print("testando filho direita")
raiz.insert_raiz(raiz, 57 , 6,btree_matchs)
filho_esquerda = raiz.array_nodos[1]
for i in filho_esquerda.array_chaves_offsets:
	print(i)
print("inicio3")

raiz.insert_raiz(raiz, 11 , 6,btree_matchs)
raiz.insert_raiz(raiz, 22 , 6,btree_matchs)
raiz.Escreve_nodo_bin()