"""
Fase 3: Preparação dos Dados
Projeto: Modelagem Preditiva de Crescimento Populacional e Demográfico na Bacia do Rio Negro
Descrição: Limpeza, tratamento de inconsistências, filtragem e engenharia de atributos
(criação de taxas de crescimento anual e agregações).
"""

import os
import pandas as pd
import numpy as np

def preparar_dados():
    caminho_dados = "data/tabela_final_rio_negro.csv"
    if not os.path.exists(caminho_dados):
        caminho_dados = "tabela_final_rio_negro.csv"
        
    df = pd.read_csv(caminho_dados)
    print(f"[INFO] Iniciando preparação de dados. Linhas iniciais: {len(df)}")
    
    # 1. Limpeza e tratamento de inconsistências (remoção de duplicatas ou nulos críticos)
    df = df.dropna(subset=['Município', 'Ano', 'Quantidade', 'Tipo de informação'])
    df['Município'] = df['Município'].str.strip().str.title()
    
    # 2. Filtragem de atributos relevantes (Foco em Informações Populacionais e Domiciliares)
    df_filtrado = df[df['Tipo de informação'].isin(['População', 'Domicílios'])].copy()
    
    # 3. Engenharia de Atributos: Pivotagem e Agregação por Município, Ano e Localidade
    df_pivot = df_filtrado.pivot_table(
        index=['Código IBGE', 'Município', 'Estado', 'Ano', 'Localidade'],
        columns='Tipo de informação',
        values='Quantidade',
        aggfunc='sum'
    ).reset_index()
    
    # Garantir presença das colunas esperadas
    if 'População' not in df_pivot.columns:
        df_pivot['População'] = np.nan
    if 'Domicílios' not in df_pivot.columns:
        df_pivot['Domicílios'] = np.nan
        
    df_pivot = df_pivot.sort_values(by=['Município', 'Localidade', 'Ano'])
    
    # 4. Cálculo de taxas de crescimento inter-censitárias / temporais por município e localidade
    df_pivot['Taxa_Crescimento_Anual'] = df_pivot.groupby(['Município', 'Localidade'])['População'].pct_change() * 100
    
    # Salvar base processada
    os.makedirs("outputs", exist_ok=True)
    caminho_saida = "outputs/dados_processados_rio_negro.csv"
    df_pivot.to_csv(caminho_saida, index=False)
    print(f"[SUCESSO] Dados preparados salvos em '{caminho_saida}'. Dimensões: {df_pivot.shape}")

if __name__ == "__main__":
    preparar_dados()
