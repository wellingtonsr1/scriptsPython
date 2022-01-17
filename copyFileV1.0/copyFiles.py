#!/usr/bin/env python3

'''
Nome: copyFiles.py
Versão: 1.1
Autor: wellington
'''

import os
import shutil
import sys

def help():
    print("+", '-' * 65, "+")
    print('| Uso:                                                              |')
    print('|     Com o script dentro da mesma pasta dos arquivos, execute:     |')
    print('|                                                                   |')
    print('|            python3 copyFiles.py mp3,mp4,pdf,txt                   |')
    print('|                           ou                                      |')
    print('|            ./copyFiles.py  mp3,mp4,pdf,txt                        |')
    print("+",'-' * 65,"+")

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
                    if not os.path.exists(destination):
                        os.mkdir(destination)
                    shutil.copy(filename, destination)
                    size += 1

    [print('Arquivos copiados!') if size != 0 else print('Nenhum arquivo foi copiado!')]
                                                      
if __name__ == '__main__':
    main()

