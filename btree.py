
from bisect import bisect_left 
from collections import namedtuple
import struct
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

       ##print(alist)

   return alist


class nodo_btree:

	def __init__(self, offset, arquivo):

		
		self.arquivo =arquivo #30 bytes
		self.Busca_nodo_bin(offset, arquivo)
		self.numero_chaves
		self.array_chaves_offsets =self.array_chaves_offsets
		self.array_nodos = self.array_nodos
		self.folha=self.folha
		self.raiz= self.raiz
		self.offset = offset
		self.ordem = self.ordem
		self.numero_chaves = self.numero_chaves
		

	def isfull(self):
		if(self.numero_chaves > self.ordem*2):
			return True
		else:
			return False

	def insert_raiz(self, nodo_offset, chave, offset, arquivo) :
		#print("----- ENtra em Insere Raiz ----")
		if(False):
			#print("chave ja existe, nao ira adicionar")
			return False
		else:
			nodo = nodo_btree(nodo_offset, arquivo)
			#print(isinstance(nodo.array_chaves_offsets, list))
			if(nodo.numero_chaves == 0):
				nodo.array_chaves_offsets.append((chave,offset)) #se ta vazio, só insere
				nodo.numero_chaves= 1
				#print("raiz vazia")
				nodo.Escreve_nodo_bin(0)
			else:			
				pos = bisect_left(nodo.array_chaves_offsets, (chave, offset))
				if (pos < len(nodo.array_chaves_offsets)):
					if first(nodo.array_chaves_offsets[pos]) == chave:
						return False
				if nodo.folha:
					if(pos == len(nodo.array_chaves_offsets)):
						nodo.array_chaves_offsets.append((chave,offset))
						nodo.numero_chaves=nodo.numero_chaves+1
						nodo.numero_chaves= len(nodo.array_chaves_offsets)
						if(nodo.numero_chaves !=  len(nodo.array_chaves_offsets)):
							#print("numero_chaves da raiz folha diferente do tamnha do array_chaves_offsets")
							#print("numero_chaves"+ str(nodo.numero_chaves))
							#print("nodo.array_chaves_offsets tamanho = "+ str(len(nodo.array_chaves_offsets)))
							#print("nodo.array_chaves_offsets:")
							#print(nodo.array_chaves_offsets)
							input()					
						if nodo.isfull():
							##print("ele entra aqui por acaso?")
							nodo.split_raiz()
						nodo.Escreve_nodo_bin(0)
						#print("--- sai de insere raiz---")
						return True

					elif not (first(nodo.array_chaves_offsets) == chave):
						nodo.array_chaves_offsets.insert(pos, (chave,offset))
						nodo.numero_chaves=nodo.numero_chaves+1
						if nodo.isfull():
							##print("ele entra aqui por acaso?")
							nodo.split_raiz()
							nodo.Escreve_nodo_bin(0)
							#print("--- sai de insere raiz---")
						else:
							nodo.Escreve_nodo_bin(0)
							#print("--- sai de insere raiz---")
						return True
					else:
						return False
				else:
					#print("tamnho do array_chaves_offsets = "+ str(len(nodo.array_chaves_offsets)))
					#print(nodo.array_chaves_offsets)
					#print("pos = "+str(pos)+ "tamanho do array_nodos = "+str(len(nodo.array_nodos)))
					if(nodo.array_nodos[pos] == 0):
						#print('tentando dar insert_key na raiz, nodo.array_nodos[pos] = '+str(nodo.array_nodos[pos]))
						input()

					##print("inserindo chave ="+str(chave)+" entre ("+str(nodo.array_chaves_offsets[pos-1])+ ','+str(nodo.array_chaves_offsets[pos]))			
					returno =  nodo.insert_key(nodo.array_nodos[pos], chave, offset, nodo.arquivo)
					if first(returno) == -1:
						return second(returno)
					else:

						#print(' nodo chave offset = ' +str(nodo.array_chaves_offsets))
						#print('segundo returno  = '+str(second(returno)))
						
						if isinstance(first(returno), tuple):
							#print("primeiro elemento de returno é tupla, mas deveria ser int, returno = "+str(returno))
							input()
						novo_pos = bisect_left(nodo.array_chaves_offsets, second(returno))
						nodo.array_chaves_offsets.insert(novo_pos,second(returno))
						
						if(first(returno) == self.offset):
							#print("tentando adicionar a proprio offset como nodo")
							#print("proprio offset = "+str(self.offset)+ ", offset a adicionar = " +str(first(returno)))
							input()
						nodo.array_nodos.insert(novo_pos,first(returno))
						nodo.numero_chaves=nodo.numero_chaves +1
						#print(' nodo chave offset = ' +str(nodo.array_chaves_offsets))
						#print('segundo returno  = '+str(second(returno)))
						#print("nodo array_nodos = "+str(nodo.array_nodos))
						#print("nodo.numero_chaves = "+str(nodo.numero_chaves))
						#print("parou pq mandei")
						#input()
						nodo.Escreve_nodo_bin(0)
						if(nodo.isfull()):
							nodo.split_raiz()
							raiz.Escreve_nodo_bin(0)


	def insert_key(self, nodo_offset, chave, offset, arquivo):
		#print("--  entra em insert_key ---")
		#print('entrando no nodo com offset = '+str(nodo_offset))
		nodo = nodo_btree(nodo_offset, arquivo)
		pos = bisect_left(nodo.array_chaves_offsets, (chave, offset))
		if (pos < len(nodo.array_chaves_offsets)):
				if first(nodo.array_chaves_offsets[pos]) == chave: #sempre procura a chave na btre, se estiver retorna FALSE
					return (-1, False)
		if nodo.folha:
			#print("pos ="+str(pos)+ 'chave = '+str(chave))
			#print("tamanho do array_chaves_offsets"+ str(len(nodo.array_chaves_offsets)))
			#print('numero_chaves do nodo = '+str(nodo.numero_chaves))
			#print(nodo.array_chaves_offsets)
			if(False):
				return (-1,False)
			else:
				nodo.array_chaves_offsets.insert(pos,(chave, offset))
				nodo.numero_chaves=nodo.numero_chaves +1
				if nodo.isfull():
					return nodo.split_node()
				else:
					nodo.Escreve_nodo_bin(nodo_offset)
					return (-1, True)
		else:
			returno = self.insert_key(nodo.array_nodos[pos], chave, offset, arquivo)
			if returno == -1:
				return returno
			else:
				novo_pos = bisect_left(nodo.array_chaves_offsets, second(returno))
				nodo.array_chaves_offsets.insert(novo_pos,second(returno))
				nodo.array_nodos.insert(novo_pos,first(returno))
				nodo.numero_chaves= nodo.numero_chaves +1
				#print(' nodo chave offset = ' +str(nodo.array_chaves_offsets))
				#print('segundo returno  = '+str(second(returno)))
				#print("nodo array_nodos = "+str(nodo.array_nodos))
				#print("nodo.numero_chaves = "+str(nodo.numero_chaves))
				#print("parou pq mandei")
				input()
				if(nodo.isfull()):
					novo_returno = nodo.split_node()
					return novo_returno
				else:
					#print(self.offset)
					nodo.Escreve_nodo_bin(nodo_offset)

					return (-1, second(returno))



	def split_raiz(self):
		#print("----Entra em split raiz --")
		meio = int(self.numero_chaves/2)
		nodo_esquerdo = nodo_btree(0, self.arquivo)
		nodo_direito = nodo_btree(0,self.arquivo)
		nodo_esquerdo.array_chaves_offsets = list()
		nodo_direito.array_chaves_offsets=list()	
		nodo_esquerdo.array_nodos=list()
		nodo_direito.array_nodos=list()
		nodo_esquerdo.folha=self.folha
		nodo_direito.folha=self.folha
		self.folha=False
		nodo_esquerdo.raiz=False
		nodo_direito.raiz=False
		for i in self.array_chaves_offsets[:200] :
			nodo_esquerdo.array_chaves_offsets.append(i)
		for i in self.array_nodos[:meio+1]:
			nodo_esquerdo.array_nodos.append(i)
		for i in self.array_chaves_offsets[201:]:
			nodo_direito.array_chaves_offsets.append(i)
		for i in self.array_nodos[meio+1:]:
			nodo_direito.array_nodos.append(i)
		self.array_chaves_offsets= [self.array_chaves_offsets[meio]]
		nodo_esquerdo.numero_chaves = int(self.numero_chaves /2)
		nodo_direito.numero_chaves = int(self.numero_chaves /2 )
		self.numero_chaves = 1
		if(nodo_direito.numero_chaves == 0) or (nodo_esquerdo.numero_chaves == 0):
			#print("nodo direito ou esquerdo com numero_chaves errado")
			#print("nodo direito = "+ str(nodo_direito.numero_chaves)+ ", esquerdo = "+str(nodo_esquerdo.numero_chaves) )
			input()
		if(nodo_direito.numero_chaves != len(nodo_direito.array_chaves_offsets)):
			#print("split_raiz nodo direito com menos chave do que deveria!!!")
			#print("1 numero_chaves = "+str(nodo_direito.numero_chaves)+", tamanho ="+str(len(nodo_direito.array_chaves_offsets)))
			input()
		if(nodo_esquerdo.numero_chaves != len(nodo_esquerdo.array_chaves_offsets)):
			#print("split raiz nodo esquerdo com menos chaves do que deveria!!!")
			#print(" 1 numero_chaves = "+str(nodo_esquerdo.numero_chaves)+", tamanho ="+str(len(nodo_esquerdo.array_chaves_offsets)))
			input()
		#for i in self.array_chaves_offsets:
		#	#print(i)
		
		offset_esquerdo = nodo_esquerdo.Escreve_nodo_bin(-1)
		#print("offset_esquerdo ="+ str(offset_esquerdo))

		offset_direito = nodo_direito.Escreve_nodo_bin(-1)
		#print("offset_direito ="+ str(offset_direito))
		##print("WTF")
		self.array_nodos =list()
		if(offset_esquerdo == 0) or (offset_direito == 0):
			#print("offset da direita ou esquerda INVALIDO")
			#print("offset_direito = "+str(offset_direito)+", offset_esquerdo = "+str(offset_esquerdo))
			input()
		self.array_nodos.append(offset_esquerdo)
		self.array_nodos.append(offset_direito)
		#print('offset_esquerdo = '+str(offset_esquerdo)+'  e offset_direito = '+ str(offset_direito))
		self.folha=False
		self.numero_chaves=1
		self.raiz = True
		##print(self.folha)
		#input()
		self.Escreve_nodo_bin(0)
		#input()

	def split_node(self):
		#print(" ---  entra em split_node -----")
		meio = int(self.numero_chaves/2)
		nodo_esquerdo = nodo_btree(0, self.arquivo)
		nodo_direito = nodo_btree(0, self.arquivo)
		nodo_esquerdo.array_chaves_offsets=list()
		nodo_direito.array_chaves_offsets=list()
		for i in self.array_chaves_offsets[:200] :
			nodo_esquerdo.array_chaves_offsets.append(i)
		
		for i in self.array_chaves_offsets[201:]:
			nodo_direito.array_chaves_offsets.append(i)
		if not self.folha:
			for i in self.array_nodos[:meio]:
				nodo_esquerdo.array_nodos.append(i)
			for i in self.array_nodos[meio+1:]:
				nodo_direito.array_nodos.append(i)
		volta = self.array_chaves_offsets[meio]
		nodo_esquerdo.raiz= False
		nodo_direito.raiz=False
		nodo_esquerdo.folha=self.folha
		nodo_direito.folha=self.folha
		nodo_direito.numero_chaves=int(self.numero_chaves/2)
		nodo_esquerdo.numero_chaves=int(self.numero_chaves/2)
		if(nodo_direito.numero_chaves == 0) or (nodo_esquerdo.numero_chaves == 0):
			#print("split_node nodo direito ou esquerdo com numero_chaves errado")
			#print("nodo direito = "+ str(nodo_direito.numero_chaves)+ ", esquerdo = "+str(nodo_esquerdo.numero_chaves) )
			input()
		if(nodo_direito.numero_chaves != len(nodo_direito.array_chaves_offsets)):
			#print("split_node nodo direito com menos chave do que deveria!!!")
			#print("2 numero_chaves = "+str(nodo_direito.numero_chaves)+", tamanho ="+str(len(nodo_direito.array_chaves_offsets)))
			input()
		if(nodo_esquerdo.numero_chaves != len(nodo_esquerdo.array_chaves_offsets)):
			#print("split_node nodo esquerdo com menos chaves do que deveria!!!")
			#print("2 numero_chaves = "+str(nodo_esquerdo.numero_chaves)+", tamanho ="+str(len(nodo_esquerdo.array_chaves_offsets)))
			input()

		offset_direito = nodo_direito.Escreve_nodo_bin(self.offset)
		if(offset_direito != self.offset):
			print("ARQUIVO CORROMPIDO!!!!!!")
		self = nodo_direito
		offset_esquerda = nodo_esquerdo.Escreve_nodo_bin(-1)
		if(offset_esquerda==0):
			print("offset_esquerda INVALIDO")
			#print("offset_esquerda = "+str(offset_esquerda))
			#input()
		return (offset_esquerda,(volta))

	def Escreve_nodo_bin(self, offset):
		firstByte = 1
		#print("-- ENTRA EM Escreve_nodo_bin")
		#print("offset = "+ str(offset))


		#codificação de godel para bits se é folha e se é raiz
		if self.folha == True: 
			firstByte = firstByte*9
		
		if self.raiz: 
			firstByte = firstByte*4

		#firstByte = firstByte + 40
		
		##print(firstByte)
		##print("testando chaves "+str(self.numero_chaves))
		segunda_parte = struct.pack('h H I H', firstByte, self.ordem, self.offset, self.numero_chaves)
		impresoes_chaves = self.ordem*2 - self.numero_chaves
		zero = 0
		#print('é lista?')
		##print(isinstance(self, nodo_btree))
		##print(isinstance(self.array_chaves_offsets[0][0], int))
		##print(first(self.array_chaves_offsets))
		if(self.numero_chaves != len(self.array_chaves_offsets)):
			#print("numero_chaves é diferente do tamanho do array_chaves_offsets")
			#print("numero_chaves = "+str(self.numero_chaves)+"tamanho = "+ str(len(self.array_chaves_offsets)))
			input()
		if(self.array_chaves_offsets != None):
			chaves_bytes = struct.pack('I H', self.array_chaves_offsets[0][0], self.array_chaves_offsets[0][0])
			for k in self.array_chaves_offsets[1:]: #apenas pra testar
				if isinstance(k,bool):
					#print('algum elemento em array_chaves_offsets é bool mas nao deveria: '+ str(k))
					input()
			for interador in self.array_chaves_offsets[1:]: #
	   			chaves_bytes= chaves_bytes + struct.pack('I H', interador[0], interador[0])
		else:
			chaves_bytes= struct.pack('I H', zero, zero)
			impresoes_chaves=impresoes_chaves-1		
		#for i in self.array_chaves_offsets[1:]:
	   	#	chaves_bytes= chaves_bytes + struct.pack('I H', first(i), second(i))

		##print(chaves_bytes)

		#print('numero_chaves = '+ str(self.numero_chaves))
		#print(" ordem * 2 = " + str(self.ordem *2))
		#print('impresoes_chaves = '+str(impresoes_chaves))
		for i in range(impresoes_chaves):
	  		chaves_bytes= chaves_bytes + struct.pack('I H', zero, zero)

		if not self.folha :
	    		impresoes_nodos = self.ordem*2 +1 -(self.numero_chaves +1)
	    		nodos_bytes = struct.pack('I', self.array_nodos[0])
	    		for i in self.array_nodos[1:]:
	    				nodos_bytes =nodos_bytes+ struct.pack('I', i)
	    				#print("Escrevendo offsets de nodos, "+ str(i))
	    				if i == self.offset :
	    					#print('tentando escrever proprio offset como nodo!!')
	    					#print("offset propio = "+str(self.offset)+" ,offset tentando escrever = "+str(i))
	    					input()
	    		for i in range(impresoes_nodos):
	    				nodos_bytes = nodos_bytes +struct.pack('I', zero)

	    		#print(impresoes_nodos)
	    		#for i in range(self.ordem*2 +1):
	   			#		nodos_bytes= struct.pack('I', zero)
		else:
	   		nodos_bytes = struct.pack('I', zero)
	   		#print("Nodo Folha, Escrevendo nodos zero no arquivo")
	   		for i in range(self.ordem*2 ):
	   				nodos_bytes= nodos_bytes + struct.pack('I', zero)
		##print(size(chaves_bytes))
		string = self.arquivo
		b= bytes(string, 'utf-8')
		##print("first bute =")
		nome_arquivo = struct.pack('82s', b)
		btre_bytes = segunda_parte +chaves_bytes + nodos_bytes+nome_arquivo
		#print("segunda parte = " +str(len(segunda_parte)))
		#print("chaves_bytes = " +str(len(chaves_bytes)))
		#print("nodos_bytes = "+str(len(nodos_bytes)))
		#print("nome_arquivo="+ str(len(nome_arquivo)))
		

		if(offset<0):
			btre_file = open(self.arquivo,'ab')
			#print("abriu modo append")
			if( btre_file.tell() == 0):
				#print('modo append não funciona')
				input()
		else:
			btre_file = open(self.arquivo,'rb+')
			btre_file.seek(offset)
		if (self.raiz == False) and (btre_file.tell()== 0):
			#print('Esta tendendo escrever um nodo que não é raiz no espaço da raiz!!!')
			#print('offset = '+str(offset))
			input()
		offset_daEscrita = btre_file.tell()
		
		#print("o namoral  "+ str(btre_file.tell()) +"   tamanho btre_bytes" + str(len(btre_bytes)))
		if(len(btre_bytes) != 4096):
			#print("tamanho de registro INVALIDO")
			input()
		btre_file.write(btre_bytes)
		btre_file.close()
		if(offset_daEscrita <= -1):
			#print('offset_daEscrita INVALIDO , offset_daEscrita = '+str(offset_daEscrita))
			input()
		return offset_daEscrita
		##print(btre_bytes)

	def Busca_nodo_bin(self, offset, arquivo):
		#print("---- Entra em Busca_nodo_bin ---")
		#print("offset = "+ str(offset))
		btre_file= open('btree_matchs', 'rb+')
		btre_file.seek(offset)
		btre_bytes = btre_file.read(4096) #nao to afim de fazer a formula que calcula fodasse kkkkk
		btre_file.close()
		#print(len(btre_bytes))
		btre_variaveis = struct.unpack('h H I H', btre_bytes[:10])
		firstByte = btre_variaveis[0]
		self.ordem = btre_variaveis[1]
		self.offset = btre_variaveis[2]
		self.numero_chaves = btre_variaveis[3]
		

		##print(isinstance(self.numero_chaves, int))
		##print("btre_variaveis")
		##print(isinstance(self.numero_chaves, int))
		##print(btre_variaveis[3])
		#self.numero_chaves=3
		leitura_chaves = self.ordem*2 - self.numero_chaves
		self.array_chaves_offsets=list()
		if(self.numero_chaves == 0):
			self.array_chaves_offsets = list()
		else:
			for i in range(self.numero_chaves):
				chaves_offset = struct.unpack('I H',btre_bytes[10+(6*i):10+(6*i)+6])
				self.array_chaves_offsets.append((chaves_offset[0], chaves_offset[1]))

		### como faz pra ver folha agora??/
		#firstByte = firstByte -40
		##print('firstByte = '+str(firstByte))
		#input()
		if firstByte%3==0:
			self.folha= True
			##print("firstByte = "+str(firstByte)+ " folha True")
		else:
			self.folha=False
			##print('folha False')
			##print('travou folha!')
			#input()
		##print("marcador de meio de Busca_nodo_bin")
		if(firstByte%2 == 0):
			self.raiz= True
		else:
			self.raiz=False

		self.array_nodos=list()
		if not self.folha:
			nodo_offset = 10+ self.ordem*2*6
			nodo_offset_fim = nodo_offset + (self.numero_chaves +1)*4
			nodo_offset = struct.unpack(str(self.numero_chaves +1)+'I', btre_bytes[2410:2410+(self.numero_chaves+1)*4])
			##print("nao é folha")
			for i in nodo_offset:
				self.array_nodos.append(i)
				if(i ==0):
					print("tentando por offset da raiz em um nodo!")
					##print("offset a ser adicionado = " +str(i))
					##print(nodo_offset)
					#input()
		else:
			#print('eh folha')
			self.array_nodos = list()
		##print("/;???")
		##print(isinstance(self.numero_chaves, int))
				
	def consulta(self, offset,chave, arquivo):
		##print('--- Entrando em Consulta ----')
		nodo = nodo_btree(offset, arquivo)
		##print('voltando a Consulta')
		##print(nodo.array_chaves_offsets)
		for i in nodo.array_chaves_offsets:
			if isinstance(i,str):
				print('parou por que i é string mas não deveria, i= '+ str(i))
				#input()
		if isinstance(chave,str):
			print('chave é string, mas não deveria : chave = ' +str(chave))
			#input()
		pos = bisect_left(nodo.array_chaves_offsets, (chave, 0))
		##print("nodo é folha?"+ str(nodo.folha))
		if (pos == len(nodo.array_chaves_offsets)):
			if(nodo.folha):
				##print("Não achou em nodo Folha fim")
				return False
			else:
				##print("Não é folha, vai para o mais a direita")
				return nodo.consulta(nodo.array_nodos[-1],chave, arquivo)
		else:
			if nodo.array_chaves_offsets[pos][0] == chave:
				##print("achou e vai devolver offset")
				return second(nodo.array_chaves_offsets[pos])
			elif not nodo.folha:
				##print("não é folha, vai a posição = "+ str(pos)+ 'entre '+ str((nodo.array_chaves_offsets[pos-1], nodo.array_chaves_offsets[pos]) ))
				return nodo.consulta(nodo.array_nodos[pos],chave, arquivo)
			else:
				##print("Não achou em nodo Folha meio")
				return False


		



