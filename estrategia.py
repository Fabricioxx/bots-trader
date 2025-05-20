import pandas as pd
import ta

def analisar_mercado(df):
    """
    Analisa o DataFrame de candles e retorna o sinal de operação ('compra', 'venda', 'manter').
    Estratégia baseada em cruzamento de médias, RSI e volume.
    """
    # Garantir que as colunas estejam 1-D e numéricas
    df['close'] = pd.to_numeric(df['close'], errors='coerce')
    df['volume'] = pd.to_numeric(df['volume'], errors='coerce')
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

def aplicar_estrategia(df):
    """
    Marca o sinal de cada candle no DataFrame ('compra', 'venda', 'manter').
    Pode ser usada em backtests.
    """
    df['close'] = pd.to_numeric(df['close'], errors='coerce')
    df['volume'] = pd.to_numeric(df['volume'], errors='coerce')
    df['ma9'] = ta.trend.sma_indicator(df['close'], window=9)
    df['ma21'] = ta.trend.sma_indicator(df['close'], window=21)
    df['rsi'] = ta.momentum.rsi(df['close'], window=14)
    df['volume_ma'] = df['volume'].rolling(window=20).mean()
    df['sinal'] = 'manter'
    for i in range(1, len(df)):
        if df['ma9'].iat[i-1] < df['ma21'].iat[i-1] and df['ma9'].iat[i] > df['ma21'].iat[i]:
            if 50 < df['rsi'].iat[i] < 65 and df['volume'].iat[i] > df['volume_ma'].iat[i]:
                df.at[df.index[i], 'sinal'] = 'compra'
        elif df['ma9'].iat[i-1] > df['ma21'].iat[i-1] and df['ma9'].iat[i] < df['ma21'].iat[i]:
            if 35 < df['rsi'].iat[i] < 50 and df['volume'].iat[i] > df['volume_ma'].iat[i]:
                df.at[df.index[i], 'sinal'] = 'venda'
    return df
