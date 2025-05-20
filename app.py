import streamlit as st
import pandas as pd
import yfinance as yf
import os

st.set_page_config(page_title="Painel Bot Trader 80/20", layout="wide")
st.title("Painel Bot Trader 80/20")

# Exibe preço do BTC
df = yf.download("BTC-USD", interval="1m", period="1d")
df = df[['Close', 'Volume']]
st.line_chart(df['Close'], use_container_width=True)

# Exibe sinais e posição atual a partir dos logs
log_path = os.path.join('logs', 'BTCUSDT_trades.log')
if os.path.exists(log_path):
    with open(log_path) as f:
        logs = f.readlines()
    st.subheader("Últimas operações")
    st.text(''.join(logs[-10:]))
else:
    st.info("Nenhum log encontrado ainda.")

st.write("Aqui você pode acompanhar o preço, sinais e últimas operações do bot em tempo real.")
