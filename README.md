# Life Fitness Data Analysis

## Descrição do Projeto

O **Life Fitness Data Analysis** é um projeto de análise de dados desenvolvido para a rede de academias Life Fitness. O objetivo é coletar, processar e visualizar dados de clientes, fornecendo insights valiosos para os gerentes e colaboradores tomarem decisões estratégicas baseadas em dados.

## Tecnologias Utilizadas

- **Python**: Linguagem principal.
  - `pandas`: Manipulação e análise de dados.
  - `numpy`: Operações numéricas.
  - `matplotlib` e `plotly`: Visualizações interativas.
  - `sqlite3`: Gerenciamento de banco de dados.
  - `streamlit`: Interface web interativa.
  
## Estrutura do Projeto
life_fitness_data_analysis/
├── data/                       
│   ├── raw/                    # Dados brutos
│   └── processed/              # Dados processados
├── notebooks/                  
├── scripts/                    
├── app/                        
├── requirements.txt            
└── README.md

## Como executar o projeto:
pip install -r requirements.txt
python scripts/data_collection.py
python scripts/data_processing.py
python scripts/data_analysis.py
streamlit run app/streamlit_app.py