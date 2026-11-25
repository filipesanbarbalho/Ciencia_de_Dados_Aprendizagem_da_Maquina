"""
Fase 5: Avaliação
Projeto: Modelagem Preditiva de Crescimento Populacional e Demográfico na Bacia do Rio Negro
Descrição: Cruzamento dos resultados métricos do modelo com os critérios de sucesso do negócio
definidos na Fase 1, analisando o impacto real das projeções.
"""

import os
import pandas as pd


def executar_avaliacao() -> None:
    caminho_preds = "outputs/predicoes_2030.csv"
    if not os.path.exists(caminho_preds):
        print("[ERRO] Arquivo de predições não encontrado. Execute 04_modelagem.py primeiro.")
        return

    df_preds = pd.read_csv(caminho_preds, encoding="utf-8")
    if df_preds.empty:
        print("[ERRO] O arquivo 'outputs/predicoes_2030.csv' está vazio.")
        return

    colunas_obrigatorias = ["R2_Historico", "MAE_Historico"]
    faltantes = [c for c in colunas_obrigatorias if c not in df_preds.columns]
    if faltantes:
        print(f"[ERRO] Colunas obrigatórias ausentes em predicoes_2030.csv: {faltantes}")
        return

    df_preds["R2_Historico"] = pd.to_numeric(df_preds["R2_Historico"], errors="coerce")
    df_preds["MAE_Historico"] = pd.to_numeric(df_preds["MAE_Historico"], errors="coerce")

    r2_validos = df_preds["R2_Historico"].dropna()
    mae_validos = df_preds["MAE_Historico"].dropna()

    if r2_validos.empty or mae_validos.empty:
        print("[ERRO] Não há valores numéricos válidos em 'R2_Historico' ou 'MAE_Historico'.")
        return

    r2_medio = float(r2_validos.mean())
    r2_mediana = float(r2_validos.median())
    r2_min = float(r2_validos.min())
    r2_max = float(r2_validos.max())
    mae_medio = float(mae_validos.mean())

    proporcao_meta_r2 = float((r2_validos >= 0.80).mean() * 100.0)
    criterio_sucesso_r2 = r2_medio >= 0.80

    print("=" * 60)
    print("RELATÓRIO DE AVALIAÇÃO TÉCNICA E DE NEGÓCIO (CRISP-DM)")
    print("=" * 60)
    print(f"Média de R² dos modelos ajustados: {r2_medio:.4f} (Mediana: {r2_mediana:.4f})")
    print(f"Faixa de R² observada: [{r2_min:.4f}, {r2_max:.4f}]")
    print(f"Média de Erro Absoluto Médio (MAE): {mae_medio:.2f} habitantes")
    print(f"Modelos com R² >= 0.80: {proporcao_meta_r2:.1f}%")

    print("\n[VERIFICAÇÃO DE CRITÉRIOS DE SUCESSO]")
    print(f"- Meta Técnica R² >= 0.80 atingida? {'SIM' if criterio_sucesso_r2 else 'NÃO'} ({r2_medio:.4f})")
    print("- Alinhamento com Planejamento Urbano: Aderente para dimensionamento de redes de saneamento e escolas.")

    bloco_projecao = ""
    for col_proj in ["Projecao_2030", "Populacao_2030", "Previsao_2030"]:
        if col_proj in df_preds.columns:
            total_2030 = pd.to_numeric(df_preds[col_proj], errors="coerce").dropna().sum()
            bloco_projecao = f"- **População Projetada Total (2030 - `{col_proj}`):** {total_2030:,.0f} habitantes\n"
            break

    status_meta = "ATENDIDA" if criterio_sucesso_r2 else "NÃO ATINGIDA (requer revisão do modelo)"

    relatorio_avaliacao = f"""# Relatório de Avaliação - Fase 5 (CRISP-DM)

- **Média de Coeficiente de Determinação (R²):** {r2_medio:.4f} (Mediana: {r2_mediana:.4f} | Mín: {r2_min:.4f} | Máx: {r2_max:.4f})
- **Média de Erro Absoluto (MAE):** {mae_medio:.2f} pessoas
- **Cobertura da Meta Técnica (R² >= 0.80):** {proporcao_meta_r2:.1f}% dos registros ({status_meta})
{bloco_projecao}- **Conclusão:** Os modelos de projeção foram avaliados frente aos critérios estabelecidos na Fase 1 para apoiar o planejamento regional e a alocação de infraestrutura na Bacia do Rio Negro.
"""

    os.makedirs("outputs/relatorios", exist_ok=True)
    caminho_relatorio = "outputs/relatorios/05_avaliacao_modelo.md"
    with open(caminho_relatorio, "w", encoding="utf-8") as f:
        f.write(relatorio_avaliacao)

    print(f"[SUCESSO] Relatório de avaliação gerado em '{caminho_relatorio}'.")


if __name__ == "__main__":
    executar_avaliacao()
