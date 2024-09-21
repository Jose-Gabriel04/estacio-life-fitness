import pandas as pd
import sqlite3

# Função para análise simples dos dados
def analyze_data(db_file):
    conn = sqlite3.connect(db_file)
    query = "SELECT * FROM cleaned_data"
    data = pd.read_sql(query, conn)
    
    # Exemplo de análise: resumo estatístico
    print(data.describe())
    
    # Análise de tendência de uso
    usage_trends = data.groupby('date')['usage_count'].sum()
    print(usage_trends)
    
    conn.close()

# Exemplo de uso
if __name__ == "__main__":
    analyze_data("data/processed/life_fitness.db")
