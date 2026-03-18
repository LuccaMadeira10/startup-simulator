# MVP Plan

## Decisoes ja definidas

- A simulacao avanca em rodadas mensais.
- Cada rodada representa exatamente 1 mes.
- O projeto continua com foco de aprendizado e deve crescer em etapas pequenas.

## Recorte do primeiro MVP

O primeiro MVP nao precisa modelar tudo que esta no README.
Ele precisa provar o loop principal da simulacao:

1. Criar uma startup.
2. Registrar o estado inicial da empresa.
3. Receber as decisoes de uma rodada mensal.
4. Calcular o resultado do mes.
5. Salvar o historico da rodada.
6. Mostrar a evolucao da startup ao longo dos meses.

## Entidades recomendadas

### Startup

Representa o cadastro base da empresa.

Campos iniciais sugeridos:

- id
- name
- industry
- initial_capital
- created_at

### SimulationState

Representa o estado atual da startup no mes corrente.

Campos iniciais sugeridos:

- startup_id
- current_month
- cash
- users
- mrr
- team_size

### RoundDecision

Representa o que o usuario escolheu naquele mes.

Campos iniciais sugeridos:

- startup_id
- month
- marketing_budget
- product_investment
- hiring_count

### RoundResult

Representa o que o sistema calculou para aquele mes.

Campos iniciais sugeridos:

- startup_id
- month
- new_users
- revenue
- costs
- net_result
- cash_end

## Regras de modelagem para manter desde ja

- Separar cadastro da startup do estado da simulacao.
- Separar decisao do usuario do resultado calculado.
- Usar mes como unidade padrao para custos, receita e crescimento.
- Guardar historico por rodada em vez de sobrescrever tudo.
- Evitar dinheiro com float quando a simulacao ficar mais seria.

## Ordem ideal de implementacao

1. Consolidar dependencias e estrutura basica do projeto.
2. Criar o motor de simulacao em Python puro, sem depender da API.
3. Escrever testes para o motor da simulacao.
4. Implementar persistencia com banco de dados.
5. Adaptar a API para trabalhar com o motor e com o banco.
6. Construir o frontend consumindo endpoints ja estaveis.

## Por agora

O melhor proximo passo e implementar o motor da simulacao em pequena escala.
Antes disso, vale fechar as regras do primeiro mes com poucas variaveis.

Sugestao de escopo inicial:

- marketing influencia novos usuarios
- equipe influencia custo mensal
- usuarios geram receita mensal
- caixa final decide se a startup continua viva

## deixar para depois

- captacao de investimento
- concorrencia
- eventos aleatorios
- multiplos produtos
- dashboards mais completos no frontend
