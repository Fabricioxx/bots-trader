# 🤖 Trading Bot 80/20 — Projeto Completo

Automatize operações na Binance Testnet utilizando o princípio de Pareto (80/20): foque apenas nos 20% dos momentos com maior probabilidade de sucesso! O bot combina médias móveis, RSI e volume, executa ordens reais (Testnet), possui painel web, logs completos, scripts de backtest, controle de risco e alta personalização.

---

## ✨ Principais Funcionalidades

- Estratégia 80/20: opera só nos melhores sinais com confluência de indicadores.
- Ordens reais na Testnet da Binance.
- Controle de posição, stop loss, take profit e persistência de estado.
- Painel web interativo via Streamlit.
- Logs detalhados.
- Scripts de backtest com e sem visualização gráfica.
- Estrutura modular, fácil de personalizar.

---

## 🚀 Como começar

### 1. Pré-requisitos

- Python 3.8+
- Conta na Binance Testnet ([crie aqui](https://testnet.binance.vision/))
- Chave de API e Secret da Testnet

### 2. Instalação

```bash
pip install -r requirements.txt
```

### 3. Configuração

Edite o arquivo `config.py` e coloque suas credenciais:

```python
API_KEY = "SUA_API_KEY"
API_SECRET = "SEU_API_SECRET"
BASE_URL = "https://testnet.binance.vision"
SYMBOL = "BTCUSDT"    # Ou outro par suportado
QUANTIDADE = 0.001    # Ajuste conforme seu saldo
```

### 4. Rodando o Bot

```bash
python bot.py
```

O bot irá:

- Buscar dados de mercado a cada minuto
- Tomar decisões baseadas na estratégia 80/20
- Executar ordens reais na Testnet
- Aplicar stop loss e take profit automáticos
- Registrar operações e decisões em logs
- Persistir o estado da posição

### 5. Painel Web Interativo

```bash
streamlit run app.py
```

- Visualize preços em tempo real
- Veja operações recentes do bot
- Acompanhe sinais e posição atual

### 6. Backtest da Estratégia

- Simulação simples:
  ```bash
  python backtest.py
  ```
- Com gráfico:
  ```bash
  python backtest_grafico.py
  ```
- Painel interativo:
  ```bash
  streamlit run backtest_streamlit.py
  ```

---

## 🗂️ Estrutura dos Arquivos

- `bot.py` — Bot principal, controle de posição, stop, logs e persistência
- `estrategia.py` — Estratégia 80/20 (médias móveis, RSI, volume)
- `binance_client.py` — Interface com API da Binance
- `config.py` — Configuração (API, símbolo, quantidade)
- `logs/` — Logs das operações
- `app.py` — Painel web (Streamlit)
- `backtest.py` — Backtest simples
- `backtest_grafico.py` — Backtest com gráfico
- `backtest_streamlit.py` — Painel interativo do backtest
- `requirements.txt` — Dependências
- `.gitignore` — Protege arquivos sensíveis

---

## 📈 Estratégia 80/20 Implementada

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

### Diferenciais

- Foco só nos sinais de alta probabilidade (evita overtrading)
- Critérios claros, reduz decisões emocionais
- Gestão de risco automática (stop e take profit)
- Parâmetros facilmente ajustáveis

---

## 🔒 Segurança

- Roda apenas na Testnet da Binance por padrão
- Credenciais no `config.py` (NUNCA compartilhe publicamente)
- `.gitignore` já protege arquivos sensíveis

---

## 🛠️ Personalizações e Expansões

- Para operar múltiplos ativos, duplique o bloco do bot para cada símbolo
- Ajuste stops/take profit em `bot.py`
- Implemente novas estratégias em `estrategia.py`
- Expanda o painel web para mais métricas

---

## 📚 Documentação e Suporte

- Consulte o arquivo `tutorial.md` para passo a passo detalhado.
- Detalhes da lógica em `estrategia.md`.
- Abra issues ou contribua para melhorias!

---

## ❤️ Contribuição

Pull requests são bem-vindos. Para discussões ou dúvidas, utilize as issues do repositório.

---

**Desenvolvido por [Fabricioxx](https://github.com/Fabricioxx) • Projeto open source**
