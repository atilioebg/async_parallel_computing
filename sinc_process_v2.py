import multiprocessing

"""
Esta função mostra a solução para o problema de sincronia nos multiprocessos
uma vez que varios processos tentam acessar o mesmo dado, causando
o conhecido "race condition"
"""

# Neste código está a correção de sincronia, usando o lock. Para isso basta 
# passar o lock para os métodos e realizado dentro de um contexto
def depositar(saldo, lock):
    for _ in range(10000):
        with lock:
            # o.value é o valor compartilhado entre os processos
            value = saldo.value + 1 


def sacar(saldo, lock):
    for _ in range(10000):
        with lock:
            # o .value é o valor compartilhado entre os processos
            value = saldo.value - 1 


def realizar_transacoes(saldo, lock):
	
	# criando os processos
	pc1 = multiprocessing.Process(target=depositar, args=(saldo,lock))
	pc2 = multiprocessing.Process(target=sacar, args=(saldo,lock))
	
	pc1.start()
	pc2.start()
	
	pc1.join()
	pc2.join()
	
if __name__=='__main__':
	
    # inciando a variável a ser compartilhada
    saldo = multiprocessing.Value('i', 100)

    # vamos instanciar o lock aqui,usando o Rlockpara evitar o starvation
    lock = multiprocessing.RLock()
	
    print(f'Saldo Inicial: {saldo.value}')
	
    for _ in range(10):
        realizar_transacoes(saldo, lock)
	
    print(f'Saldo final: {saldo.value}')
	