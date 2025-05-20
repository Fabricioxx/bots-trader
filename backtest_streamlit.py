import yfinance as yf
import pandas as pd
import ta
import matplotlib.pyplot as plt
import logging
import streamlit as st

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
    df = yf.download("BTC-USD", interval="1h", period="30d")
    df = df[['Close', 'Volume']]
    df = df.rename(columns={"Close": "close", "Volume": "volume"})
    return df

def aplicar_estrategia(df):
    df['ma9'] = ta.trend.sma_indicator(df['close'], window=9)
    df['ma21'] = ta.trend.sma_indicator(df['close'], window=21)
    df['rsi'] = ta.momentum.rsi(df['close'], window=14)
    df['volume_ma'] = df['volume'].rolling(window=20).mean()
    df['sinal'] = 'manter'

    for i in range(1, len(df)):
        if df['ma9'].iloc[i-1] < df['ma21'].iloc[i-1] and df['ma9'].iloc[i] > df['ma21'].iloc[i]:
            if 50 < df['rsi'].iloc[i] < 65 and df['volume'].iloc[i] > df['volume_ma'].iloc[i]:
                df.at[df.index[i], 'sinal'] = 'compra'
        elif df['ma9'].iloc[i-1] > df['ma21'].iloc[i-1] and df['ma9'].iloc[i] < df['ma21'].iloc[i]:
            if 35 < df['rsi'].iloc[i] < 50 and df['volume'].iloc[i] > df['volume_ma'].iloc[i]:
                df.at[df.index[i], 'sinal'] = 'venda'
    return df

def simular(df):
    capital = CAPITAL_INICIAL
    btc = 0
    posicao = "neutro"
    preco_entrada = 0
    historico = []

    for i in range(len(df)):
        preco = df['close'].iloc[i]
        sinal = df['sinal'].iloc[i]
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
