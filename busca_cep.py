import requests
import pandas as pd
import os

def buscar_cep(nome_rua, cidade, uf):
    url = f"https://viacep.com.br/ws/{uf}/{cidade}/{nome_rua}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        if dados:
            return [
                {
                    "CEP": endereco['cep'],
                    "Logradouro": endereco['logradouro'],
                    "Bairro": endereco['bairro'],
                    "Cidade": cidade,
                    "Estado": uf
                }
                for endereco in dados
            ]
    return []

def processar_csv(input_csv, output_excel):
    # Verifica se o arquivo existe
    if not os.path.isfile(input_csv):
        print(f"Arquivo não encontrado: {input_csv}")
        return
    
    try:
        # Lê o arquivo CSV de entrada
        df = pd.read_csv(input_csv)
        print("Colunas encontradas no CSV:", df.columns)  # Para verificar as colunas
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
        return
    
    lista_resultados = []

    for index, row in df.iterrows():
        try:
            nome_rua = row['Rua']
            cidade = row['Cidade']
            uf = row['Estado']
        except KeyError as e:
            print(f"Erro: coluna {e} não encontrada. Verifique o arquivo CSV.")
            continue

        resultados = buscar_cep(nome_rua, cidade, uf)
        lista_resultados.extend(resultados)
    
    # Converte os resultados em um DataFrame pandas
    df_resultados = pd.DataFrame(lista_resultados)
    
    # Salva os resultados em uma planilha Excel
    df_resultados.to_excel(output_excel, index=False)
    print(f"Resultados salvos na planilha: {output_excel}")

# Exemplo de uso
input_csv = "enderecos_2.csv"  # Nome do arquivo CSV de entrada
output_excel = "resultados_ceps.xlsx"  # Nome do arquivo Excel de saída
processar_csv(input_csv, output_excel)
