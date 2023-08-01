import sys
import re

# Compara el contenido de dos archivos, para buscar que hay en el primero y el segundo
# asi mismo muestra lo que hay en el primero y NO en el segundo

def main():
	a = sys.argv[1]
	b = sys.argv[2]
	compare(a,b)


def compare(A,B):
	#leer el contenido de los archivos
	with open(A, 'r') as a:
		lines_A = set(a.read().splitlines())

	with open(B, 'r') as b:
		lines_B = set(b.read().splitlines())

	#Obtenemos las lineas de A que esten contenidas en B
	inter = lines_A.intersection(lines_B)
	# Obtener las lineas de A que NO esten en B
	diff = lines_A.difference(lines_B)
	#mostrar los resultados
	p = '[\w-]+?(?=\.)'
	# This pattern is divided into 3 patterns
	#[\w] matches the words inside the set
	#+? matches the string if it’s present only once before ? keyword
	#(?=) matches all characters without newline and make sure to stop at.
	f1 = re.search(p, a.name)
	f2 = re.search(p, b.name)
	print(f"Lineas de {f1.group()} en {f2.group()}\n")
	for l in inter:
		print(f'{l}')

	print(f'Lineas de {f1.group()} que NO estan en {f2.group()}\n')
	for l in diff:
		print(l)


if __name__ == '__main__':
	main()
