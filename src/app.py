import streamlit as st

from agente import responder


# Configuração da página
st.set_page_config(
    page_title="OrganizaFin",
    page_icon="💰",
    layout="centered"
)


# Título da aplicação
st.title("💰 OrganizaFin")

st.write(
    "Seu assistente inteligente para organização financeira pessoal."
)

# Inicializa o histórico da conversa
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []


# Exibe as mensagens anteriores
for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])


# Campo para o usuário digitar uma pergunta
pergunta = st.chat_input("Digite sua pergunta sobre suas finanças...")


# Processa a pergunta do usuário
if pergunta:
    # Exibe a mensagem do usuário
    with st.chat_message("user"):
        st.markdown(pergunta)

    try:
        # Gera a resposta do OrganizaFin
        with st.chat_message("assistant"):
            with st.spinner("Analisando suas informações..."):
                resposta = responder(pergunta)

            st.markdown(resposta)

        # Salva a conversa somente após a resposta ser gerada com sucesso
        st.session_state.mensagens.append(
            {"role": "user", "content": pergunta}
        )

        st.session_state.mensagens.append(
            {"role": "assistant", "content": resposta}
        )

    except Exception as erro:
        st.error(
            "Não foi possível gerar a resposta no momento. "
            "Tente novamente em alguns instantes."
        )

        print(f"Erro ao gerar resposta: {erro}")