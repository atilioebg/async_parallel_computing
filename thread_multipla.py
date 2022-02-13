import threading
import time

def main():
    
    threads = [
               threading.Thread(target=contar, args=('elefante', 10)),
               threading.Thread(target=contar, args=('buraco', 5)),
               threading.Thread(target=contar, args=('dinheiro', 20)),
               threading.Thread(target=contar, args=('pato', 25))
               ]
    
    
    
    [th.start() for th in threads]  # instancia no pool de espera
    
    print("Segue executanto outros comandos")
    print("XXXXXXXXXXXXX")
    
    [th.join() for th in threads] # aguarda executar
    
    print("Executada a thread")
    

def contar (o_que, numero):
    
    for n in range (1, numero + 1):
        print(f'{n} {o_que}(s)...')
        time.sleep(1)
        
if __name__=='__main__':
    main()
