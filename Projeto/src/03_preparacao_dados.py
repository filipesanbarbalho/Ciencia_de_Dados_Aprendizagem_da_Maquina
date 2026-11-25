"""
Fase 3: Preparação dos Dados
Projeto: Modelagem Preditiva de Crescimento Populacional e Demográfico na Bacia do Rio Negro
(criação de taxas de crescimento anual e agregações).
"""

import os
import numpy as np
import pandas as pd


def _normalizar_nome_municipio(nome: str) -> str:
    """Normaliza espaços e capitaliza palavras preservando conectores comuns em minúsculo."""
    conectores = {"da", "de", "do", "das", "dos", "e"}
    palavras = nome.strip().split()
    resultado = []
    for idx, palavra in enumerate(palavras):
        baixa = palavra.lower()
        if idx > 0 and baixa in conectores:
            resultado.append(baixa)
        else:
            resultado.append(baixa.capitalize())
    return " ".join(resultado)


def preparar_dados() -> pd.DataFrame:
    caminho_dados = "data/tabela_final_rio_negro.csv"
    if not os.path.exists(caminho_dados):
        caminho_dados = "tabela_final_rio_negro.csv"

    if not os.path.exists(caminho_dados):
        raise FileNotFoundError(
            "Arquivo 'tabela_final_rio_negro.csv' não encontrado em 'data/' nem no diretório atual."
        )

    df = pd.read_csv(caminho_dados, encoding="utf-8")
    print(f"[INFO] Iniciando preparação de dados. Linhas iniciais: {len(df)}")

    # 1. Limpeza e tratamento de inconsistências
    colunas_criticas = ["Município", "Ano", "Quantidade", "Tipo de informação"]
    df = df.drop_duplicates().dropna(subset=colunas_criticas).copy()

    df["Município"] = df["Município"].astype(str).apply(_normalizar_nome_municipio)
    df["Tipo de informação"] = df["Tipo de informação"].astype(str).str.strip()

    if "Localidade" in df.columns:
        df["Localidade"] = df["Localidade"].fillna("Total").astype(str).str.strip()
    else:
        df["Localidade"] = "Total"

    if "Estado" not in df.columns:
        df["Estado"] = "AM"
    else:
        df["Estado"] = df["Estado"].fillna("AM").astype(str).str.strip()

    if "Código IBGE" not in df.columns:
        df["Código IBGE"] = pd.NA

    # Conversão numérica segura para Ano e Quantidade
    df["Ano"] = pd.to_numeric(df["Ano"], errors="coerce")
    if df["Quantidade"].dtype == object:
        quantidade_limpa = (
            df["Quantidade"]
            .astype(str)
            .str.replace(".", "", regex=False)
            .str.replace(",", ".", regex=False)
            .str.strip()
        )
        df["Quantidade"] = pd.to_numeric(quantidade_limpa, errors="coerce")
    else:
        df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce")

    df = df.dropna(subset=["Ano", "Quantidade"]).copy()
    df["Ano"] = df["Ano"].astype(int)

    # 2. Filtragem de atributos relevantes (População e Domicílios)
    df_filtrado = df[df["Tipo de informação"].isin(["População", "Domicílios"])].copy()

    # 3. Engenharia de Atributos: Pivotagem e Agregação
    index_cols = ["Código IBGE", "Município", "Estado", "Ano", "Localidade"]
    df_pivot = df_filtrado.pivot_table(
        index=index_cols,
        columns="Tipo de informação",
        values="Quantidade",
        aggfunc="sum",
        dropna=False,
    ).reset_index()

    df_pivot.columns.name = None

    for col_esperada in ["População", "Domicílios"]:
        if col_esperada not in df_pivot.columns:
            df_pivot[col_esperada] = np.nan

    df_pivot = df_pivot.sort_values(by=["Município", "Localidade", "Ano"]).reset_index(drop=True)

    # 4. Cálculo de variação percentual e taxa de crescimento anual ajustada pelo intervalo de anos
    grupo = df_pivot.groupby(["Município", "Localidade"], dropna=False)

    pop_anterior = grupo["População"].shift(1)
    ano_anterior = grupo["Ano"].shift(1)
    delta_anos = df_pivot["Ano"] - ano_anterior

    variacao_periodo = np.where(
        (pop_anterior > 0) & df_pivot["População"].notna(),
        ((df_pivot["População"] - pop_anterior) / pop_anterior) * 100.0,
        np.nan,
    )
    df_pivot["Variacao_Percentual_Periodo"] = variacao_periodo

    # Taxa anual média no intervalo (evita distorção quando o intervalo entre anos é diferente de 1)
    df_pivot["Taxa_Crescimento_Anual"] = np.where(
        (delta_anos > 0) & pd.notna(variacao_periodo),
        variacao_periodo / delta_anos,
        np.nan,
    )

    # Densidade domiciliar média (habitantes por domicílio)
    df_pivot["Hab_Por_Domicilio"] = np.where(
        df_pivot["Domicílios"] > 0,
        df_pivot["População"] / df_pivot["Domicílios"],
        np.nan,
    )

    # Salvar base processada
    os.makedirs("outputs", exist_ok=True)
    caminho_saida = "outputs/dados_processados_rio_negro.csv"
    df_pivot.to_csv(caminho_saida, index=False, encoding="utf-8")
    print(f"[SUCESSO] Dados preparados salvos em '{caminho_saida}'. Dimensões: {df_pivot.shape}")

    return df_pivot


if __name__ == "__main__":
    preparar_dados()
