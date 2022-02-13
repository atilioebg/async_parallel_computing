import multiprocessing

"""
Esta é uma função que mostra como enviar dados entre processos independentes, ou
seja fazendo a conexão entre processos distintos através do QUEUE. O QUEUE permite
melhor gerenciar processos através do lock/unlock.
"""

def ping(queue):
    # envia o dado 'Geek' com o conn.send
	queue.put('Geek')
	

def pong(queue):
    # recebe o dado 'Geek' com o conn.recv
	msg = queue.get()
	print(f'{msg} University')
	

def main():
	# criando um cano (pipe) e ele retona as duas saidas (pontas) do cano
	# o true é pasa indicar que conn. tanto pode enviar como receber
	queue = multiprocessing.Queue()
	
	# fazendo a comunicacao entre processos, coisa que inicialmente nao tem
	# P1 cria um process que usa ping para enviar um dados
	p1 = multiprocessing.Process(target=ping, args=(queue,))
	# P2 cria um processo que recebe dados de P1 via pong
	p2 = multiprocessing.Process(target=pong, args=(queue,))
	
	# Envia para o pool de processamento
	p1.start()
	p2.start()
	
	# Executa ccada processoa até finalizar
	p1.join()
	p2.join()
	

if __name__ == '__main__':
	main()