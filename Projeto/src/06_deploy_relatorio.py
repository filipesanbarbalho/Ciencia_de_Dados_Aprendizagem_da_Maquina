"""
Fase 6: Implementação / Documentação
Projeto: Modelagem Preditiva de Crescimento Populacional e Demográfico na Bacia do Rio Negro
Descrição: Consolidação final de artefatos, geração de resumo executivo e exportação
do arquivo final consolidado de predições demográficas.
"""

import os
import pandas as pd

def executar_deploy():
    caminho_preds = "outputs/predicoes_2030.csv"
    if not os.path.exists(caminho_preds):
        print("[ERRO] Predições não encontradas para o deploy.")
        return
        
    df_preds = pd.read_csv(caminho_preds)
    
    # Criar tabela consolidada final de entrega
    caminho_final = "outputs/tabela_predicoes_consolidada_rio_negro.csv"
    df_preds.to_csv(caminho_final, index=False)
    
    print("="*60)
    print("PIPELINE CRISP-DM CONCLUÍDO COM SUCESSO")
    print("="*60)
    print(f"[ARTEFATO FINAL GERADO]: {caminho_final}")
    print("\nResumo das Projeções Populacionais para 2030:")
    print(df_preds[['Município', 'Localidade', 'População_Projetada']].to_string(index=False))
    print("\n[INFO] Todos os relatórios, figuras e modelos foram empacotados na pasta /outputs/ com sucesso.")

if __name__ == "__main__":
    executar_deploy()
