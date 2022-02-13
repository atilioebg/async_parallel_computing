import multiprocessing
import time

"""
Esta é uma função que mostra que os processos não compartilham estado (memória)
"""

# essa função recebe um valor e um status e 
# executa um if conforme o status (stat) de entrada
def funcao1(val, stat):
	if stat:
		res = val + 10
		stat = False
	else:
		res = val + 20
		val = 200
		stat = True
	
	print(f'O resultado da função 1 é {res}.')
	time.sleep(0.001)
	
	
def funcao2(val, stat):
	if stat:
		res = val + 30
		stat = False
	else:
		res = val + 40
		val = 400
		stat = True
	
	print(f'O resultado da função 2 é {res}.')
	time.sleep(0.001)


def main():

	valor = 100
	status = False
	
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