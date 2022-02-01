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


import os
import shutil
import socket
import re
from datetime import datetime
from time import sleep


root = 'C:\\users'
current_date = datetime.today().strftime('%d-%m-%Y')
backup_folder = 'bkp_'+socket.gethostname()+'_'+current_date
ext_list = ['.pdf', '.docx', '.xlsx', '.odt', '.ods']
file_directory = 'Arquivos_'
len_length = 30

def header(status_message):
    clean_sceen()
    print("-=-" * len_length)
    print("Status: {}".center(25).format(status_message), end='')
    print("Máquina: " + socket.gethostname().ljust(20), end='')
    print("Data: " + current_date.ljust(20))
    print("-=-" * len_length)
    print()

def foot():
    print()
    print("-=-" * len_length)
    print()  
    print('Pressione ENTER pra continuar.')
    os.system('pause > NULL' if os.name == 'nt' else 'continue') 
    raise SystemExit()

def final_information(drive):
    header('Backup realizado')
    print(' Verifique os arquivos em {}'.rjust(50).format(os.path.join(drive, backup_folder)))

def clean_sceen():
    os.system('cls') 

def get_user_folders():
    list_user_folders = []
    for user_folder in os.listdir(root):
        if os.path.isdir(os.path.join(root, user_folder)):
            list_user_folders.append(user_folder)    
        continue
    return list_user_folders

def get_drive():
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

def processing_core():
    line_count = 0  
    file_count = 0 
    drive = get_drive()
    
    header('Backup iniciado')

    for user_folder in get_user_folders():
        # C:\\bkp_NomeMaquina_dataBackup\pastaUsusario
        path_backup_folder = os.path.join(os.path.join(drive, backup_folder), user_folder)

        # Varre a árvore de diretórios a partir de 'C:\Users\pastaUsuário'
        for folder, subfolders, files in os.walk(os.path.join(root, user_folder)):

            for file_name in files:
                origin = os.path.join(folder, file_name)

                for ext in ext_list:
                    # Cria o diretório 'Arquivos_pdf', 'Arquivos_docx' etc
                    file_directory_by_ext = file_directory+ext.replace('.', '')

                    if file_name.endswith(ext):
                        file_count += 1
                        # Cria 'C:\\bkp_NomeMaquina_dataCriaçãoBackup\pastaUsusário\Arquivos_EXT'
                        full_backup_folder = os.path.join(path_backup_folder, file_directory_by_ext)

                        if not os.path.exists(full_backup_folder):
                            os.makedirs(full_backup_folder)
                        
                        destination = os.path.join(full_backup_folder, file_name) 
                        
                        try:
                            shutil.copy(origin, destination)
                            if line_count == 20:
                                header('Backup iniciado')
                                line_count = 0

                            print('Adicionado [{}] na pasta [{}] em [{}]'.format(file_name, file_directory_by_ext, user_folder))
                            sleep(0.3)
                            line_count += 1
                        except Exception as err:
                            print('Error: {}'.format(err))
                            print()
                            foot()   

                    continue
                
    if file_count != 0:
        final_information(drive)
    else:
        header('Backup abortado')
        print('Não há arquivos para copiar.'.center(95))
        foot()


def main():  
    print("-=-" * len_length)
    print('S I S T E M A  D E  B A C K U P'.center(95))
    print("-=-" * len_length)
    processing_core()
    foot()


if __name__ == '__main__':
    main()



  
   
