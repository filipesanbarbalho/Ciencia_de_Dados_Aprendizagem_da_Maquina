"""
Fase 1: Entendimento do Negócio
Projeto: Modelagem Preditiva de Crescimento Populacional e Demográfico na Bacia do Rio Negro
Autor: Cientista de Dados / Engenheiro de Software Sênior
Descrição: Define formalmente os objetivos de negócio, escopo, premissas e metas técnicas.
"""

import os

def definir_entendimento_negocio():
    os.makedirs("outputs/relatorios", exist_ok=True)
    
    relatorio = """# Relatório da Fase 1: Entendimento do Negócio

## 1. Contexto e Problema de Negócio
A Bacia do Rio Negro apresenta dinâmicas demográficas complexas, caracterizadas por grandes centros urbanos em expansão (como Manaus) e municípios ribeirinhos/isolados (como Barcelos, Santa Isabel do Rio Negro e São Gabriel da Cachoeira) com forte presença de comunidades tradicionais e indígenas. A ausência de projeções demográficas precisas dificulta o planejamento de políticas públicas, saneamento, infraestrutura escolar e gestão de recursos hídricos.

## 2. Objetivos de Negócio
* **Otimização de Políticas Públicas:** Subsidiar gestores públicos com previsões robustas da população urbana e rural até 2030.
* **Planejamento de Infraestrutura:** Direcionar investimentos em saneamento, saúde e educação de acordo com o crescimento real e projetado dos domicílios e densidades demográficas.
* **Sustentabilidade Ambiental:** Monitorar a pressão demográfica sobre os ecossistemas da bacia.

## 3. Metas Técnicas de Mineração de Dados
* **Acurácia Preditiva:** Obter métricas de avaliação robustas com Erro Absoluto Médio ($MAE$) inferior a 5% da população média e coeficiente de determinação ($R^2 > 0.85$).
* **Reprodutibilidade:** Automatizar todo o pipeline de ponta a ponta seguindo o padrão CRISP-DM.
* **Desacoplamento Modular:** Garantir que cada fase do projeto seja independente, testável e integrada por artefatos versionados.
"""

    caminho_arquivo = "outputs/relatorios/01_entendimento_negocio.md"
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(relatorio)
        
    print(f"[SUCESSO] Relatório de Entendimento do Negócio gerado em: {caminho_arquivo}")

if __name__ == "__main__":
    definir_entendimento_negocio()
