import time
import pandas as pd
from binance_client import client
from estrategia import analisar_mercado
from config import SYMBOL, QUANTIDADE
import os
from datetime import datetime
import logging

LOG_DIR = 'logs'
os.makedirs(LOG_DIR, exist_ok=True)

# Configuração de logging detalhado
logging.basicConfig(filename=os.path.join(LOG_DIR, f'{SYMBOL}_trading_bot.log'),
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Parâmetros de risco
STOP_LOSS_PCT = 0.02  # 2%
TAKE_PROFIT_PCT = 0.04  # 4%

# Controle de posição
posicao_atual = "neutro"  # ou "comprado" / "vendido"
preco_entrada = 0

def obter_candles():
    klines = client.get_klines(symbol=SYMBOL, interval='1m', limit=100)
    df = pd.DataFrame(klines, columns=[
        'time','o','h','l','c','v','ct','qav','nt','tbbav','tbqav','ignore'])
    df['close'] = df['c'].astype(float)
    df['volume'] = df['v'].astype(float)
    return df[['close', 'volume']]

def executar_ordem(tipo, preco=None):
    try:
        if tipo == 'compra':
            ordem = client.order_market_buy(symbol=SYMBOL, quantity=QUANTIDADE)
        elif tipo == 'venda':
            ordem = client.order_market_sell(symbol=SYMBOL, quantity=QUANTIDADE)
        print(f"Ordem executada: {ordem}")
        logging.info(f"Ordem {tipo.upper()} executada: {ordem}")
        log_ordem(tipo, ordem)
    except Exception as e:
        print("Erro ao executar ordem:", e)
        logging.error(f"Erro ao executar ordem {tipo.upper()}: {e}")
        log_ordem(tipo, str(e))

def log_ordem(tipo, info):
    with open(os.path.join(LOG_DIR, f"{SYMBOL}_trades.log"), 'a') as f:
        f.write(f"{datetime.now()} - {tipo.upper()} - {info}\n")

while True:
    df = obter_candles()
    decisao = analisar_mercado(df)
    preco_atual = df['close'].iloc[-1]
    print(f"Decisão: {decisao} | Posição atual: {posicao_atual} | Preço: {preco_atual}")
    logging.info(f"Decisão: {decisao} | Posição atual: {posicao_atual} | Preço: {preco_atual}")

    # Stop Loss e Take Profit automáticos
    if posicao_atual == "comprado":
        if preco_atual <= preco_entrada * (1 - STOP_LOSS_PCT):
            print(f"STOP LOSS ativado a {preco_atual:.2f}")
            logging.info(f"STOP LOSS ativado a {preco_atual:.2f}")
            executar_ordem("venda", preco_atual)
            posicao_atual = "vendido"
        elif preco_atual >= preco_entrada * (1 + TAKE_PROFIT_PCT):
            print(f"TAKE PROFIT ativado a {preco_atual:.2f}")
            logging.info(f"TAKE PROFIT ativado a {preco_atual:.2f}")
            executar_ordem("venda", preco_atual)
            posicao_atual = "vendido"

    if decisao == "compra" and posicao_atual != "comprado":
        executar_ordem("compra", preco_atual)
        posicao_atual = "comprado"
        preco_entrada = preco_atual
        logging.info(f"Compra executada a {preco_entrada:.2f}")

    elif decisao == "venda" and posicao_atual == "comprado":
        executar_ordem("venda", preco_atual)
        posicao_atual = "vendido"
        logging.info(f"Venda executada a {preco_atual:.2f}")

    time.sleep(60)
