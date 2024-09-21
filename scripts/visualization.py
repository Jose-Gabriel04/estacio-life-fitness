import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import sqlite3

# Função para criar gráficos interativos com Plotly
def plot_usage_trends(db_file):
    conn = sqlite3.connect(db_file)
    query = "SELECT date, usage_count FROM cleaned_data"
    data = pd.read_sql(query, conn)
    
    # Gráfico interativo de tendências de uso
    fig = px.line(data, x='date', y='usage_count', title="Tendência de Uso por Data")
    fig.show()

    conn.close()

# Exemplo de uso
if __name__ == "__main__":
    plot_usage_trends("data/processed/life_fitness.db")
