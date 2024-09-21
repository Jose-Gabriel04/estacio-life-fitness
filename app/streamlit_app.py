import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# Função para carregar dados do SQLite
def load_data(db_file):
    conn = sqlite3.connect(db_file)
    query = "SELECT * FROM cleaned_data"
    data = pd.read_sql(query, conn)
    conn.close()
    return data

# Configuração do App Streamlit
st.title("Análise de Dados da Life Fitness")
st.subheader("Tendência de Uso dos Clientes")

# Carregar e exibir os dados
data = load_data("data/processed/life_fitness.db")
st.dataframe(data.head())

# Criar visualização interativa
fig = px.line(data, x='date', y='usage_count', title="Tendência de Uso por Data")
st.plotly_chart(fig)
