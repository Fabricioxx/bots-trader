# Tutorial Completo do Projeto Trading Bot 80/20

Este tutorial irá guiá-lo passo a passo para instalar, configurar, rodar, analisar e monitorar o seu robô trader Python para a Binance, com estratégia baseada no Princípio de Pareto (80/20), stop loss, take profit, logs e painel web interativo.

---

## 1. Pré-requisitos

- Python 3.8+
- Conta na Binance Testnet ([crie aqui](https://testnet.binance.vision/))
- Chave de API e Secret da Testnet

---

## 2. Instalação

Abra o terminal na pasta do projeto e execute:

```powershell
pip install -r requirements.txt
```

---

## 3. Configuração

Edite o arquivo `config.py` e coloque sua API Key e Secret da Binance Testnet:

```python
API_KEY = "SUA_API_KEY"
API_SECRET = "SEU_API_SECRET"
BASE_URL = "https://testnet.binance.vision"
SYMBOL = "BTCUSDT"  # Ou outro par suportado
QUANTIDADE = 0.001   # Ajuste conforme seu saldo
```

---

## 4. Rodando o Bot

Execute o bot principal:

```powershell
python bot.py
```

O bot irá:
- Buscar dados de mercado a cada minuto
- Tomar decisões baseadas na estratégia 80/20
- Executar ordens reais na Testnet
- Aplicar stop loss e take profit automáticos
- Registrar todas as operações e decisões em logs

---

## 5. Monitorando via Painel Web

Execute o painel web interativo:

```powershell
streamlit run app.py
```

- Visualize o preço em tempo real
- Veja as últimas operações do bot
- Acompanhe sinais e posição atual

---

## 6. Backtest da Estratégia

Para simular a estratégia com dados históricos e visualizar o desempenho:

```powershell
python backtest_grafico.py
```

- O script irá baixar dados históricos do BTC/USD
- Aplicar a estratégia 80/20
- Exibir um gráfico da evolução do capital

---

## 7. Estrutura dos Arquivos

- `bot.py`: Bot principal com controle de posição, stop loss, take profit e logs
- `estrategia.py`: Lógica da estratégia 80/20 (médias móveis, RSI, volume)
- `binance_client.py`: Interface com a API da Binance
- `config.py`: Configurações gerais (API, símbolo, quantidade)
- `logs/`: Logs detalhados das operações
- `app.py`: Painel web interativo com Streamlit
- `backtest_grafico.py`: Backtest com gráfico de capital
- `requirements.txt`: Dependências do projeto

---

## 8. Dicas de Segurança

- Nunca compartilhe seu `config.py` publicamente
- Use sempre a Testnet para testes
- Para operar com dinheiro real, revise e adapte o código com cautela

---

## 9. Personalizações e Expansões

- Para múltiplos ativos, duplique o bloco de execução do bot para cada símbolo desejado
- Ajuste os parâmetros de stop loss/take profit em `bot.py`
- Implemente novas estratégias em `estrategia.py`
- Expanda o painel web para mostrar mais métricas

---

## 10. Suporte

Abra issues ou contribua no repositório do projeto para dúvidas e melhorias!
