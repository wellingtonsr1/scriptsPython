import csv
import xml.etree.ElementTree as ET
from tkinter import Tk, filedialog, messagebox

def convert_csv_to_xml():
    # Criar a janela principal
    root = Tk()
    root.withdraw()  # Ocultar a janela principal
    
    # Selecionar o arquivo CSV de entrada
    csv_file = filedialog.askopenfilename(
        title="Selecione o arquivo CSV",
        filetypes=[("CSV files", "*.csv")]
    )
    if not csv_file:
        messagebox.showwarning("Aviso", "Nenhum arquivo CSV selecionado.")
        return
    
    # Selecionar o local para salvar o arquivo XML de saída
    xml_file = filedialog.asksaveasfilename(
        title="Salvar arquivo XML como",
        defaultextension=".xml",
        filetypes=[("XML files", "*.xml")]
    )
    if not xml_file:
        messagebox.showwarning("Aviso", "Nenhum local para salvar o XML selecionado.")
        return

    try:
        # Criar a raiz do XML
        root_xml = ET.Element("Root")

        # Ler o arquivo CSV
        with open(csv_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                item = ET.SubElement(root_xml, "Item")
                for key, value in row.items():
                    child = ET.SubElement(item, key)
                    child.text = value

        # Escrever o XML
        tree = ET.ElementTree(root_xml)
        tree.write(xml_file, encoding='utf-8', xml_declaration=True)

        messagebox.showinfo("Sucesso", f"Arquivo convertido e salvo em: {xml_file}")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro durante a conversão: {e}")

# Executar a função
convert_csv_to_xml()

