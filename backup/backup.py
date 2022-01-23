#! python3
# backup.py
# Copia os arquivos das pastas (Desktop, Documents e Downloads) dos usuários 
# que tenhasm pelo menos um arquivo em qualquer uma delas.


import os, shutil, socket
from datetime import datetime


currentDate = datetime.today().strftime('%d-%m-%Y')
backup = 'C:\\Backup_'+socket.gethostname()+'_'+currentDate

print("-=-" * 30)
print("Iniciando o backup...".center(40), end='')
print("Máquina: " + socket.gethostname().ljust(20), end='')
print("Data: " + currentDate.ljust(30))
print("-=-" * 30)
print()

for folderName, subfolders, filenames in os.walk('C:\\Users'): 
    listDir = folderName.split(os.path.sep)
    for dir in listDir:
        if dir != 'Desktop' and dir != 'Documents' and dir != 'Downloads':
            continue
        
        os.chdir('C:\\Users\\'+listDir[2])
        fullPathBackup = 'C:\\Backup_'+socket.gethostname()+'_'+currentDate+'\\'+listDir[2]
        
        for file in filenames:
            if file.endswith('.pdf') or file.endswith('.docx') or file.endswith('.xlsx'):
                if not os.path.exists(fullPathBackup):
                    os.makedirs(fullPathBackup)
                    
                print('Adicionando %s em %s...' % (file, listDir[2]))
                shutil.copy('C:\\Users\\'+listDir[2]+'\\'+dir+'\\'+file, fullPathBackup)
print()
print("-=-" * 30)
print('Backup realizado. Verifique os arquivos em '.rjust(50) + backup)  
print()     
                

          
        


  
   