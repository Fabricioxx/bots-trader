# Trading Bot

Este projeto é um bot de trading em Python para a Binance, focado em operar apenas nos 20% dos momentos de maior probabilidade de sucesso, segundo o Princípio de Pareto (80/20). Ele utiliza confluência de médias móveis, força da tendência (RSI) e volume acima da média para tomar decisões. O bot executa ordens reais na Testnet da Binance, possui estrutura modular, registra logs das operações e agora conta com backtest gráfico.

## Como começar

1. Certifique-se de ter o Python instalado.
2. Instale as dependências necessárias:
   ```powershell
   pip install -r requirements.txt
   ```
3. Configure sua API Key e Secret da Binance Testnet no arquivo `config.py`.
4. Execute o bot com:
   ```powershell
   python bot.py
   ```

## Estrutura de arquivos

- `bot.py`: Código principal, responsável pelo loop de execução, coleta de dados, decisão e execução de ordens.
- `estrategia.py`: Implementa a lógica da estratégia 80/20 (cruzamento de médias, RSI, volume).
- `binance_client.py`: Interface de conexão com a API da Binance.
- `config.py`: Configurações gerais (API Key, Secret, símbolo, quantidade, URL da Testnet).
- `logs/`: Pasta onde são salvos os logs das operações realizadas.
- `requirements.txt`: Lista de dependências do projeto.
- `backtest.py`: Script para simular a estratégia com dados históricos e mostrar o resultado final.
- `backtest_grafico.py`: Script para simular a estratégia e exibir um gráfico da evolução do capital ao longo do tempo.

## Estratégia 80/20 implementada

O robô só opera quando há forte confluência de sinais, buscando os 20% dos momentos mais favoráveis:

### Compra
- Média móvel curta (MA9) cruza para cima a longa (MA21)
- RSI entre 50 e 65 (momentum positivo, sem sobrecompra)
- Volume atual acima da média dos últimos 20 candles

### Venda
- Média móvel curta (MA9) cruza para baixo a longa (MA21)
- RSI entre 35 e 50 (momentum negativo, sem sobrevenda)
- Volume atual acima da média dos últimos 20 candles

### Mantém posição
- Se nenhuma das condições acima for atendida, o bot não executa ordens.

## Controle de posição inteligente

O bot mantém o estado da posição atual (`comprado`, `vendido` ou `neutro`) e só executa uma nova ordem se houver mudança real de direção, evitando ordens repetidas.

## Backtest e análise gráfica

- `backtest.py`: Simula a estratégia com dados históricos do BTC/USD (últimos 60 dias, candles de 1h) e mostra o capital final.
- `backtest_grafico.py`: Além da simulação, exibe um gráfico da evolução do capital ao longo do tempo usando Matplotlib.

### Como rodar o backtest gráfico

1. Instale as dependências:
   ```powershell
   pip install -r requirements.txt
   ```
2. Execute:
   ```powershell
   python backtest_grafico.py
   ```

O script irá baixar os dados históricos, aplicar a estratégia e mostrar um gráfico do desempenho do capital.

## Segurança
- O bot opera apenas na Testnet da Binance por padrão, evitando riscos financeiros reais.
- As credenciais ficam no arquivo `config.py` (NUNCA compartilhe este arquivo publicamente).

## Próximos passos sugeridos
- Adicionar stop loss e take profit automáticos
- Criar dashboards e relatórios interativos
- Fazer backtests com outros ativos e períodos
- Subir para um VPS para rodar 24/7

## Observações
- Este projeto está em desenvolvimento inicial.
- Sinta-se à vontade para sugerir melhorias ou abrir issues.
