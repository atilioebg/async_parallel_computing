import multiprocessing 
"""
Criando um único processo
"""

print(F'Iniciando o processo com o nome: {multiprocessing.current_process().name}')


def faz_algo(valor):
    print(f'Fazendo algo com o {valor}.')
    
    
def main():
    # criando uma processo
    pc = multiprocessing.Process(target=faz_algo, args=('passaro',))
    print(f'Iniciando o processo com o nome: {pc.name}')

    # Coloca o processo na pool de execução
    pc.start()
    
    # Aguarda até o processo ser finalizado
    pc.join()
    
if __name__ == '__main__':
    main()
