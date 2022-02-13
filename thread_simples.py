import threading
import time
"""
NÚMERO DE THREADS, NUCLEOS E NUCLEOS FÌSICOS POR PROCESSADOR: 
    import psutil
    
    # “logical CPUs” means the number of physical cores multiplied by the number of threads that can run on each core
    
    # Number of physical cores
    physical_cores = psutil.cpu_count(logical = False)
    
    # Number of cores (physical and not physical)
    cores = psutil.cpu_count(logical = True)
    
    # Number of threads per core
    threads_count = psutil.cpu_count() / psutil.cpu_count(logical=False)

NÚMERO DE NUCLEOS:
    import multiprocessing
    multiprocessing.cpu_count()
"""

def main():
    th = threading.Thread(target=contar, args=('elefante', 10))
    
    th.start() # instancia no pool de espera
    
    print("Segue executanto outros comandos")
    print("XXXXXXXXXXXXX")
    
    th.join() # aguarda executar
    
    print("Executada a thread")
    

def contar (o_que, numero):
    
    for n in range (1, numero + 1):
        print(f'{n} {o_que}(s)...')
        time.sleep(1)
        
if __name__=='__main__':
    main()
