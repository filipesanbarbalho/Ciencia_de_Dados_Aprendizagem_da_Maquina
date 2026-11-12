"""
Fase 4: Modelagem
Projeto: Modelagem Preditiva de Crescimento Populacional e Demográfico na Bacia do Rio Negro
Descrição: Aplicação de técnicas matemáticas e estatísticas (Regressão Linear e Projeção Tendencial)
para projetar o crescimento populacional futuro dos municípios.
"""

import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib

def executar_modelagem():
    caminho_dados = "outputs/dados_processados_rio_negro.csv"
    if not os.path.exists(caminho_dados):
        print("[ERRO] Base de dados processada não encontrada. Execute 03_preparacao_dados.py primeiro.")
        return
        
    df = pd.read_csv(caminho_dados)
    df_pop = df.dropna(subset=['População']).copy()
    
    print(f"[INFO] Iniciando modelagem preditiva para {df_pop['Município'].nunique()} municípios.")
    
    resultados_predicoes = []
    modelos = {}
    
    # Treinamento de modelo de tendência linear temporal por Município e Localidade
    for (municipio, localidade), grupo in df_pop.groupby(['Município', 'Localidade']):
        if len(grupo) < 2:
            continue # Necessário ao menos 2 pontos temporais para regressão
            
        X = grupo[['Ano']].values
        y = grupo['População'].values
        
        # Ajuste do modelo de Regressão Linear
        modelo = LinearRegression()
        modelo.fit(X, y)
        
        # Avaliação in-sample / métricas técnicas
        y_pred = modelo.predict(X)
        rmse = np.sqrt(mean_squared_error(y, y_pred))
        mae = mean_absolute_error(y, y_pred)
        r2 = r2_score(y, y_pred) if len(grupo) > 2 else 1.0
        
        print(f"-> Município: {municipio} | Localidade: {localidade} | R²: {r2:.4f} | MAE: {mae:.2f}")
        
        # Projeção Futura para o ano de 2030
        ano_futuro = np.array([[2030]])
        pop_projetada_2030 = modelo.predict(ano_futuro)[0]
        
        resultados_predicoes.append({
            'Município': municipio,
            'Localidade': localidade,
            'Ano_Projecao': 2030,
            'População_Projetada': max(0, int(pop_projetada_2030)),
            'RMSE_Historico': rmse,
            'MAE_Historico': mae,
            'R2_Historico': r2
        })
        
        modelos[f"{municipio}_{localidade}"] = modelo
        
    df_preds = pd.DataFrame(resultados_predicoes)
    caminho_preds = "outputs/predicoes_2030.csv"
    df_preds.to_csv(caminho_preds, index=False)
    
    # Salvar modelos treinados
    joblib.dump(modelos, "outputs/modelos_regressao_demografica.pkl")
    print(f"[SUCESSO] Modelagem concluída. Predições para 2030 salvas em '{caminho_preds}'.")

if __name__ == "__main__":
    executar_modelagem()
