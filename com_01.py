import multiprocessing
import random

"""
Esta é uma função que mostra como enviar dados entre processos independentes, ou
seja fazendo a conexão entre processos distintos através do PIPE. O PIPE não 
permite muita gerência de processos, ou seja, não temos o lock/unlock como no
queue.
"""

def ping(conn):
    # envia o dado 'Geek' com o conn.send
	conn.send('Geek')
	

def pong(conn):
    # recebe o dado 'Geek' com o conn.recv
	msg = conn.recv()
	print(f'{msg} University')
	

def main():
	# criando um cano (pipe) e ele retona as duas saidas (pontas) do cano
	# o true é pasa indicar que conn. tanto pode enviar como receber
	conn1, conn2 = multiprocessing.Pipe(True)
	
	# fazendo a comunicacao entre processos, coisa que inicialmente nao tem
	# P1 cria um process que usa ping para enviar um dados
	p1 = multiprocessing.Process(target=ping, args=(conn1,))
	# P2 cria um processo que recebe dados de P1 via pong
	p2 = multiprocessing.Process(target=pong, args=(conn2,))
	
	# Envia para o pool de processamento
	p1.start()
	p2.start()
	
	# Executa ccada processoa até finalizar
	p1.join()
	p2.join()
	

if __name__ == '__main__':
	main()