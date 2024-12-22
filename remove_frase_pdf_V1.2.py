import os
import subprocess
import sys


def check_and_install(package_name):
    print("------------------- Checando dependências... -------------------\n")
    try:
        __import__(package_name)
        print(f"A biblioteca '{package_name}' já está instalada.")
    except ImportError:
        print(f"A biblioteca '{package_name}' não está instalada. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"A biblioteca '{package_name}' foi instalada com sucesso.")
    print("\n------------- Inicando o processamento dos PDFs... -------------\n")
    
         
def remover_frase_pdf(input_pdf, frase, output_pdf):
    # Abrir o PDF para leitura
    pdf_document = fitz.open(input_pdf)

    # Iterar por todas as páginas
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text_instances = page.search_for(frase)

        # Se a frase for encontrada, cobri-la com um retângulo branco
        for inst in text_instances:
            page.add_redact_annot(inst)
            page.apply_redactions()

            # Salvar o novo PDF
            pdf_document.save(output_pdf)
    pdf_document.close()



if __name__ == "__main__":
    check_and_install("PyMuPDF")
    
    import argparse
    import fitz  # PyMuPDF
    
    # Configurando o argparse para receber apenas a frase
    parser = argparse.ArgumentParser(description="Remover uma frase específica de todos os PDFs em uma pasta.")
    parser.add_argument("frase", help="A frase a ser removida dos PDFs.")

    # Lendo os argumentos da linha de comando
    args = parser.parse_args()
    frase = args.frase

    # Pasta padrão contendo os PDFs
    input_folder = os.getcwd()  # Usar a pasta atual como padrão

    # Obtendo a lista de arquivos PDF na pasta
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".pdf"):
            input_pdf = os.path.join(input_folder, filename)
            output_pdf = os.path.join(input_folder, f"{os.path.splitext(filename)[0]}_new.pdf")

            print(f"Processando: {filename} -> {output_pdf}")

            # Remover a frase do PDF
            remover_frase_pdf(input_pdf, frase, output_pdf)

    print("\n-------------------- Processamento concluído. --------------------\n")

