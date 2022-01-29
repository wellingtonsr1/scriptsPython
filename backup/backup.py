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
from time import sleep


root = 'C:\\users'
currentDate = datetime.today().strftime('%d-%m-%Y')
backupFolder = 'bkp_'+socket.gethostname()+'_'+currentDate
extList = ['.pdf', '.docx', '.xlsx', '.odt', '.ods']
fileDirectory = 'Arquivos_'

def header(statusMessage):
    print("-=-" * 30)
    print("Status: {}".center(25).format(statusMessage), end='')
    print("Máquina: " + socket.gethostname().ljust(20), end='')
    print("Data: " + currentDate.ljust(20))
    print("-=-" * 30)
    print()

def foot():
    print()
    print("-=-" * 30)
    print()  
    print('Pressione ENTER pra continuar.')
    os.system('pause > NULL' if os.name == 'nt' else 'continue') 

def finalInformation(drive):
    cleanSceen()
    header('Backup realizado')
    print(' Verifique os arquivos em {}'.rjust(50).format(os.path.join(drive, backupFolder)))

def cleanSceen():
    os.system('cls') 

def getUserFolders():
    listUserFolders = []
    for userFolder in os.listdir(root):
        if os.path.isdir(os.path.join(root, userFolder)):
            listUserFolders.append(userFolder)    
        continue
    return listUserFolders

def getDrive():
    drive = input("Informe a unidade de disco. (Tecle ENTER para unidade C:\): ")
    if drive == '':
        drive = 'C'
    return drive

def display():
    lineCount = 0    
    drive = getDrive()+':\\'
    header('Backup iniciado')

    for userFolder in getUserFolders():
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
                        
                        try:
                            shutil.copy(origin, destination)
                            if lineCount == 20:
                                cleanSceen()
                                header('Backup iniciado.')
                                lineCount = 0

                            print('Adicionado [{}] na pasta [{}] em [{}]'.format(file, fileDirectoryByExt, userFolder))
                            sleep(0.3)
                            lineCount += 1
                        except Exception as err:
                            print('Error: {}'.format(err))
                            print()
                            foot()
                            raise SystemExit()
                        
                    continue
    finalInformation(drive)
                                
def main():  
    print("-=-" * 30)
    print('S I S T E M A  D E  B A C K U P'.center(100))
    print("-=-" * 30)
    display()
    foot()


if __name__ == '__main__':
    main()



  
   