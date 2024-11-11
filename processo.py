import psutil

'''
    Localizar todos os processos em execução do elementclient
'''

def listar_processos():
    for processo in psutil.process_iter(['pid', 'name']):
        if 'elementclient' in processo.info['name'].lower():
            print(f"Processo: {processo.info['name']}, PID: {processo.info['pid']}")

listar_processos()
