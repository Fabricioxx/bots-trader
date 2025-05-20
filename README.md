# Trading Bot 80/20 - Projeto Completo

Este projeto é um robô de trading em Python para a Binance, com foco em operar apenas nos 20% dos momentos de maior probabilidade de sucesso (Princípio de Pareto 80/20). O bot utiliza confluência de médias móveis, RSI e volume, executa ordens reais na Testnet, possui controle de posição, stop loss, take profit, logs detalhados, painel web e scripts de backtest.

## Como começar

1. **Pré-requisitos:**
   - Python 3.8+
   - Conta na Binance Testnet ([crie aqui](https://testnet.binance.vision/))
   - Chave de API e Secret da Testnet

2. **Instalação:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Configuração:**
   Edite o arquivo `config.py` e coloque sua API Key e Secret da Binance Testnet:
   ```python
   API_KEY = "SUA_API_KEY"
   API_SECRET = "SEU_API_SECRET"
   BASE_URL = "https://testnet.binance.vision"
   SYMBOL = "BTCUSDT"  # Ou outro par suportado
   QUANTIDADE = 0.001   # Ajuste conforme seu saldo
   ```

4. **Rodando o Bot:**
   ```powershell
   python bot.py
   ```
   O bot irá:
   - Buscar dados de mercado a cada minuto
   - Tomar decisões baseadas na estratégia 80/20
   - Executar ordens reais na Testnet
   - Aplicar stop loss e take profit automáticos
   - Registrar todas as operações e decisões em logs
   - Persistir o estado da posição para evitar erros em reinícios

5. **Monitorando via Painel Web:**
   ```powershell
   streamlit run app.py
   ```
   - Visualize o preço em tempo real
   - Veja as últimas operações do bot
   - Acompanhe sinais e posição atual

6. **Backtest da Estratégia:**
   - Simulação simples:
     ```powershell
     python backtest.py
     ```
   - Com gráfico:
     ```powershell
     python backtest_grafico.py
     ```
   - Painel interativo:
     ```powershell
     streamlit run backtest_streamlit.py
     ```

## Estrutura dos Arquivos

- `bot.py`: Bot principal com controle de posição, stop loss, take profit, logs e persistência de estado
- `estrategia.py`: Lógica centralizada da estratégia 80/20 (médias móveis, RSI, volume)
- `binance_client.py`: Interface com a API da Binance
- `config.py`: Configurações gerais (API, símbolo, quantidade)
- `logs/`: Logs detalhados das operações e estado
- `app.py`: Painel web interativo com Streamlit para monitorar o bot
- `backtest.py`: Backtest simples da estratégia
- `backtest_grafico.py`: Backtest com gráfico da evolução do capital
- `backtest_streamlit.py`: Painel interativo do backtest
- `requirements.txt`: Dependências do projeto
- `.gitignore`: Protege arquivos sensíveis e desnecessários

## Estratégia 80/20 implementada

- **Compra:**
  - MA9 cruza para cima a MA21
  - RSI entre 50 e 65
  - Volume acima da média dos últimos 20 candles
- **Venda:**
  - MA9 cruza para baixo a MA21
  - RSI entre 35 e 50
  - Volume acima da média dos últimos 20 candles
- **Mantém posição:**
  - Se nenhuma das condições acima for atendida

## Segurança
- O bot opera apenas na Testnet da Binance por padrão
- As credenciais ficam no arquivo `config.py` (NUNCA compartilhe este arquivo publicamente)
- `.gitignore` já protege arquivos sensíveis

## Personalizações e Expansões
- Para múltiplos ativos, duplique o bloco de execução do bot para cada símbolo desejado
- Ajuste os parâmetros de stop loss/take profit em `bot.py`
- Implemente novas estratégias em `estrategia.py`
- Expanda o painel web para mostrar mais métricas

## Suporte
Abra issues ou contribua no repositório do projeto para dúvidas e melhorias!
