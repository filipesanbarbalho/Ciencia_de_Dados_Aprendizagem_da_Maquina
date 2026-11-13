# Modelagem Preditiva de Crescimento Populacional e Demográfico na Bacia do Rio Negro

Repositório oficial do trabalho acadêmico e técnico voltado para a análise estatística, engenharia de dados e modelagem preditiva do crescimento populacional nos municípios da Bacia do Rio Negro, desenvolvido sob a metodologia **CRISP-DM (Cross-Industry Standard Process for Data Mining)**.

---

## Contextualização da Bacia do Rio Negro
A Bacia do Rio Negro é uma das bacias hidrográficas mais importantes da Amazônia, abrangendo ecossistemas críticos, terras indígenas e centros urbanos e ribeirinhos de grande relevância geopolítica e ambiental. Os municípios contemplados neste estudo são:
* **Barcelos**
* **Manaus**
* **Santa Isabel do Rio Negro**
* **São Gabriel da Cachoeira**

---

##  Objetivos do Projeto

### 1. Objetivos de Negócio
* **Planejamento Urbano e Regional:** Fornecer projeções demográficas confiáveis para subsidiar o dimensionamento de infraestrutura básica (saneamento, energia, habitação) e serviços públicos.
* **Gestão de Recursos Hídricos e Ambientais:** Estimar a pressão antrópica sobre os recursos hídricos e áreas de preservação na bacia.
* **Políticas Públicas Direcionadas:** Avaliar o diferencial de crescimento entre áreas urbanas e rurais para otimizar a alocação de recursos sociais e assistenciais.

### 2. Metas Técnicas
* Consolidar uma base de dados estruturada a partir de fontes oficiais (`tabela_final_rio_negro.csv`).
* Executar pipeline de engenharia de atributos calculando taxas de crescimento anual e proporções demográficas.
* Desenvolver e comparar modelos de machine learning e regressão estatística (Regressão Linear, Random Forest e Crescimento Exponencial) com Erro Percentual Absoluto Médio ($MAPE < 10\%$) e $R^2 > 0.85$.
* Disponibilizar artefatos reprodutíveis e prontos para implantação.

---

##  Descrição do Dataset
O conjunto de dados base (`tabela_final_rio_negro.csv`) contém as seguintes colunas:
* `ID`: Identificador único da linha.
* `Município`: Nome do município da bacia.
* `Estado`: Unidade federativa (Amazonas).
* `Ano`: Ano de referência (ex: 2010, 2022, 2024).
* `Localidade`: Categoria espacial (`Urbana`, `Rural`, `Total`).
* `Tipo de informação`: Métrica demográfica (`População`, `Demografia`, `Domicílios`, `Deslocamento`).
* `Quantidade`: Valor numérico da métrica.
* `Unidade`: Unidade de medida (`Pessoas`, etc.).
* `Fonte`: Origem oficial dos dados (IBGE - Censo Demográfico e SIDRA).
* `Código IBGE`: Código oficial de identificação municipal.

---

##  Estrutura do Repositório
```text
.
├── data/
│   └── tabela_final_rio_negro.csv
├── outputs/
│   ├── figures/
│   └── relatorios/
├── src/
│   ├── 01_entendimento_negocio.py
│   ├── 02_analise_exploratoria.py
│   ├── 03_preparacao_dados.py
│   ├── 04_modelagem.py
│   ├── 05_avaliacao.py
│   └── 06_deploy_relatorio.py
├── requirements.txt
└── README.md
