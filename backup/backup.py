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
extList = ['.pdf', '.docx', '.xlsx', '.odt', '.ods']
fileDirectory = 'Arquivos_'

def header():
    print("-=-" * 30)
    print("Iniciando o backup...".center(40), end='')
    print("Máquina: " + socket.gethostname().ljust(20), end='')
    print("Data: " + currentDate.ljust(30))
    print("-=-" * 30)
    print()

def foot():
    print()
    print("-=-" * 30)
    print('Backup realizado. Verifique os arquivos em '.rjust(50) + pathBackup)  
    print()    

def main():  
    header()
    
    # Lista as pastas dos usuários em 'C:\Users'
    for userFolder in [userFolders for userFolders in os.listdir(root)]:
        fullPathBackup = os.path.join(pathBackup, userFolder)

        # Varre a árvore de diretórios a partir de 'C:\Users\pastaUsuário'
        for folder, subfolders, files in os.walk(os.path.join(root, userFolder)):
            for file in files:
                origin = os.path.join(folder, file)
                for ext in extList:
                    fileDirectoryByExt = fileDirectory+ext.replace('.', '')
                    if file.endswith(ext):
                        backupFolder = os.path.join(fullPathBackup, fileDirectoryByExt)
                        if not os.path.exists(backupFolder):
                            os.makedirs(backupFolder)

                        destination = os.path.join(backupFolder, file) 
                        print('Adicionando [%s] na pasta [%s] em [%s]' % (file, fileDirectoryByExt, userFolder))
                        shutil.copy(origin, destination)

                    continue

    foot()
    print('Pressione ENTER pra continuar.')
    os.system('pause > NULL') 
                                
 
 
if __name__ == '__main__':
    main()



  
   