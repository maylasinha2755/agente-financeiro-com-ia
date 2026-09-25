# Código da Aplicação — OrganizaFin

Esta pasta contém o código-fonte do **OrganizaFin**, um assistente virtual de organização financeira pessoal desenvolvido com Python, Streamlit e a API do Gemini.

O agente utiliza os dados disponíveis na base de conhecimento do projeto para ajudar o usuário a compreender suas receitas, despesas, categorias de gastos, metas de economia e limites de orçamento.

---

## Estrutura

```text
src/
├── app.py              # Interface do chatbot desenvolvida com Streamlit
├── agente.py           # Lógica do agente e integração com o Gemini
├── config.py           # Carregamento das configurações e da chave da API
└── requirements.txt    # Dependências necessárias para executar o projeto
```

### Arquivos

- **app.py:** responsável pela interface do OrganizaFin utilizando Streamlit. Recebe as perguntas do usuário, exibe as respostas e mantém o histórico da conversa durante a sessão.

- **agente.py:** contém a lógica principal do agente, o System Prompt, o carregamento da base de conhecimento e a integração com o modelo Gemini.

- **config.py:** carrega as variáveis de ambiente utilizadas pela aplicação, incluindo a chave da API do Gemini.

- **requirements.txt:** contém as bibliotecas necessárias para executar o projeto.

---

## Dependências

As dependências utilizadas pela aplicação estão definidas no arquivo `requirements.txt`:

```text
streamlit
google-genai
python-dotenv
```

Para instalar as dependências, execute o comando abaixo na raiz do projeto:

```bash
python -m pip install -r src/requirements.txt
```

---

## Configuração da API

O OrganizaFin utiliza a API do Gemini para gerar as respostas do agente.

Para executar o projeto localmente, crie um arquivo `.env` na raiz do projeto e adicione sua chave da API:

```env
GEMINI_API_KEY=sua_chave_aqui
```

> **Importante:** nunca publique sua chave da API no GitHub. O arquivo `.env` está incluído no `.gitignore` do projeto para impedir que essas informações sejam enviadas ao repositório.

---

## Como Rodar

Com as dependências instaladas e a variável `GEMINI_API_KEY` configurada no arquivo `.env`, execute o seguinte comando na raiz do projeto:

```bash
python -m streamlit run src/app.py
```

Após iniciar a aplicação, o Streamlit disponibilizará um endereço local para acessar o OrganizaFin pelo navegador.

Normalmente, a aplicação poderá ser acessada em:

```text
http://localhost:8501
```

---

## Funcionamento

O fluxo principal da aplicação ocorre da seguinte forma:

1. O OrganizaFin carrega os arquivos da base de conhecimento disponíveis na pasta `data`;
2. Os dados de perfil financeiro, categorias de gastos, transações e histórico de atendimento são organizados em um contexto;
3. O usuário envia uma pergunta por meio da interface desenvolvida em Streamlit;
4. A pergunta é enviada juntamente com o contexto e as instruções definidas no System Prompt;
5. O modelo Gemini analisa as informações disponíveis;
6. A resposta é apresentada ao usuário no chatbot;
7. O histórico da conversa é mantido durante a sessão.

---

## Base de Conhecimento Utilizada

A aplicação utiliza os seguintes arquivos disponíveis na pasta `data`:

```text
data/
├── categorias_gastos.json
├── historico_atendimento.csv
├── perfil_financeiro.json
└── transacoes.csv
```

Esses arquivos fornecem as informações utilizadas pelo agente para realizar suas análises financeiras.

---

## Modelo de IA

O OrganizaFin utiliza o modelo:

```text
gemini-3.5-flash-lite
```

A integração com o Gemini é realizada por meio da biblioteca:

```text
google-genai
```

O modelo recebe o contexto da base de conhecimento, as instruções de comportamento do OrganizaFin e a pergunta realizada pelo usuário.

---

## Segurança e Limitações

O OrganizaFin foi configurado para:

- Utilizar as informações disponíveis na base de conhecimento;
- Não inventar receitas, despesas, transações ou outros dados financeiros;
- Informar quando não existem dados suficientes para responder a uma pergunta;
- Não solicitar senhas ou dados bancários confidenciais;
- Não realizar transações ou movimentações bancárias;
- Não recomendar investimentos ou produtos financeiros específicos;
- Informar quando uma pergunta está fora do escopo de organização financeira pessoal.

O objetivo do OrganizaFin é auxiliar na **compreensão e organização das finanças pessoais**, sem substituir, quando necessário, a orientação de um profissional financeiro.
