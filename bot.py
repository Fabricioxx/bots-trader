import time
import pandas as pd
from binance_client import client
from estrategia import analisar_mercado
from config import SYMBOL, QUANTIDADE
import os
from datetime import datetime

LOG_DIR = 'logs'
os.makedirs(LOG_DIR, exist_ok=True)

def obter_candles():
    klines = client.get_klines(symbol=SYMBOL, interval='1m', limit=100)
    df = pd.DataFrame(klines, columns=[
        'time','o','h','l','c','v','ct','qav','nt','tbbav','tbqav','ignore'])
    df['close'] = df['c'].astype(float)
    df['volume'] = df['v'].astype(float)
    return df[['close', 'volume']]

def executar_ordem(tipo):
    try:
        if tipo == 'compra':
            ordem = client.order_market_buy(symbol=SYMBOL, quantity=QUANTIDADE)
        elif tipo == 'venda':
            ordem = client.order_market_sell(symbol=SYMBOL, quantity=QUANTIDADE)
        print(f"Ordem executada: {ordem}")
        log_ordem(tipo, ordem)
    except Exception as e:
        print("Erro ao executar ordem:", e)
        log_ordem(tipo, str(e))

def log_ordem(tipo, info):
    with open(os.path.join(LOG_DIR, f"{SYMBOL}_trades.log"), 'a') as f:
        f.write(f"{datetime.now()} - {tipo.upper()} - {info}\n")

# Loop principal
enquanto_rodar = True
while enquanto_rodar:
    df = obter_candles()
    decisao = analisar_mercado(df)
    print(f"Decisão: {decisao}")

    if decisao in ['compra', 'venda']:
        executar_ordem(decisao)

    time.sleep(60)
