# Trading Bot

Este projeto é um bot de trading em Python para a Binance, focado em operar apenas nos 20% dos momentos de maior probabilidade de sucesso, segundo o Princípio de Pareto (80/20). Ele utiliza confluência de médias móveis, força da tendência (RSI) e volume acima da média para tomar decisões. O bot executa ordens reais na Testnet da Binance, possui estrutura modular e registra logs das operações.

## Como começar

1. Certifique-se de ter o Python instalado.
2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure sua API Key e Secret da Binance Testnet no arquivo `config.py`.
4. Execute o bot com:
   ```bash
   python bot.py
   ```

## Estrutura de arquivos

- `bot.py`: Código principal, responsável pelo loop de execução, coleta de dados, decisão e execução de ordens.
- `estrategia.py`: Implementa a lógica da estratégia 80/20 (cruzamento de médias, RSI, volume).
- `binance_client.py`: Interface de conexão com a API da Binance.
- `config.py`: Configurações gerais (API Key, Secret, símbolo, quantidade, URL da Testnet).
- `logs/`: Pasta onde são salvos os logs das operações realizadas.
- `requirements.txt`: Lista de dependências do projeto.

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

## Como funciona o código

- O `bot.py` executa um loop a cada 1 minuto:
  1. Busca os últimos candles do ativo na Binance Testnet.
  2. Chama a função `analisar_mercado` da `estrategia.py` para decidir se deve comprar, vender ou manter.
  3. Se a decisão for comprar ou vender, executa a ordem via API e registra no log.
  4. Todos os resultados e erros são salvos em arquivos de log na pasta `logs/`.

- O `estrategia.py` utiliza a biblioteca `ta` para calcular médias móveis, RSI e volume médio, e aplica as regras da estratégia.
- O `binance_client.py` faz a conexão segura com a API da Binance Testnet.
- O `config.py` centraliza todas as configurações sensíveis e parâmetros do robô.

## Segurança
- O bot opera apenas na Testnet da Binance por padrão, evitando riscos financeiros reais.
- As credenciais ficam no arquivo `config.py` (NUNCA compartilhe este arquivo publicamente).

## Próximos passos sugeridos
- Adicionar controle de posição (não abrir 2 compras seguidas)
- Implementar stop loss e take profit automáticos
- Criar dashboards e relatórios
- Fazer backtests com dados históricos
- Subir para um VPS para rodar 24/7

## Observações
- Este projeto está em desenvolvimento inicial.
- Sinta-se à vontade para sugerir melhorias ou abrir issues.
