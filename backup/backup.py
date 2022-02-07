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
import logging

logging.basicConfig(
    filename='backup/logs/backup.log', 
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

root = 'C:\\users'
current_date = datetime.today().strftime('%d-%m-%Y')
backup_folder = 'bkp_'+socket.gethostname()+'_'+current_date
ext_list = ['.pdf', '.docx', '.xlsx', '.odt', '.ods']
file_directory = 'Arquivos_'
len_length = 30


def man_header():
    clean_sceen()
    print('-=-' * len_length)
    print('S I S T E M A  D E  B A C K U P'.center(95))
    print('-=-' * len_length)

def secondary_header(status_message):
    logging.info(status_message)
    clean_sceen()
    print('-=-' * len_length)
    print(f'Status: {status_message}'.rjust(30), end='')
    print(f'Máquina: {socket.gethostname()}'.center(35), end='')
    print(f'Data: {current_date}'.ljust(30))
    print('-=-' * len_length)
    print('')
    
def foot():
    print('')
    print('-=-' * len_length)
    print('')  
    print('Pressione ENTER pra continuar.')
    os.system('pause > NULL') 
    #raise SystemExit()

def final_information(drive):
    logging.info('Backup realizado')
    secondary_header('Backup realizado')
    print(f'Verifique os arquivos em {os.path.join(drive, backup_folder)}'.center(95))
    

def clean_sceen():
    os.system('cls') 

def get_user_folders():
    logging.info('Obtendo as pasta dos usuários.')

    list_user_folders = []  
    for user_folder in os.listdir(root):
        if os.path.isdir(os.path.join(root, user_folder)):
            list_user_folders.append(user_folder)    
        continue
    return list_user_folders

def get_drive():
    logging.info('Obtendo a unidade de disco')

    while True:
        man_header()

        drive = re.sub(r'\s+', '', input('Onde deseja salvar os arquivos? (Tecle ENTER para unidade C:\): '.rjust(66)))
        if not drive:
            drive = 'C'
        drive = drive+':\\'
        if os.path.exists(drive):
            return drive.upper()
        else:
            print('')
            print('A unidade de disco informada não existe.'.center(95))
            logging.warning(f'A unidade {drive} não existe.')
            foot()

def report(folder_path):
    logging.info('Gerando o report.txt')

    os.chdir(folder_path)

    file_object = open('report.txt', 'w', encoding='utf-8')

    file_object.write('-=-' * len_length + '\n')
    file_object.write(f'Backup realizado em {current_date}'.center(95)  + '\n')
    file_object.write('-=-' * len_length  + '\n')

    for folder, subfolders, files in os.walk(folder_path):
        # substitui o nome da pasta principal por vazio e conta quantos niveis (\) tem
        level = folder.replace(folder_path, '').count(os.sep)

        indentation = '|' + '_' * 4 * (level)
        file_object.write(f'{indentation}{os.path.basename(folder)}/' + '\n')

        subindentation = '|' + '_' * 4 * (level + 1)
        for f in files:
            if not f.endswith('txt') or f == 'NULL':
                file_object.write(f'{subindentation}{f}' + '\n')

    file_object.write('-=-' * len_length  + '\n')
    file_object.close()
    
    logging.info('Arquivo report.txt gerado')

def processing_core():
    line_count = 0  
    file_count = 0 
    drive = get_drive()
    
    secondary_header('Backup iniciado')
    logging.info('Backup iniciado')

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
                                secondary_header('Backup iniciado')
                                line_count = 0

                            print(f'Adicionado [{file_name}] na pasta [{file_directory_by_ext}] em [{user_folder}]')
                            logging.info(f'Adicionado [{file_name}] na pasta [{file_directory_by_ext}] em [{user_folder}]')
                            sleep(0.3)
                            line_count += 1
                        except Exception as err:
                            print(f'Error: {err}')
                            print('')
                            foot() 
                            raise SystemExit()  

                    continue
                
    if file_count != 0:
        report(os.path.join(drive, backup_folder))
        final_information(drive)
    else:
        secondary_header('Backup abortado')
        print('Não há arquivos para copiar.'.center(95))
        #foot()

def main():  
    logging.info('Programa iniciado.')
    processing_core()
    foot()


if __name__ == '__main__':
    main()



  
   