def first( tupla):
	
	return tupla[0]

def second(tupla):
	return tupla[1]

btree_matchs= "btree_matchs"



raiz = nodo_btree(0, btree_matchs)
#raiz.raiz =True
#raiz.Folha = Ture
'''
#print("inicio")
for i in raiz.array_chaves_offsets:
	#print(i)
#print("inicio1")
raiz.insert_raiz(raiz, 33, 6,btree_matchs)
for i in raiz.array_chaves_offsets:
	#print(i)
#print("inicio2")
raiz.insert_raiz(raiz, 55, 6,btree_matchs)
for i in raiz.array_chaves_offsets:
	#print(i)
#print("inicio3")
raiz.insert_raiz(raiz, 66 , 6,btree_matchs)
for i in raiz.array_chaves_offsets:
	#print(i)
#print("inicio3")
raiz.insert_raiz(raiz, 40 , 6,btree_matchs)
#print( "fim das insercoes")
for i in raiz.array_chaves_offsets:
	#print(i)

raiz.insert_raiz(raiz, 15 , 6,btree_matchs)
#print("testando filho esquerda")
#filho_esquerda = raiz.array_nodos[0]
#for i in filho_esquerda.array_chaves_offsets:
	##print(i)
#print("testando filho direita")
raiz.insert_raiz(raiz, 57 , 6,btree_matchs)
#filho_esquerda = raiz.array_nodos[1]
#for i in filho_esquerda.array_chaves_offsets:
#	#print(i)
#print("inicio3")
'''

'''
for i in raiz.array_chaves_offsets:
	#print(i)

nodo = nodo_btree(0, btree_matchs)
#print(nodo.raiz)
travador = raiz.consulta(0,6000,btree_matchs)
#print("offset procurado = "+ str(travador))
#print("vai #printar tamanho da do array_chaves_offsets da raiz = ")
#print(len(raiz.array_chaves_offsets))
#print(raiz.array_chaves_offsets)
#for i in range(1,500):
	#travador = raiz.consulta(0,i,btree_matchs)
#	#print('procurando = ' + str(i))
	#if travador :
	#	input()

	##print("procurando o valor  = " + str(i))
#	#print(travador)
#nodo =nodo_btree(raiz.array_nodos[0],btree_matchs)


raiz.numero_chaves =0
raiz.folha = True
raiz.raiz = True
raiz.array_chaves_offsets = None
raiz.array_nodos = list()
raiz.ordem = 200
#print("escreve vazio")
raiz.Escreve_nodo_bin(0)
nodo = nodo_btree(0, btree_matchs)
#print('ta fumado só pode')
#print(nodo.raiz)
'''
