import pandas as pd
import sqlite3

# Função para limpar os dados
def clean_data(db_file):
    conn = sqlite3.connect(db_file)
    query = "SELECT * FROM customer_data"
    data = pd.read_sql(query, conn)
    
    # Exemplo de limpeza: removendo valores nulos e duplicados
    data.dropna(inplace=True)
    data.drop_duplicates(inplace=True)
    
    data.to_sql('cleaned_data', conn, if_exists='replace', index=False)
    conn.close()
    print("Dados limpos e salvos no banco de dados")

# Exemplo de uso
if __name__ == "__main__":
    clean_data("data/processed/life_fitness.db")
