import time
# from concurrente.features.thread import ThreadPoolExecutor as Executor
from concurrent.futures.process import ProcessPoolExecutor as Executor


"""
Este programa mostra como usar a abstração em threads e multiprocessing, pois
isto permite alternar entre estes 2 métodos apenas mudando a importacao da lib usada,
uma vez que as linhas de comando que executam estas 2 coisas são muito similares.
Para mudar entre thread e process e só comentar e/ou descomentar as importaçoes.
"""

def processar(param):
    print(f'Só testando a passagem de {param} na função.')
    print('[', end='', flush=True)
    for _ in range(1, 11):
        print('#', end='', flush=True)
        time.sleep(1)
    print(']', end='', flush=True)
    return 42
	

if __name__ == '__main__':

    with Executor() as executor:
        future = executor.submit(processar, 'parametro de teste')
    print(f'O retorno foi {future.result()}.')
        