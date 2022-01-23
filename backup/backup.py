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

currentDate = datetime.today().strftime('%d-%m-%Y')
backup = 'C:\\Backup_'+socket.gethostname()+'_'+currentDate
extList = ['.pdf', '.docx', '.xlsx', '.odt']

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
    print('Backup realizado. Verifique os arquivos em '.rjust(50) + backup)  
    print()     


def main():  
    header()
    
    for folderName, subfolders, filenames in os.walk('C:\\Users'): 
        dirList = folderName.split(os.path.sep)
        for dir in dirList:
            if dir != 'Desktop' and dir != 'Documents' and dir != 'Downloads':
                continue
            
            os.chdir('C:\\Users\\'+dirList[2])
            fullPathBackup = 'C:\\Backup_'+socket.gethostname()+'_'+currentDate+'\\'+dirList[2]
            
            for file in filenames:
                for ext in extList:
                    if file.endswith(ext):
                        if not os.path.exists(fullPathBackup):
                            os.makedirs(fullPathBackup)
                        #os.chdir('C:\\Users\\'+dirList[2]+'\\'+dir+'\\') 
                        #print(os.getcwd())
                        print('Adicionado [%s] na pasta [%s]' % (file, dirList[2]))
                        shutil.copy('C:\\Users\\'+dirList[2]+'\\'+dir+'\\'+file, fullPathBackup)
                        
                        
    foot() 

 
 
if __name__ == '__main__':
    main()



  
   