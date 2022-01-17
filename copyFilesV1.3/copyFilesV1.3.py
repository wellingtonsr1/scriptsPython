#!/usr/bin/env python3

'''
Nome: copyFiles.py
Versão: 1.3

Autor: wellington

Data: 24/05/2020

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
from progressbar import *

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
    print("+", '-' * 65, "+")
    print('| Uso:                                                              |')
    print('|     Com o script dentro da mesma pasta dos arquivos, execute:     |')
    print('|                                                                   |')
    print('|            python3 copyFiles.py mp3,mp4,pdf,txt                   |')
    print('|                           ou                                      |')
    print('|            ./copyFiles.py  mp3,mp4,pdf,txt                        |')
    print("+",'-' * 65,"+")
    #os.system('pause > NULL' if os.name == 'nt' else 'continue')

def main():
    size = 0

    if len(sys.argv[1:]) != 1:
        help()
        return
    else:
        fileType = sys.argv[1]
        namedir = 'Arquivos_'
       
        for extensao in fileType.split(','): 
            destination = namedir+extensao.upper()
            for filename in os.listdir():
                if os.path.isfile(filename) and filename.endswith('.'+extensao):
                    limparTela()
                    print('Copiando para \'{}\''.format(destination))
                    if not os.path.exists(destination):
                        os.mkdir(destination)
                        dirlist.append(destination)
                    try:
                        shutil.copy(filename, destination)
                        size += 1
                        barraprogresso(size)
                    except Exception:
                        print('Houve um erro durande o progresso.')
                        #os.system('pause > NULL' if os.name == 'nt' else 'continue')
                        
    resumo(size)   

if __name__ == '__main__':
    main()

