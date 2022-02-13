import multiprocessing

"""
Esta função mostra o problema de sincronia nos multiprocessos
uma vez que varios processos tentam acessar o mesmo dado, causando
o conhecido "race condition"
"""

def depositar(saldo):
	for _ in range(10000):
		# saldo.value é o valor compartilhado entre os processos
		saldo.value = saldo.value + 1 


def sacar(saldo):
	for _ in range(10000):
		# saldo.value é o valor compartilhado entre os processos
		saldo.value = saldo.value - 1 


def realizar_transacoes(saldo):
	
	# criando os processos
	pc1 = multiprocessing.Process(target=depositar, args=(saldo,))
	pc2 = multiprocessing.Process(target=sacar, args=(saldo,))
	
	pc1.start()
	pc2.start()
	
	pc1.join()
	pc2.join()
	
if __name__=='__main__':
	
	# inciando a variável a ser compartilhada
	saldo = multiprocessing.Value('i', 100)
	
	print(f'Saldo Inicial: {saldo.value}')
	
	for _ in range(10):
		realizar_transacoes(saldo)
	
	print(f'Saldo final: {saldo.value}')
	