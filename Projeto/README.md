Modelagem Preditiva de Crescimento Populacional na Bacia do Rio Negro

Repositório de um trabalho acadêmico sobre análise estatística, engenharia de dados e modelagem preditiva do crescimento populacional em municípios da Bacia do Rio Negro, desenvolvido com a metodologia CRISP-DM (Cross-Industry Standard Process for Data Mining).

Contextualização

A Bacia do Rio Negro é uma das bacias hidrográficas mais importantes da Amazônia. Abrange ecossistemas sensíveis, terras indígenas e centros urbanos e ribeirinhos. Os municípios incluídos neste estudo são:

Barcelos
Manaus
Santa Isabel do Rio Negro
São Gabriel da Cachoeira
Objetivos
Objetivos de negócio
Planejamento urbano e regional: oferecer projeções demográficas que possam contribuir para discussões sobre infraestrutura básica (saneamento, energia, habitação) e serviços públicos.
Recursos hídricos e ambientais: fazer uma estimativa inicial da pressão da população sobre os recursos hídricos e as áreas de preservação da bacia.
Políticas públicas: comparar o crescimento entre áreas urbanas e rurais, como apoio à reflexão sobre a alocação de recursos sociais e assistenciais.
Metas técnicas
Reunir uma base de dados estruturada a partir de fontes oficiais (tabela_final_rio_negro.csv).
Montar um pipeline de engenharia de atributos com taxas de crescimento anual e proporções demográficas.
Desenvolver e comparar modelos de regressão e machine learning (Regressão Linear, Random Forest e Crescimento Exponencial), tendo como referência MAPE abaixo de 10% e R² acima de 0,85.
Disponibilizar o código de forma reprodutível.

Nota: como há poucos anos de referência por município, as metas de desempenho são um ponto de partida e os resultados devem ser interpretados com cautela.

Descrição do dataset

O arquivo tabela_final_rio_negro.csv contém as colunas:

ID: identificador único da linha.
Município: nome do município da bacia.
Estado: unidade federativa (Amazonas).
Ano: ano de referência (por exemplo, 2010, 2022, 2024).
Localidade: categoria espacial (Urbana, Rural ou Total).
Tipo de informação: métrica demográfica (População, Demografia, Domicílios ou Deslocamento).
Quantidade: valor numérico da métrica.
Unidade: unidade de medida (Pessoas, etc.).
Fonte: origem dos dados (IBGE - Censo Demográfico e SIDRA).
Código IBGE: código de identificação do município.
Estrutura do repositório
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
