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

root = 'C:\\users'
drive = 'C:\\'
currentDate = datetime.today().strftime('%d-%m-%Y')
backupFolder = 'bkp_'+socket.gethostname()+'_'+currentDate
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
    print('Backup realizado. Verifique os arquivos em {}'.rjust(50).format(os.path.join(drive, backupFolder)))
    print()    

def main():  
    header()
    
    # Lista as pastas dos usuários em 'C:\Users'
    for userFolder in [userFolders for userFolders in os.listdir(root)]:
        # C:\\bkp_NomeMaquina_dataBackup\pastaUsusario
        pathBackupFolder = os.path.join(os.path.join(drive, backupFolder), userFolder)

        # Varre a árvore de diretórios a partir de 'C:\Users\pastaUsuário'
        for folder, subfolders, files in os.walk(os.path.join(root, userFolder)):
            for file in files:
                origin = os.path.join(folder, file)
                for ext in extList:
                    # Cria o diretório 'Arquivos_pdf', 'Arquivos_docx' etc
                    fileDirectoryByExt = fileDirectory+ext.replace('.', '')
                    if file.endswith(ext):
                        # Cria 'C:\\bkp_NomeMaquina_dataCriaçãoBackup\pastaUsusário\Arquivos_EXT'
                        fullBackupFolder = os.path.join(pathBackupFolder, fileDirectoryByExt)
                        if not os.path.exists(fullBackupFolder):
                            os.makedirs(fullBackupFolder)

                        destination = os.path.join(fullBackupFolder, file) 
                        print('Adicionando [{}] na pasta [{}] em [{}]'.format(file, fileDirectoryByExt, userFolder))
                        shutil.copy(origin, destination)

                    continue

    foot()
    print('Pressione ENTER pra continuar.')
    os.system('pause > NULL') 
                                
 
 
if __name__ == '__main__':
    main()



  
   