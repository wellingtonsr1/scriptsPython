import csv
import xml.etree.ElementTree as ET

# Caminho dos arquivos
csv_file = "contatos IPM - COMPLETO-ATUALIZADO.csv"
xml_file = "contatos IPM - COMPLETO-ATUALIZADO.xml"

# Criar a raiz do XML
root = ET.Element("Root")

# Ler o arquivo CSV
with open(csv_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        item = ET.SubElement(root, "Item")
        for key, value in row.items():
            child = ET.SubElement(item, key)
            child.text = value

# Escrever o XML
tree = ET.ElementTree(root)
tree.write(xml_file, encoding='utf-8', xml_declaration=True)

print(f"Arquivo convertido e salvo em: {xml_file}")

