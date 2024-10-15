import sys
import math
import random



def show_matrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			print ( matrix[i][j], end = "\t")
		print()

abc = "abcdefghijklomnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚáéíóú"
abc2 = "abcdefghijklomnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚáéíóú1234567890"

abecedario = {
	'a': 0,
	'A': 0,
	'á': 0,
	'Á': 0,
	'b': 1,
	'B': 1,
	'c': 2,
	'C': 2,
	'd': 3,
	'D': 3,
	'e': 4,
	'E': 4,
	'é': 4,
	'É': 4,
	'f': 5,
	'F': 5,
	'g': 6,
	'G': 6,
	'h': 7,
	'H': 7,
	'i': 8,
	'I': 8,
	'í': 8,
	'Í': 8,
	'j': 9,
	'J': 9,
	'k': 10,
	'K': 10,
	'l': 11,
	'L': 11,
	'm': 12,
	'M': 12,
	'n': 13,
	'N': 13,
	'ñ': 14,
	'Ñ': 14,
	'o': 15,
	'O': 15,
	'ó': 15,
	'Ó': 15,
	'p': 16,
	'P': 16,
	'q': 17,
	'Q': 17,
	'r': 18,
	'R': 18,
	's': 19,
	'S': 19,
	't': 20,
	'T': 21,
	'u': 21,
	'U': 21,
	'ú': 21,
	'Ú': 21,
	'v': 22,
	'V': 22,
	'w': 23,
	'W': 23,
	'x': 24,
	'X': 24,
	'y': 25,
	'Y': 25,
	'z': 26,
	'Z': 26
}

convert_abecedario = {
	0: 'A',
	1: 'B',
	2: 'C',
	3: 'D',
	4: 'E',
	5: 'F',
	6: 'G',
	7: 'H',
	8: 'I',
	9: 'J',
	10: 'K',
	11: 'L',
	12: 'M',
	13: 'N',
	14: 'Ñ',
	15: 'O',
	16: 'P',
	17: 'Q',
	18: 'R',
	19: 'S',
	20: 'T',
	21: 'U',
	22: 'V',
	23: 'W',
	24: 'X',
	25: 'Y',
	26: 'Z'
}



def decifrado_cesar(text, key):
	new_text = ""
	for i in range(len(text)):
		if text[i] in abc:
			aux = abecedario[text[i]]
			aux += key
			if aux > 26:
				aux -= 27
			if aux < 0:
				aux += 27
			new_text = new_text+convert_abecedario[aux]
		else:
			new_text = new_text + text[i]
	return new_text

def decifrado_atbash(text):
	new_text = ""
	for i in range(len(text)):
		if text[i] in abc:
			aux = abecedario[text[i]]
			aux = 26-aux
			new_text = new_text+convert_abecedario[aux]
		else:
			new_text = new_text + text[i]
	return new_text


def gen_rejilla(size):
	rejilla = []
	rejaux = []
	for i in range(size):
		aux = []
		aux2 = []
		for j in range(size):
			aux.append(0)
			aux2.append(0)
		rejilla.append(aux2)
		rejaux.append(aux)

	

	count = 1

	for i in range(size//2):
		for j in range(size//2):
			rejaux[i][j] = count
			count+=1

	count = 1

	for i in range(size-1, size//2-1,-1):
		for j in range(size//2):
			rejaux[j][i] = count
			count += 1

	count = 1

	for i in range(size-1,size//2-1,-1):
		for j in range(size-1,size//2-1,-1):
			rejaux[i][j] = count
			count += 1

	count = 1

	for j in range (size//2):
		for i in range(size-1,size//2-1,-1):
			rejaux[i][j] = count
			count += 1

	listed = []

	for i in range((size//2)*(size//2)):
		listed.append(random.randint(1,4))

	for i in range(size//2):
		for j in range(size//2):
			if listed[rejaux[i][j]-1] == 1:
				rejilla[i][j] = 1

	for i in range(size-1, size//2-1,-1):
		for j in range(size//2):
			if listed[rejaux[j][i]-1] == 2:
				rejilla[j][i] = 1

	for i in range(size-1,size//2-1,-1):
		for j in range(size-1,size//2-1,-1):
			if listed[rejaux[i][j]-1] == 3:
				rejilla[i][j] = 1

	for j in range (size//2):
		for i in range(size-1,size//2-1,-1):
			if listed[rejaux[i][j]-1] == 4:
				rejilla[i][j] = 1

	return rejilla




def girar_rejilla(rejilla):
	new_rejilla = []
	for i in range(len(rejilla)-1, -1, -1):
		aux = []
		for j in range(len(rejilla)):
			aux.append(rejilla[j][i])
		new_rejilla.append(aux)
	return new_rejilla


def cifrado_rejilla(text):
	raw_text = ""
	for i in range(len(text)):
		if text[i] in abc2:
			raw_text= raw_text+text[i]
	size = math.ceil(math.sqrt(len(raw_text)))
	if size%2 == 1:
		size+=1
	for i in range((size*size)-len(raw_text)):
		raw_text= raw_text+convert_abecedario[random.randint(0,26)]

	rejilla = gen_rejilla(size)

	print("TEXTO CRUDO:\n\n")
	print(raw_text,end="\n\n")

	encrypted = ""
	print("REJILLA GENERADA\n\n")

	show_matrix(rejilla)

	for k in range(4):
		for i in range(len(rejilla)):
			for j in range(len(rejilla)):
				if (rejilla[i][j]) == 1:
					encrypted = encrypted+raw_text[i*size+j]
		rejilla = girar_rejilla(rejilla)

	print("TEXTO ENCRIPTADO:\n\n")

	return encrypted




text = "wikyvmheh iq gsptyxegmsq"
print("DECIFRADO CESAR CON 4 POSICIONES\n\n")
print("texto original: ",end=" ")
print(text,end="\n\n")
print("texto decifrado: ",end=" ")
print(decifrado_cesar(text,-4),end = "\n\n\n")


text = "hvtfirwzw vn xlnkfgzxrln"
print("DECIFRADO ATBASH\n\n")
print("texto original: ",end=" ")
print(text,end="\n\n")
print("texto decifrado: ",end=" ")
print(decifrado_atbash(text),end = "\n\n\n")

text = "La norma ISO 27799 es una guía esencial para garantizar la seguridad de la información en el sector de la atención médica."
print("CIFRADO POR REJILLAS\n\n")
print("texto original: ",end=" ")
print(text,end="\n\n")
print (cifrado_rejilla(text))

