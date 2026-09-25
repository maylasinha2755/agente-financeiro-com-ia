import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

# Chave da API do Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
