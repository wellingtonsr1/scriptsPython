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
import re
from datetime import datetime
from time import sleep


root = 'C:\\users'
currentDate = datetime.today().strftime('%d-%m-%Y')
backupFolder = 'bkp_'+socket.gethostname()+'_'+currentDate
extList = ['.pdf', '.docx', '.xlsx', '.odt', '.ods']
fileDirectory = 'Arquivos_'
lenLength = 30

def header(statusMessage):
    cleanSceen()
    print("-=-" * lenLength)
    print("Status: {}".center(25).format(statusMessage), end='')
    print("Máquina: " + socket.gethostname().ljust(20), end='')
    print("Data: " + currentDate.ljust(20))
    print("-=-" * lenLength)
    print()

def foot():
    print()
    print("-=-" * lenLength)
    print()  
    print('Pressione ENTER pra continuar.')
    os.system('pause > NULL' if os.name == 'nt' else 'continue') 
    raise SystemExit()

def finalInformation(drive):
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
    drive = re.sub(r'\s+', '', input("Onde deseja salvar os arquivos? (Tecle ENTER para unidade C:\): ".rjust(66)))
    if drive == '':
        drive = 'C'
    drive = drive+':\\'
    if os.path.exists(drive):
        return drive.upper()
    else:
        print()
        print('A unidade de disco informada não existe.'.center(95))
        foot()

def processingCore():
    lineCount = 0  
    fileCount = 0 
    drive = getDrive()
    
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
                        fileCount += 1
                        # Cria 'C:\\bkp_NomeMaquina_dataCriaçãoBackup\pastaUsusário\Arquivos_EXT'
                        fullBackupFolder = os.path.join(pathBackupFolder, fileDirectoryByExt)
                        if not os.path.exists(fullBackupFolder):
                            os.makedirs(fullBackupFolder)
                        
                        destination = os.path.join(fullBackupFolder, file) 
                        
                        try:
                            shutil.copy(origin, destination)
                            if lineCount == 20:
                                header('Backup iniciado')
                                lineCount = 0

                            print('Adicionado [{}] na pasta [{}] em [{}]'.format(file, fileDirectoryByExt, userFolder))
                            sleep(0.3)
                            lineCount += 1
                        except Exception as err:
                            print('Error: {}'.format(err))
                            print()
                            foot()                        
                    continue
    if fileCount != 0:
        finalInformation(drive)
    else:
        header('Backup abortado')
        print('Não há arquivos para copiar.'.center(95))
        foot()


def main():  
    print("-=-" * lenLength)
    print('S I S T E M A  D E  B A C K U P'.center(95))
    print("-=-" * lenLength)
    processingCore()
    foot()


if __name__ == '__main__':
    main()



  
   