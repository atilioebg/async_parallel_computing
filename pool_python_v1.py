import multiprocessing 
"""
Criando um multiprocesso com 2 vezes o número de cores do pc
""" 

def calcular(dado):
    return dado ** 2

    
def main():
    # Tamanho da pool, será 2 (threads) * número de núcleos
    tamanho_do_pool = multiprocessing.cpu_count()*2

    print(f'Tamanho da pool: {tamanho_do_pool}')

    # configurando o número de processos na pool
    pool = multiprocessing.Pool(processes=tamanho_do_pool)
    
    # Dados de entrada a serem processados
    entradas = list(range(10))
    
    # Passando as entradas para serem processadas com o map
    saidas = pool.map(calcular, entradas)
    
    print(f'Saídas: {saidas}')

    # O close, diferente do start, manda executar os processor
    pool.close()
    # Executa ccada processoa até finalizar
    pool.join()
    
    
if __name__ == '__main__':
    main()
