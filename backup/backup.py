#! python3

#+--------------------------------------------------Descrição-------------------------------------------------------+
#| - Copia os arquivos das pastas (Desktop, Documents e Downloads) dos usuários que tenham pelo menos um arquivo    |
#|   em qualquer uma delas.     		                                                                            |
#+----------------------------------------------------Autor---------------------------------------------------------+
#| - Wellington        									         	                                                |
#+----------------------------------------------Sistemas testados---------------------------------------------------+
#| - Windows 10(x64)		                    				 		                                            |
#+-------------------------------------------------IMPORTANTE-------------------------------------------------------+
#| - Precisa ser salvo na unidade C:\	                                                                            |
#| - Executar o 'backup.bat'                                                                                        |
#| - Executar como administrador                                                                                    |								               
#+------------------------------------------------------------------------------------------------------------------+


import os, shutil, socket
from datetime import datetime

root = 'c:\\users'
currentDate = datetime.today().strftime('%d-%m-%Y')
pathBackup = 'C:\\bkp_'+socket.gethostname()+'_'+currentDate
extList = ['.pdf', '.docx', '.xlsx', '.odt']
fileDirectory = 'Arquivos_'

def header():
    print("-=-" * 30)
    print("Iniciando o backup...".center(40), end='')
    print("Máquina: " + socket.gethostname().ljust(20), end='')
    print("Data: " + currentDate.ljust(30))
    print("-=-" * 30)
    print()

def foot(pathBkp):
    print()
    print("-=-" * 30)
    print('Backup realizado. Verifique os arquivos em '.rjust(50) + pathBkp)  
    print()     

def main():  
    header()
    
    for userFolder in [userFolders for userFolders in os.listdir(root)]:
        fullPathBackup = os.path.join(pathBackup, userFolder)
        for folder, subfolders, files in os.walk(os.path.join(root, userFolder)):
            for file in files:
                pathFile = os.path.join(folder, file)
                
                for ext in extList:
                    fileDirectoryByExt = fileDirectory+ext.replace('.', '')
                    if file.endswith(ext):
                        if not os.path.exists(os.path.join(fullPathBackup, fileDirectoryByExt)):
                            os.makedirs(os.path.join(fullPathBackup, fileDirectoryByExt))
                            
                        print('Adicionando [%s] na pasta [%s] em [%s]' % (file, fileDirectoryByExt, userFolder))
                        shutil.copy(pathFile, os.path.join(fullPathBackup+'\\'+fileDirectoryByExt, file))
                    continue

    foot(pathBackup)
                        
                
 
 
if __name__ == '__main__':
    main()



  
   