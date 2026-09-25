# Base de Conhecimento

## Dados Utilizados

A base de conhecimento do OrganizaFin utiliza dados financeiros simulados, organizados em arquivos CSV e JSON. Os dados são utilizados para permitir que o agente analise receitas, despesas, categorias de gastos e metas financeiras do usuário.

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Fornecer contexto sobre interações e análises financeiras anteriores |
| `perfil_financeiro.json` | JSON | Armazenar informações sobre renda, meta de economia e limite de orçamento do usuário |
| `categorias_gastos.json` | JSON | Organizar e auxiliar na classificação das despesas por categoria |
| `transacoes.csv` | CSV | Registrar e analisar receitas e despesas do usuário |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

O arquivo `transacoes.csv` original foi mantido como base, preservando sua estrutura de data, descrição, categoria, valor e tipo. Os dados simulados foram adaptados e expandidos para representar diferentes despesas de um orçamento pessoal, incluindo novas transações e categorias. Também foram adicionadas transações repetidas em algumas categorias para permitir análises de gastos acumulados pelo agente.

O arquivo `perfil_investidor.json` foi renomeado para `perfil_financeiro.json` e adaptado à proposta do OrganizaFin. Foram removidas informações relacionadas ao perfil de investidor, patrimônio e tolerância a risco, e adicionados campos voltados à organização do orçamento, como meta de economia mensal e limite de orçamento mensal.

O arquivo `produtos_financeiros.json` foi substituído por `categorias_gastos.json`, removendo informações relacionadas a investimentos e incluindo categorias utilizadas para organizar e interpretar as despesas pessoais registradas nas transações.

O arquivo `historico_atendimento.csv` teve sua estrutura original preservada, mantendo os campos de data, canal, tema, resumo e status de resolução. Os registros foram adaptados para representar interações relacionadas à organização financeira pessoal, como análise do orçamento, gastos por categoria, metas de economia e acompanhamento do limite mensal.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos CSV e JSON são carregados no início da execução da aplicação. 
Os dados do `perfil_financeiro.json`, `categorias_gastos.json`, `transacoes.csv` e `historico_atendimento.csv` são lidos e organizados para compor o contexto utilizado pelo OrganizaFin durante a conversa.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados carregados são incluídos no contexto enviado ao modelo junto com as instruções do agente. A cada pergunta, o OrganizaFin utiliza as informações disponíveis na base de conhecimento para identificar os dados relevantes e elaborar a resposta.

As transações são utilizadas para análises de receitas, despesas e categorias de gastos; o perfil financeiro fornece informações sobre renda, meta de economia e limite de orçamento; as categorias auxiliam na classificação das despesas; e o histórico de atendimento fornece contexto sobre interações anteriores.

Quando uma informação necessária não estiver disponível na base de conhecimento, o agente deve informar essa limitação em vez de criar ou estimar dados.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```text
Perfil Financeiro:
- Nome: Mariana Souza
- Idade: 29 anos
- Profissão: Assistente Administrativa
- Renda mensal: R$ 4.500,00
- Meta de economia mensal: R$ 500,00
- Limite de orçamento mensal: R$ 4.000,00

Transações:
- 01/09: Salário - Receita - R$ 4.500,00
- 02/09: Aluguel - Moradia - R$ 1.300,00
- 03/09: Supermercado - Alimentação - R$ 480,00
- 05/09: Internet - Contas - R$ 120,00
- 08/09: Restaurante - Lazer - R$ 150,00

Categorias de Gastos:
- Moradia: aluguel, condomínio, energia e água
- Alimentação: supermercado, restaurante e padaria
- Transporte: combustível, Uber e ônibus
- Saúde: farmácia, consulta médica e academia
- Lazer: streaming, cinema e restaurante
- Contas: internet, telefone e energia

Histórico de Atendimento:
- Orçamento mensal: análise da distribuição das despesas
- Alimentação: consulta do total de gastos com alimentação
- Meta de economia: acompanhamento da meta mensal de R$ 500,00

```
