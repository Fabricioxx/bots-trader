import yfinance as yf
import pandas as pd
import ta
import matplotlib.pyplot as plt
from estrategia import aplicar_estrategia

def carregar_dados():
    df = yf.download("BTC-USD", interval="1h", period="60d", auto_adjust=False)
    df = df[['Close', 'Volume']]
    df = df.rename(columns={"Close": "close", "Volume": "volume"})
    df['close'] = pd.to_numeric(df['close'], errors='coerce')
    df['volume'] = pd.to_numeric(df['volume'], errors='coerce')
    return df

def simular_com_grafico(df):
    capital = 10000
    btc = 0
    posicao = "neutro"
    historico_capital = []

    for i in range(len(df)):
        preco = df['close'].iat[i]
        sinal = df['sinal'].iat[i]

        if sinal == "compra" and posicao != "comprado":
            btc = capital / preco
            capital = 0
            posicao = "comprado"

        elif sinal == "venda" and posicao == "comprado":
            capital = btc * preco
            btc = 0
            posicao = "vendido"

        total = capital if posicao != "comprado" else btc * preco
        historico_capital.append(total)

    # Plotar gráfico
    plt.figure(figsize=(12,6))
    plt.plot(df.index, historico_capital, label="Capital ($)")
    plt.title("Backtest Estratégia 80/20 - Capital ao Longo do Tempo")
    plt.xlabel("Data")
    plt.ylabel("Capital em $")
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"Capital final: ${historico_capital[-1]:.2f}")

# Uso centralizado da estratégia

df = carregar_dados()
df = aplicar_estrategia(df)
simular_com_grafico(df)
