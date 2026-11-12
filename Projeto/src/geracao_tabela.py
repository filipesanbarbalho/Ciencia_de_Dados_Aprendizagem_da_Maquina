"""
Módulo de Geração da Tabela Final e Visualizações
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_tabela_e_graficos():
    df = pd.read_csv("dados/dados_tratados/base_tratada.csv")
    
    # Ordenação por município e ano conforme especificado
    df = df.sort_values(by=["Município", "Ano"])
    
    # Exportar tabela final CSV
    caminho_final = "resultados/tabela_final.csv"
    df.to_csv(caminho_final, index=False, encoding="utf-8-sig")
    print(f"Tabela final exportada com sucesso para: {caminho_final} ({len(df)} registros)")
    
    # Geração de Gráficos
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    
    df_pop = df[df["Tipo de informação"] == "População"]
    sns.barplot(data=df_pop, x="Município", y="Quantidade", hue="Ano", palette="Blues")
    plt.title("Evolução Populacional por Município (Região do Rio Negro)")
    plt.xlabel("Município")
    plt.ylabel("Quantidade de Habitantes")
    plt.xticks(rotation=15)
    plt.tight_layout()
    
    plt.savefig("resultados/graficos/evolucao_populacional.png", dpi=300)
    plt.close()
    print("Gráficos gerados com sucesso na pasta resultados/graficos/!")

if __name__ == "__main__":
    gerar_tabela_e_graficos()
