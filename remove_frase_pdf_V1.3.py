import os
import subprocess
import sys
import pkg_resources


def check_and_install(package_name):
    """Verifica e instala o pacote necessário."""
    print("------------------- Checando dependências... -------------------\n")
    try:
        dist = pkg_resources.get_distribution(package_name)
        print(f"A biblioteca '{package_name}' já está instalada. Versão: {dist.version}")
    except pkg_resources.DistributionNotFound:
        print(f"A biblioteca '{package_name}' não está instalada. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"A biblioteca '{package_name}' foi instalada com sucesso.")
    except Exception as e:
        print(f"Erro ao verificar/instalar a biblioteca '{package_name}': {e}")
        sys.exit(1)
    print("\n------------- Iniciando o processamento dos PDFs... -------------\n")



def remover_frase_pdf(input_pdf, frase, output_pdf):
    """Remove uma frase específica de um PDF e salva o resultado."""
    try:
        pdf_document = fitz.open(input_pdf)
        alterado = False  # Para verificar se alterações foram realizadas

        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text_instances = page.search_for(frase)

            for inst in text_instances:
                page.add_redact_annot(inst, text="", fill=(1, 1, 1))  # Retângulo branco
                alterado = True

            if alterado:
                page.apply_redactions()

        if alterado:
            pdf_document.save(output_pdf)
            print(f"Alterações salvas em: {output_pdf}\n")
        else:
            print(f"Nenhuma alteração necessária para: {input_pdf}\n")

        pdf_document.close()

    except Exception as e:
        print(f"Erro ao processar o arquivo {input_pdf}: {e}")


if __name__ == "__main__":
    check_and_install("PyMuPDF")

    import argparse
    import fitz  # PyMuPDF

    # Configuração do argparse
    parser = argparse.ArgumentParser(description="Remove uma frase específica de todos os PDFs em uma pasta.")
    parser.add_argument("frase", help="A frase a ser removida dos PDFs.")
    parser.add_argument("-d", "--dir", default=os.getcwd(), help="Pasta contendo os arquivos PDF (padrão: pasta atual).")

    args = parser.parse_args()
    frase = args.frase
    input_folder = args.dir

    # Listar e processar arquivos PDF
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".pdf"):
            input_pdf = os.path.join(input_folder, filename)
            output_pdf = os.path.join(input_folder, f"{os.path.splitext(filename)[0]}_editado.pdf")

            print(f"Processando: {filename} -> {output_pdf}")
            remover_frase_pdf(input_pdf, frase, output_pdf)

    print("\n-------------------- Processamento concluído. --------------------\n")

