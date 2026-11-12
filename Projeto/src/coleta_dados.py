"""
Módulo de Coleta de Dados Oficiais do IBGE
Região do Rio Negro - Amazonas
"""
import os
import requests
import pandas as pd

# Configuração de diretórios
os.makedirs("dados/dados_originais", exist_ok=True)
os.makedirs("dados/dados_tratados", exist_ok=True)
os.makedirs("resultados", exist_ok=True)
os.makedirs("resultados/graficos", exist_ok=True)

MUNICIPIOS = {
    "Manaus": "1302603",
    "Barcelos": "1300607",
    "Santa Isabel do Rio Negro": "1303809",
    "São Gabriel da Cachoeira": "1305606"
}

def coletar_dados_sidra():
    print("Iniciando coleta de dados oficiais via API SIDRA / IBGE...")
    
    # Exemplo estruturado de requisição para Tabela 6579 (Estimativa de População)
    url_pop = "https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021|2022|2024/variaveis/9324?localidades=N6[1302603,1300607,1303809,1305606]"
    
    try:
        response = requests.get(url_pop)
        if response.status_code == 200:
            data = response.json()
            print("Dados populacionais coletados com sucesso!")
            # Salvar bruto
            import json
            with open("dados/dados_originais/populacao_bruta.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        else:
            print(f"Erro na requisição SIDRA: {response.status_code}")
    except Exception as e:
        print(f"Erro de conexão: {e}")

if __name__ == "__main__":
    coletar_dados_sidra()
