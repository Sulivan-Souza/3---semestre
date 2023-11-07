





import os
import sys
import socket

def main():
    os.system('clear')
    print('''\033[1;32m
    =========================================================
    |                                                       |
    |       Verificador de disponibilidade de máquinas      |
    |                                                       |
    =========================================================
    ''')
    print('\033[1;37m')
    host = input('Digite o endereço IP ou URL: ')
    port = int(input('Digite a porta: '))
    print('\033[1;37m')
    print('Verificando...')
    print('\033[1;37m')
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((host, port))
        print('A máquina está funcionando!')
        s.close()
    except:
        print('A máquina não está funcionando!')
        sys.exit()
        
if __name__ == '__main__':
    main()