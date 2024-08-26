# Uso: python remover_frase.py arquivo.pdf "frase a ser removida" novo_arquivo.pdf


import fitz  # PyMuPDF
import argparse

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
    # Configurando o argparse para receber argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Remover uma frase específica de um PDF.")
    parser.add_argument("input_pdf", help="Caminho do arquivo PDF de entrada.")
    parser.add_argument("frase", help="A frase a ser removida do PDF.")
    parser.add_argument("output_pdf", help="Caminho do arquivo PDF de saída.")

    # Lendo os argumentos da linha de comando
    args = parser.parse_args()

    # Chamando a função para remover a frase
    remover_frase_pdf(args.input_pdf, args.frase, args.output_pdf)

