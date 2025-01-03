import os
import shutil
import socket
import re
from datetime import datetime
from time import sleep

# Configurações iniciais
ROOT = 'C:\\Users'
CURRENT_DATE = datetime.today().strftime('%d-%m-%Y')
BACKUP_FOLDER = f'bkp_{socket.gethostname()}_{CURRENT_DATE}'
EXT_LIST = ['.pdf', '.docx', '.xlsx', '.odt', '.ods', '.rtf']
FILE_DIRECTORY = 'Arquivos_'
LINE_LENGTH = 30
TARGET_FOLDERS = ['Desktop', 'Documents', 'Downloads', 'Videos', 'Music', 'Pictures']


def clear_screen():
    """Limpa a tela do console."""
    os.system('cls')


def header(status_message):
    """Exibe o cabeçalho com o status do backup."""
    clear_screen()
    print('-=-' * LINE_LENGTH)
    print(f'Status: {status_message}'.ljust(60), end='')
    print(f'Máquina: {socket.gethostname()}'.ljust(20), end='')
    print(f'Data: {CURRENT_DATE}')
    print('-=-' * LINE_LENGTH + '\n')


def footer():
    """Exibe o rodapé e pausa a execução."""
    print('\n' + '-=-' * LINE_LENGTH)
    print('Pressione ENTER para continuar.')
    os.system('pause > NULL')


def final_information(drive):
    """Exibe a mensagem final com o local do backup."""
    header('Backup realizado')
    print(f'Verifique os arquivos em: {os.path.join(drive, BACKUP_FOLDER)}')


def get_user_folders():
    """Obtém as pastas de usuários no diretório ROOT."""
    return [folder for folder in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, folder))]


def get_drive():
    """Solicita ao usuário a unidade de destino para o backup."""
    while True:
        header('Backup iniciado')
        drive = input('Onde deseja salvar os arquivos? (Tecle ENTER para unidade C:\\): ').strip()
        drive = drive if drive else 'C:'
        drive = drive.upper() + '\\'

        if os.path.exists(drive):
            return drive
        else:
            print('\nUnidade de disco informada não existe.'.center(95))
            footer()


def generate_report(folder_path):
    """Gera um relatório dos arquivos copiados."""
    report_path = os.path.join(folder_path, 'report.txt')
    file_counts = {ext: 0 for ext in EXT_LIST}
    total_size = 0

    with open(report_path, 'w', encoding='utf-8') as report:
        report.write('-=-' * LINE_LENGTH + '\n')
        report.write(f'Backup realizado em {CURRENT_DATE}'.center(95) + '\n')
        report.write('-=-' * LINE_LENGTH + '\n')

        for folder, _, files in os.walk(folder_path):
            level = folder.replace(folder_path, '').count(os.sep)
            indentation = '|' + '_' * 4 * level
            report.write(f'{indentation}{os.path.basename(folder)}/\n')

            subindentation = '|' + '_' * 4 * (level + 1)
            for file in files:
                if file not in ['report.txt', 'NULL']:
                    file_path = os.path.join(folder, file)
                    total_size += os.path.getsize(file_path)
                    for ext in EXT_LIST:
                        if file.endswith(ext):
                            file_counts[ext] += 1
                            break
                    report.write(f'{subindentation}{file}\n')

        report.write('-=-' * LINE_LENGTH + '\n')
        report.write('\nResumo:\n')
        for ext, count in file_counts.items():
            report.write(f'Total de arquivos {ext}: {count}\n')
        report.write(f'Tamanho total do backup: {total_size / (1024 * 1024):.2f} MB\n')


def process_backup():
    """Executa o processo principal de backup."""
    drive = get_drive()
    header('Backup iniciado')
    file_count = 0

    for user_folder in get_user_folders():
        backup_path = os.path.join(drive, BACKUP_FOLDER, user_folder)

        for target in TARGET_FOLDERS:
            target_path = os.path.join(ROOT, user_folder, target)
            if not os.path.exists(target_path):
                continue

            for folder, _, files in os.walk(target_path):
                for file_name in files:
                    origin = os.path.join(folder, file_name)

                    for ext in EXT_LIST:
                        if file_name.endswith(ext):
                            file_count += 1
                            target_folder = os.path.join(backup_path, FILE_DIRECTORY + ext[1:])
                            os.makedirs(target_folder, exist_ok=True)

                            destination = os.path.join(target_folder, file_name)
                            try:
                                shutil.copy(origin, destination)
                                print(f'Adicionado [{file_name}] na pasta [{FILE_DIRECTORY + ext[1:]}] em [{user_folder}]')
                                sleep(0.3)
                            except Exception as err:
                                print(f'Erro ao copiar {file_name}: {err}')
                                footer()
                                return

    if file_count > 0:
        generate_report(os.path.join(drive, BACKUP_FOLDER))
        final_information(drive)
    else:
        header('Backup abortado')
        print('Nenhum arquivo encontrado para backup.'.center(95))
        footer()


def main():
    """Função principal."""
    print('-=-' * LINE_LENGTH)
    print('S I S T E M A  D E  B A C K U P'.center(95))
    print('-=-' * LINE_LENGTH)
    process_backup()
    footer()


if __name__ == '__main__':
    main()
