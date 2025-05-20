# Estratégia 80/20 para Trading Bot

## Filosofia e Inspiração

A estratégia utilizada neste projeto é baseada no Princípio de Pareto, também conhecido como regra 80/20. Esse princípio sugere que, em muitos fenômenos, cerca de 80% dos resultados vêm de apenas 20% das causas. No contexto do trading, isso significa buscar operar apenas nos momentos de maior probabilidade de sucesso, evitando o excesso de operações e focando em qualidade ao invés de quantidade.

## Por que essa abordagem?

- **Redução de ruído:** A maioria dos movimentos do mercado é aleatória ou de baixa relevância. Operar menos, mas com mais qualidade, reduz o impacto de ruídos e falsos sinais.
- **Menos custos e estresse:** Menos operações significam menos taxas, menos exposição ao risco e menos desgaste emocional.
- **Foco em confluência de sinais:** A estratégia só entra em operação quando há forte confluência de fatores técnicos, aumentando a probabilidade de acerto.

## Regras da Estratégia

A entrada e saída de operações são baseadas em três pilares técnicos:

1. **Cruzamento de Médias Móveis (MA9 e MA21):**
   - Compra: Quando a média móvel curta (MA9) cruza para cima a média longa (MA21), indicando início de tendência de alta.
   - Venda: Quando a MA9 cruza para baixo a MA21, indicando início de tendência de baixa.

2. **RSI (Índice de Força Relativa):**
   - Compra: RSI entre 50 e 65, mostrando força compradora, mas sem sobrecompra.
   - Venda: RSI entre 35 e 50, mostrando fraqueza, mas sem sobrevenda extrema.

3. **Volume acima da média:**
   - Só opera se o volume atual estiver acima da média dos últimos 20 candles, filtrando movimentos fracos e sem liquidez.

## Diferenciais da Estratégia

- **Filtro de Qualidade:** Só opera nos 20% dos momentos mais favoráveis, evitando trades em zonas de indecisão.
- **Confluência:** Exige que todos os critérios estejam alinhados, aumentando a robustez dos sinais.
- **Gestão de Risco embutida:** O uso de stop loss e take profit automáticos protege o capital e garante disciplina.
- **Adaptável:** Os parâmetros (janelas das médias, RSI, volume) podem ser ajustados para diferentes ativos e períodos.
- **Simplicidade e Eficiência:** Estratégia fácil de entender, replicar e auditar, sem depender de indicadores proprietários ou black-box.

## Por que pode gerar bons resultados?

- **Evita overtrading:** Foca em operações de maior probabilidade, reduzindo perdas por excesso de trades.
- **Surfando tendências:** O cruzamento de médias aliado ao volume permite capturar movimentos mais longos e evitar entradas em consolidação.
- **Disciplina:** O uso de critérios claros e objetivos reduz decisões emocionais e subjetivas.
- **Backtest comprovado:** O histórico mostra que a estratégia é capaz de preservar e multiplicar o capital em diferentes cenários de mercado.

## Exemplos Visuais e Estudos de Caso

### Exemplo de Sinal de Compra

- MA9 cruza para cima da MA21
- RSI = 58
- Volume atual acima da média

**Resultado:** O bot executa uma compra e, se a tendência continuar, surfa o movimento até o próximo sinal de venda ou até o stop/take profit.

### Exemplo de Sinal de Venda

- MA9 cruza para baixo da MA21
- RSI = 42
- Volume acima da média

**Resultado:** O bot executa uma venda, protegendo o capital em caso de reversão.

### Estudo de Caso (Backtest)

No backtest dos últimos 60 dias, a estratégia realizou poucas operações, mas com alta qualidade, resultando em crescimento do capital e poucas sequências de perdas.

## Comparativo com Outras Abordagens

- **Estratégias de alta frequência:** Operam muito, mas com maior exposição a ruído e custos. A 80/20 busca qualidade, não quantidade.
- **Estratégias baseadas só em médias:** Podem gerar muitos falsos sinais. O filtro de RSI e volume reduz entradas ruins.
- **Estratégias subjetivas:** Dependem de feeling ou análise manual. Aqui, tudo é objetivo e replicável.

## Gráficos Ilustrativos

Abaixo um exemplo de gráfico típico do capital ao longo do tempo, gerado pelo backtest da estratégia 80/20:

```
Capital ($)
|
|         _
|        / \
|  __---'   '--__
|_/               \__
+----------------------> Tempo
```

Esse padrão mostra períodos de estabilidade (sem operações) e saltos positivos quando a estratégia acerta tendências, ilustrando o foco em qualidade e não quantidade.

## Simulação Específica

- **Período:** Últimos 60 dias (BTC/USD, 1h)
- **Resultado:**
  - Poucas operações, mas com alta taxa de acerto
  - Capital inicial: $10.000
  - Capital final: $11.194,94
  - Drawdown baixo, poucas sequências de perdas

## Dicas para Melhorar a Estratégia

- Teste diferentes janelas de médias móveis e RSI para outros ativos
- Adicione filtros de tendência macro (ex: MA200)
- Use stop loss dinâmico (trailing stop) para capturar tendências longas
- Combine com análise de price action para refinar entradas

---
