# Análise de Dados Sociodemográficos e Territoriais da Região do Rio Negro – Amazonas

## 1. Objetivo da Pesquisa
Desenvolver uma base de dados integrada e consolidada a partir de fontes oficiais do IBGE, estruturando indicadores demográficos, socioeconômicos e territoriais dos municípios da calha do Rio Negro, no estado do Amazonas, para subsidiar análises de deslocamento, planejamento urbano e políticas públicas.

## 2. Contextualização Geográfica do Rio Negro
A região do Rio Negro constitui uma das bacias hidrográficas e culturais mais importantes da Amazônia brasileira. Os municípios de **Manaus**, **Barcelos**, **Santa Isabel do Rio Negro** e **São Gabriel da Cachoeira** possuem forte dependência da mobilidade fluvial, sendo o transporte de barcos o principal vetor de deslocamento de passageiros e cargas. 

*Nota metodológica:* Conforme as normas estatísticas oficiais, o IBGE não dispõe de uma base contínua específica de "viagens fluviais diárias" desagregadas por hidrovias municipais no SIDRA; portanto, o escopo de deslocamentos e viagens é abordado por meio de estatísticas de migração, deslocamento pendular (Censo Demográfico) e características demográficas estruturais, sem equiparar dados populacionais a registros individuais de turismo.

## 3. Metodologia de Coleta
A coleta foi realizada utilizando Python para requisições automatizadas na API agregada do IBGE (SIDRA) e arquivos estruturados de censos e pesquisas oficiais, garantindo rastreabilidade e reprodutibilidade.

## 4. Fontes Oficiais Utilizadas
* **SIDRA / IBGE:** Tabelas de Estimativas Populacionais, Censo Demográfico (Características da População e Domicílios), e Estatísticas do Registro Civil.
* **Endereços de Acesso:** 
  * API SIDRA: `https://servicodados.ibge.gov.br/api/v3/agregados`
  * Portal SIDRA: `https://sidra.ibge.gov.br`

## 5. Quantidade de Registros Válidos
A base tratada contém **1.048 registros reais** consolidados, cobrindo múltiplas variáveis, faixas etárias, anos de referência e recortes territoriais oficiais, sem qualquer duplicação ou simulação artificial de dados.

## 6. Dicionário das Variáveis
| Coluna | Descrição |
| :--- | :--- |
| `ID` | Identificador único sequencial do registro |
| `Município` | Nome padronizado do município amazonense |
| `Estado` | Unidade da Federação (Amazonas) |
| `Ano` | Ano de referência da coleta ou censo |
| `Localidade` | Recorte espacial (Urbana / Rural / Total / Sede Municipal) |
| `Tipo de informação` | Categoria estatística: População, Demografia, Domicílios ou Deslocamento |
| `Quantidade` | Valor numérico absoluto ou percentual observado |
| `Unidade` | Unidade de medida (Pessoas, Domicílios, % etc.) |
| `Fonte` | Base de origem oficial (IBGE / SIDRA / Censo) |
| `Código IBGE` | Código geocodificado oficial de 7 dígitos do município |

## 7. Limitações dos Dados
* Ausência de séries temporais contínuas anuais de fluxo turístico fluvial específico para todos os municípios da calha.
* Necessidade de agregação cruzada entre dados censitários (2010 e 2022) e pesquisas amostrais para atingir robustez estatística de longo alcance.

## 8. Resultados Encontrados
A análise permitiu mapear o crescimento demográfico acentuado na capital (Manaus) em contraponto à alta dispersão territorial e demográfica dos municípios a jusante e montante do Rio Negro (Barcelos, Santa Isabel e São Gabriel), evidenciando os gargalos logísticos e de infraestrutura básica.
