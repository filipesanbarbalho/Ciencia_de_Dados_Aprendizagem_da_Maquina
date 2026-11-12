"""
Fase 2: Entendimento dos Dados (Análise Exploratória)
Projeto: Modelagem Preditiva de Crescimento Populacional e Demográfico na Bacia do Rio Negro
Descrição: Carrega o dataset 'tabela_final_rio_negro.csv', realiza análise descritiva,
verifica valores nulos/inconsistências e gera gráficos salvos em /outputs/figures/.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração de estilo visual limpo e direto
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11

def executar_analise_exploratoria():
    # 1. Carregamento dos dados
    caminho_dados = "data/tabela_final_rio_negro.csv"
    if not os.path.exists(caminho_dados):
        # Tenta buscar no diretório raiz caso executado de outro local
        caminho_dados = "tabela_final_rio_negro.csv"
    
    df = pd.read_csv(caminho_dados)
    print(f"[INFO] Dataset carregado com sucesso. Dimensões: {df.shape}")
    
    # 2. Verificação de qualidade e valores nulos
    nulos = df.isnull().sum()
    print("\n[INFO] Verificação de Valores Nulos por Coluna:")
    print(nulos)
    
    # 3. Estatísticas descritivas básicas
    print("\n[INFO] Estatísticas Descritivas da Quantidade:")
    print(df['Quantidade'].describe())
    
    # 4. Criação de diretório para figuras
    os.makedirs("outputs/figures", exist_ok=True)
    os.makedirs("outputs/relatorios", exist_ok=True)
    
    # Gráfico 1: População / Quantidade por Município e Ano
    plt.figure(figsize=(10, 6))
    df_pop = df[df['Tipo de informação'] == 'População']
    sns.barplot(data=df_pop, x='Município', y='Quantidade', hue='Ano', palette='Blues', ci=None)
    plt.title("Evolução das Métricas Populacionais por Município na Bacia do Rio Negro", fontsize=12, fontweight='bold')
    plt.xlabel("Município")
    plt.ylabel("Quantidade Total")
    plt.xticks(rotation=15)
    plt.legend(title="Ano")
    plt.tight_layout()
    plt.savefig("outputs/figures/evolucao_populacional_municipio.png", dpi=300)
    plt.close()
    
    # Gráfico 2: Distribuição por Localidade (Urbana vs Rural)
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x='Localidade', y='Quantidade', palette='Set2')
    plt.title("Distribuição de Valores por Localidade (Urbana, Rural, Total)", fontsize=12, fontweight='bold')
    plt.xlabel("Localidade")
    plt.ylabel("Quantidade")
    plt.yscale('log') # Escala logarítmica devido à grande variação
    plt.tight_layout()
    plt.savefig("outputs/figures/distribuicao_localidade.png", dpi=300)
    plt.close()
    
    print("[SUCESSO] Análise exploratória concluída. Gráficos salvos em 'outputs/figures/'.")

if __name__ == "__main__":
    executar_analise_exploratoria()
