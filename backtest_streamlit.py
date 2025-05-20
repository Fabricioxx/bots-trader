import yfinance as yf
import pandas as pd
import ta
import matplotlib.pyplot as plt
import logging
import streamlit as st
from estrategia import aplicar_estrategia

# CONFIG LOG
dados_log = 'backtest_streamlit.log'
logging.basicConfig(filename=dados_log, level=logging.INFO,
                    format='%(asctime)s - %(message)s')

# PARAMETROS
STOP_LOSS_PCT = 0.02  # 2%
TAKE_PROFIT_PCT = 0.04  # 4%
CAPITAL_INICIAL = 10000

# FUNÇÕES

def carregar_dados():
    df = yf.download("BTC-USD", interval="1h", period="30d", auto_adjust=False)
    df = df[['Close', 'Volume']]
    df = df.rename(columns={"Close": "close", "Volume": "volume"})
    df['close'] = pd.to_numeric(df['close'], errors='coerce')
    df['volume'] = pd.to_numeric(df['volume'], errors='coerce')
    return df


def simular(df):
    capital = CAPITAL_INICIAL
    btc = 0
    posicao = "neutro"
    preco_entrada = 0
    historico = []

    for i in range(len(df)):
        preco = df['close'].iat[i]
        sinal = df['sinal'].iat[i]
        data = df.index[i]

        if posicao == "comprado":
            if preco <= preco_entrada * (1 - STOP_LOSS_PCT):
                capital = btc * preco
                btc = 0
                posicao = "vendido"
                logging.info(f"STOP LOSS em {preco:.2f}")
            elif preco >= preco_entrada * (1 + TAKE_PROFIT_PCT):
                capital = btc * preco
                btc = 0
                posicao = "vendido"
                logging.info(f"TAKE PROFIT em {preco:.2f}")

        if sinal == "compra" and posicao != "comprado":
            btc = capital / preco
            capital = 0
            preco_entrada = preco
            posicao = "comprado"
            logging.info(f"Compra em {preco:.2f}")

        elif sinal == "venda" and posicao == "comprado":
            capital = btc * preco
            btc = 0
            posicao = "vendido"
            logging.info(f"Venda em {preco:.2f}")

        total = capital if posicao != "comprado" else btc * preco
        historico.append({"data": data, "capital": total})

    return pd.DataFrame(historico).set_index("data")

# APP STREAMLIT
st.set_page_config(page_title="Bot Trader 80/20", layout="wide")
st.title("Painel do Bot Trader - Estratégia 80/20")

st.markdown("""
Este painel mostra o desempenho do backtest de uma estratégia baseada no princípio de Pareto (80/20), com stop loss e take profit.
""")

with st.spinner("Carregando dados e rodando backtest..."):
    df = carregar_dados()
    df = aplicar_estrategia(df)
    resultado = simular(df)

col1, col2 = st.columns(2)

col1.metric("Capital Inicial", f"${CAPITAL_INICIAL:,.2f}")
col2.metric("Capital Final", f"${resultado['capital'].iloc[-1]:,.2f}")

st.line_chart(resultado['capital'])

with st.expander("🔍 Ver sinais de compra e venda"):
    st.dataframe(df[['close', 'sinal']].tail(100))
