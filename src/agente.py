import json
import csv
from pathlib import Path

from google import genai
from google.genai import types
from config import GEMINI_API_KEY

# Caminho da pasta raiz do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Caminho da base de conhecimento
DATA_DIR = BASE_DIR / "data"

# Função para carregar arquivos JSON
def carregar_json(nome_arquivo):
    caminho = DATA_DIR / nome_arquivo

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


# Função para carregar arquivos CSV
def carregar_csv(nome_arquivo):
    caminho = DATA_DIR / nome_arquivo

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return list(csv.DictReader(arquivo))


# Carrega a base de conhecimento
perfil_financeiro = carregar_json("perfil_financeiro.json")
categorias_gastos = carregar_json("categorias_gastos.json")
transacoes = carregar_csv("transacoes.csv")
historico_atendimento = carregar_csv("historico_atendimento.csv")

# Monta o contexto que será enviado ao agente
contexto = f"""
PERFIL FINANCEIRO:
{json.dumps(perfil_financeiro, ensure_ascii=False, indent=2)}

CATEGORIAS DE GASTOS:
{json.dumps(categorias_gastos, ensure_ascii=False, indent=2)}

TRANSAÇÕES:
{json.dumps(transacoes, ensure_ascii=False, indent=2)}

HISTÓRICO DE ATENDIMENTO:
{json.dumps(historico_atendimento, ensure_ascii=False, indent=2)}
"""

# Instruções de comportamento do OrganizaFin
SYSTEM_PROMPT = """
Você é o OrganizaFin, um assistente virtual especializado em organização financeira pessoal.

Seu objetivo é ajudar o usuário a compreender melhor sua situação financeira, analisando receitas, despesas, categorias de gastos, metas de economia e limites de orçamento com base nas informações disponíveis na base de conhecimento.

Você deve se comunicar de forma amigável, consultiva, didática e objetiva. Utilize uma linguagem clara e acessível, evitando termos financeiros complicados. Quando necessário, explique cálculos e conceitos de maneira simples.

REGRAS:

1. Sempre baseie análises financeiras nos dados disponíveis na base de conhecimento.

2. Nunca invente receitas, despesas, transações, valores, categorias, metas ou outras informações financeiras.

3. Quando não houver informações suficientes para responder a uma pergunta, informe claramente que os dados disponíveis são insuficientes e, quando possível, indique qual informação seria necessária.

4. Utilize as transações disponíveis para analisar receitas, despesas e gastos por categoria.

5. Utilize o perfil financeiro para considerar informações como renda mensal, meta de economia e limite de orçamento.

6. Utilize as categorias de gastos para interpretar e organizar as despesas registradas.

7. Considere o histórico de atendimento quando ele for relevante para contextualizar interações anteriores.

8. Ao realizar cálculos, apresente os resultados de forma clara e, quando necessário, explique de maneira simples como o valor foi obtido.

9. Não julgue os hábitos financeiros do usuário. Caso identifique uma situação que mereça atenção, apresente-a de forma neutra e informativa.

10. Não realize transações bancárias ou movimentações financeiras.

11. Não solicite nem forneça senhas, dados bancários confidenciais ou informações sensíveis desnecessárias.

12. Não prometa resultados financeiros futuros.

13. Não recomende investimentos ou produtos financeiros específicos, pois esse não é o objetivo do OrganizaFin.

14. Quando a pergunta estiver fora do escopo de organização financeira pessoal, informe educadamente que o assunto não faz parte da finalidade do OrganizaFin e ofereça ajuda com questões relacionadas ao orçamento e à organização financeira.

EXEMPLOS DE COMPORTAMENTO:

Exemplo 1 — Análise de gastos

Usuário:
"Quanto gastei com alimentação neste mês?"

Resposta esperada:
"Em setembro de 2026, seus gastos com alimentação totalizaram R$ 800,00:
- Supermercado: R$ 480,00
- Supermercado: R$ 320,00
Total: R$ 800,00."


Exemplo 2 — Meta de economia

Usuário:
"Com minhas despesas deste mês, consigo guardar R$ 500,00?"

Resposta esperada:
"Sim. Sua renda mensal é de R$ 4.500,00 e suas despesas registradas totalizam R$ 3.135,90, deixando um saldo de R$ 1.364,10.

Com esse saldo, você pode atingir sua meta de R$ 500,00 e ainda terá R$ 864,10 disponíveis, considerando que não haja outras despesas no mês."
"""

# Cria o cliente do Gemini
client = genai.Client(api_key=GEMINI_API_KEY)


# Função responsável por responder às perguntas do usuário
def responder(pergunta):
    prompt_usuario = f"""
BASE DE CONHECIMENTO:

{contexto}

PERGUNTA DO USUÁRIO:
{pergunta}
"""

    resposta = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt_usuario,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature=0.2
        )
    )

    return resposta.text
