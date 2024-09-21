import pandas as pd
import sqlite3

# Função para carregar dados de um arquivo CSV para o SQLite
def load_data_to_db(csv_file, db_file):
    conn = sqlite3.connect(db_file)
    data = pd.read_csv(csv_file)
    data.to_sql('customer_data', conn, if_exists='replace', index=False)
    conn.close()
    print(f"Dados de {csv_file} carregados para {db_file}")

# Exemplo de uso
if __name__ == "__main__":
    load_data_to_db("data/raw/customer_data.csv", "data/processed/life_fitness.db")