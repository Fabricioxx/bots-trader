import pandas as pd
import ta

def analisar_mercado(df):
    df['ma9'] = ta.trend.sma_indicator(df['close'], window=9)
    df['ma21'] = ta.trend.sma_indicator(df['close'], window=21)
    df['rsi'] = ta.momentum.rsi(df['close'], window=14)
    df['volume_ma'] = df['volume'].rolling(window=20).mean()

    ult = df.iloc[-1]
    penult = df.iloc[-2]

    # Compra: cruzamento de médias + rsi bom + volume forte
    if penult['ma9'] < penult['ma21'] and ult['ma9'] > ult['ma21']:
        if 50 < ult['rsi'] < 65 and ult['volume'] > ult['volume_ma']:
            return 'compra'

    # Venda: cruzamento para baixo + rsi ruim + volume forte
    if penult['ma9'] > penult['ma21'] and ult['ma9'] < ult['ma21']:
        if 35 < ult['rsi'] < 50 and ult['volume'] > ult['volume_ma']:
            return 'venda'

    return 'manter'
