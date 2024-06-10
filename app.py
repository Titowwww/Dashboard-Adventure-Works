import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from sqlalchemy import create_engine

st.set_option('deprecation.showPyplotGlobalUse', False)

db_conn_str = 'mysql+mysqlconnector://root:@localhost:3306/aw'
engine = create_engine(db_conn_str)

st.title('Adventure Works Dashboard')

dimsalesterritory_query = 'SELECT SalesTerritoryRegion, SalesTerritoryKey FROM dimsalesterritory'
dimsalesterritory = pd.read_sql(dimsalesterritory_query, engine)

factinternetsales_query = 'SELECT SalesAmount, SalesTerritoryKey FROM factinternetsales'
factinternetsales = pd.read_sql(factinternetsales_query, engine)

df = pd.merge(factinternetsales, dimsalesterritory, on  = 'SalesTerritoryKey')

# Mengambil list unik dari region
regions = df['SalesTerritoryRegion'].unique()

# Membuat dropdown di Streamlit
selected_region = st.selectbox('Select Region', regions)

# filtering data berdasarkan region yang dipilih
filtered_data = df[df['SalesTerritoryRegion'] == selected_region]

# Menampilkan beberapa baris pertama dari data yang disaring
st.write(filtered_data.head())

# Membuat visualisasi menggunakan Seaborn
plt.figure(figsize=(10, 6))
sns.barplot(data=filtered_data, x='SalesTerritoryRegion', y='SalesAmount', ci=None)
plt.title(f'Sales Amount in {selected_region}')
plt.xlabel('Region')
plt.ylabel('Sales Amount')

# Menampilkan plot di Streamlit
st.pyplot(plt)
