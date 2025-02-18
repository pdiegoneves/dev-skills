import streamlit as st
from components.question import question
from components.chart import chart

st.set_page_config(
    layout="wide",
    page_icon="https://docs.streamlit.io/logo.svg",
    page_title="FAQ - Teste"
)


logo, titulo = st.columns([2, 10])
logo.image(r"https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png")
titulo.title("F.A.Q")

metricas = st.container()
metricas_col1, metricas_col2, metricas_col3 = st.columns([ 2, 2, 8 ])
with metricas:
    metricas_col1.metric("Visitantes", 135, border=True, delta="5")
    metricas_col2.button("Mostrar", on_click=chart)


st.divider()

question(
    question="O que é uma F.A.Q?",
    response='FAQ é a sigla para Frequently Asked Questions, que em português significa "Perguntas Frequentes". É uma página de um site que reúne as dúvidas mais frequentes dos clientes.')

question(
    question="O que é a linguegem Python?",
    response='Python é uma linguagem de programação de alto nível, orientada a objetos, e de uso geral. É muito utilizada no desenvolvimento web, ciência de dados, machine learning, e automação.'
    )


col1, col2, col3 = st.columns([ 6, 6, 12 ])

col1.header("coluna 1")
col1.text("Texto coluna 1")

col2.header("coluna 2")
col2.text("Texto coluna 2")

with col3:
    st.header("coluna 3")
    st.text("Texto coluna 3 - esse texto é mais longo e deve ocupar 50% da página")