import multiprocessing
import time
import ctypes

"""
Esta é uma função que faz os dados serem compartilhados entre os estado (memória),
diferente do que foi visto no PIPE onde os dados estão em memórias diferentes mas
se comunicam.
Para isso importamos a lib ctypes e para alterar a variavél/array compartilhado
devemos colocar .value após a variável em comum, ou .array (que neste caso deve
ser de 1 unico tipo, ou tudo int, ou float ou str).
"""

# essa função recebe um valor e um status e 
# executa um if conforme o status (stat) de entrada
def funcao1(val, stat):
	if stat.value:
		res = val.value + 10
		stat.value = False
	else:
		res = val.value + 20
		val.value = 200
		stat.value = True
	
	print(f'O resultado da função 1 é {res}.')
	time.sleep(0.001)
	
	
def funcao2(val, stat):
	if stat.value:
		res = val.value + 30
		stat.value = False
	else:
		res = val.value + 40
		val.value = 400
		stat.value = True
	
	print(f'O resultado da função 2 é {res}.')
	time.sleep(0.001)


def main():
    
    # Aqui temos as principais mudanças para o compartilhamento
    # devemos inicializar a variável e/ou o array, que neste caso
    # é inicializada com o tipo c_type 'i' de inteiros, e valor 100
	valor = multiprocessing.Value('i', 100)
    # Inicializada com o tipo c_type 'ctypes.b_bool' de boleano e valor False
	status =  multiprocessing.Value(ctypes.c_bool, False)
	
	# criando os processos
	# em p1 passamos a funcao1 com as variáveis acima
	p1 = multiprocessing.Process(target=funcao1, args=(valor, status))
	# em p2 passamos a funcao2 com as variáveis acima
	p2 = multiprocessing.Process(target=funcao2, args=(valor, status))
	
	# Enviamos para o pool
	p1.start()
	p2.start()
	
	# Esperamos executar o processos
	p1.join()
	p2.join()
	
if __name__ == '__main__':
	main()