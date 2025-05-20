import yfinance as yf
import pandas as pd
from estrategia import aplicar_estrategia

def carregar_dados():
    df = yf.download("BTC-USD", interval="1h", period="60d")
    df = df[['Close', 'Volume']]
    df = df.rename(columns={"Close": "close", "Volume": "volume"})
    return df

def simular(df):
    capital = 10000
    btc = 0
    posicao = "neutro"

    for i in range(len(df)):
        preco = df['close'].iloc[i]
        sinal = df['sinal'].iloc[i]

        if sinal == "compra" and posicao != "comprado":
            btc = capital / preco
            capital = 0
            posicao = "comprado"
            print(f"{df.index[i]} | COMPRA a {preco:.2f}")

        elif sinal == "venda" and posicao == "comprado":
            capital = btc * preco
            btc = 0
            posicao = "vendido"
            print(f"{df.index[i]} | VENDA a {preco:.2f}")

    # Valor final
    total = capital if posicao != "comprado" else btc * df['close'].iloc[-1]
    print(f"\nCapital final: ${total:.2f}")

df = carregar_dados()
df = aplicar_estrategia(df)
simular(df)
