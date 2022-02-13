import multiprocessing
import time

"""
Este programa mostra como usar a abstração em threads e multiprocessing, pois
isto permite alternar entre estes 2 métodos apenas mudando a importacao da lib usada,
uma vez que as linhas de comando que executam estas 2 coisas são muito similares.
"""

def processar():
    print('[', end='', flush=True)
    for _ in range(1, 11):
        print('#', end='', flush=True)
        time.sleep(1)
    print(']', end='', flush=True)
	

if __name__ == '__main__':

	# instanciando 1 threading
	ex = multiprocessing.Process(target=processar)
	
	ex.start()
	ex.join()