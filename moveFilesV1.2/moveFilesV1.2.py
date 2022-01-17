#!/usr/bin/env python3

'''
Nome: moveFiles.py
Versão: 1.2

Data: 24/05/2020

Autor: wellington

Barra de progresso retirada de: 'https://wiki.python.org.br/BarraProgresso'

Criado usando:
    Python 3.7.3 64-bit
    Visual Studio Code, Versão: 1.45.0

Testado nos Sistemas Operacionais:
    Linux debian 10, Codenome: Buster, Arquitetura: x86_64
    Microssoft Windows 8.1, Arquitetura: 32 bits
'''

import os
import shutil
import sys
from pathlib import Path
from progressbar import *
from tqdm import tqdm
from time import sleep

extlist = []
filelist = []
dirlist = []

def barraprogresso(i):
    widgets = ['Arquivo: {} '.format(i), Percentage(), ' ', Bar(marker=RotatingMarker()),' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=20000000).start()
    for i in range(2000000):
        pbar.update(10*i+1)
    pbar.finish()

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def resumo(s):
    limparTela()
    print("+", '-' * 60, "+")   
    print('|   {:^57}  |'.format('R E S U M O '))  
    print("+", '-' * 60, "+")                        
    [print('\n {} Arquivos movidos para o(s) seguinte(s) diretório(s):    '.format(s)) if s != 0 else print('   {:^57}  '.format('Nenhum arquivo foi movido!'))]
    for d in dirlist:
        print('\t{}                                        '.format(d))
    print("\n+", '-' * 60, "+")
    #os.system('pause > NULL' if os.name == 'nt' else 'continue')

def help():
    print("+", '-' * 62, "+")
    print('| Uso:                                                           |')
    print('|   Com o script dentro da mesma pasta dos arquivos, execute:    |')
    print('|                                                                |')
    print('|       \'python3 moveFiles.py\' ou \'./moveFiles.py\'               |')
    print('|                                                                |')
    print("+",'-' * 62,"+") 
    #os.system('pause > NULL' if os.name == 'nt' else 'continue')  

def main():
    size = 0

    if len(sys.argv[1:]) > 0:
        help()
        return
    else:
        # Cria duas listas, uma com o nome completo e outra com a extenão dos arquivos
        for filenameExtensao in os.listdir():  
            name, extensao = os.path.splitext(filenameExtensao)
            extlist.append(extensao[1:])
            filelist.append(filenameExtensao)

        for ext in extlist:
            destination = 'Arquivos_'+ext.upper()
            for filename in filelist: 
                if os.path.isfile(filename) and filename.endswith('.'+ext) and not filename.endswith('.py') and not filename == 'moveFiles.bat':
                    limparTela()
                    print('Movendo para \'{}\''.format(destination))
                    if not os.path.exists(destination):
                        os.mkdir(destination)
                        dirlist.append(destination)
                    try:
                        shutil.move(filename, destination)
                        size += 1
                        barraprogresso(size)
                    except Exception:
                        print('Houve um erro durande o progresso.')
                        #os.system('pause > NULL' if os.name == 'nt' else 'continue')

    resumo(size)
    
if __name__ == '__main__':
    main()