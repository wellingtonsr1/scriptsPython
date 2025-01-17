import os
import subprocess
import sys
import pkg_resources
import tkinter as tk
from tkinter import filedialog, messagebox

# Função para verificar e instalar dependências
def check_and_install(package_name):
    try:
        pkg_resources.get_distribution(package_name)
    except pkg_resources.DistributionNotFound:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

# Instalar PyMuPDF, se necessário
check_and_install("PyMuPDF")

import fitz  # PyMuPDF

def remover_frase_pdf(input_pdf, frase, output_pdf):
    """Remove uma frase específica de um PDF e salva o resultado."""
    try:
        pdf_document = fitz.open(input_pdf)
        alterado = False

        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text_instances = page.search_for(frase)

            for inst in text_instances:
                page.add_redact_annot(inst, text="", fill=(1, 1, 1))
                alterado = True

            if alterado:
                page.apply_redactions()

        if alterado:
            pdf_document.save(output_pdf)
            return f"Alterações salvas em: {output_pdf}"
        else:
            return f"Nenhuma alteração necessária para: {input_pdf}"

    except Exception as e:
        return f"Erro ao processar o arquivo {input_pdf}: {e}"

# Função principal para processamento de PDFs
def processar_pdfs(diretorio, frase):
    resultados = []
    for filename in os.listdir(diretorio):
        if filename.lower().endswith(".pdf"):
            input_pdf = os.path.join(diretorio, filename)
            output_pdf = os.path.join(diretorio, f"{os.path.splitext(filename)[0]}_editado.pdf")
            resultado = remover_frase_pdf(input_pdf, frase, output_pdf)
            resultados.append(resultado)
    return resultados

# Função para abrir o seletor de pasta
def selecionar_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        pasta_entry.delete(0, tk.END)
        pasta_entry.insert(0, pasta)

# Função para executar o processamento
def executar():
    frase = frase_entry.get()
    diretorio = pasta_entry.get()

    if not frase:
        messagebox.showerror("Erro", "Por favor, insira a frase a ser removida.")
        return

    if not os.path.isdir(diretorio):
        messagebox.showerror("Erro", "Por favor, selecione um diretório válido.")
        return

    resultados = processar_pdfs(diretorio, frase)
    messagebox.showinfo("Processamento Concluído", "\n".join(resultados))

# Criar a janela principal
root = tk.Tk()
root.title("Remoção de Frases em PDFs")

# Layout
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

# Campo para a frase
tk.Label(frame, text="Frase a ser removida:").grid(row=0, column=0, sticky=tk.W)
frase_entry = tk.Entry(frame, width=50)
frase_entry.grid(row=0, column=1, padx=5, pady=5)

# Campo para o diretório
tk.Label(frame, text="Pasta com PDFs:").grid(row=1, column=0, sticky=tk.W)
pasta_entry = tk.Entry(frame, width=50)
pasta_entry.grid(row=1, column=1, padx=5, pady=5)

# Botão para selecionar pasta
tk.Button(frame, text="Selecionar Pasta", command=selecionar_pasta).grid(row=1, column=2, padx=5, pady=5)

# Botão para executar
executar_btn = tk.Button(frame, text="Executar", command=executar, bg="green", fg="white")
executar_btn.grid(row=2, column=0, columnspan=3, pady=10)

# Iniciar a aplicação
root.mainloop()

