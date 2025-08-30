import streamlit as st
from datetime import date

# -------------------------
# Configuração inicial
# -------------------------
st.set_page_config(page_title="Guia de Treino e Alimentação", layout="centered")

# -------------------------
# Dados dos Treinos
# -------------------------
treinos = {
    "A - Pernas e Core": [
        ("Agachamento Livre", "https://www.youtube.com/watch?v=1oed-UmAxFs"),
        ("Leg Press 45°", "https://www.youtube.com/watch?v=IZxyjW7MPJQ"),
        ("Stiff com Halteres", "https://www.youtube.com/watch?v=6P2QcD3jN8w"),
        ("Afundo com Passada", "https://www.youtube.com/watch?v=QF0BQS2W80k"),
        ("Elevação de Panturrilha", "https://www.youtube.com/watch?v=-M4-G8p8fmc"),
        ("Prancha Abdominal", "https://www.youtube.com/watch?v=ASdvN_XEl_c")
    ],
    "B - Peito, Tríceps e Ombros": [
        ("Supino Reto com Barra", "https://www.youtube.com/watch?v=rT7DgCr-3pg"),
        ("Supino Inclinado com Halteres", "https://www.youtube.com/watch?v=8iPEnn-ltC8"),
        ("Desenvolvimento Militar", "https://www.youtube.com/watch?v=B-aVuyhvLHU"),
        ("Tríceps Testa", "https://www.youtube.com/watch?v=6SS6K3lAwZ8"),
        ("Tríceps Corda no Cross", "https://www.youtube.com/watch?v=vB5OHsJ3EME"),
        ("Abdominal Oblíquo", "https://www.youtube.com/watch?v=E4h40NOUOHM")
    ],
    "C - Costas e Bíceps": [
        ("Barra Fixa", "https://www.youtube.com/watch?v=HRVvH5u6SGc"),
        ("Remada Curvada com Barra", "https://www.youtube.com/watch?v=vT2GjY_Umpw"),
        ("Pulldown na Polia", "https://www.youtube.com/watch?v=CAwf7n6Luuc"),
        ("Rosca Direta com Barra EZ", "https://www.youtube.com/watch?v=kwG2ipFRgfo"),
        ("Rosca Martelo com Halteres", "https://www.youtube.com/watch?v=zC3nLlEvin4"),
        ("Hiperextensão Lombar", "https://www.youtube.com/watch?v=ph3pddpKzzw")
    ]
}

# -------------------------
# Dados do Cardápio
# -------------------------
dias_jejum = ["Segunda-feira", "Terça-feira", "Sexta-feira"]
cardapio = {}

for dia in ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]:
    if dia in dias_jejum:
        cardapio[dia] = [
            ("Almoço", "150g frango ou carne magra + 80g arroz integral (ou tubérculos) + legumes + 1 cchá azeite"),
            ("Lanche", "1 scoop whey com água ou 100g iogurte c/ 10g whey e 7 morangos"),
            ("Jantar", "Opção 1: Igual ao almoço / Opção 2: Omelete 4 ovos / Opção 3: Rap10 com frango e creme ricota")
        ]
    else:
        cardapio[dia] = [
            ("Café da manhã", "2 ovos + pão integral + queijo branco ou Shake com frutas vermelhas"),
            ("Almoço", "150g frango/carne + 80g arroz integral + 80g feijão + legumes + 1 cchá azeite"),
            ("Lanche", "Shake ou pão integral c/ frango e creme ricota"),
            ("Pré-treino", "Barrinha de proteína"),
            ("Jantar", "Opção 1: Omelete 4 ovos / Opção 2: Rap10 com carne moída e salada")
        ]

# -------------------------
# Interface
# -------------------------
st.title("📘 Guia de Treino e Alimentação")
st.markdown("Selecione o dia da semana para visualizar o treino, o cardápio e marcar o que foi realizado.")

dia = st.selectbox("📅 Dia da semana", list(cardapio.keys()))
treino_do_dia = st.selectbox("🏋️ Tipo de Treino", list(treinos.keys()))

st.subheader("🍽️ Cardápio do Dia")
for refeicao, descricao in cardapio[dia]:
    st.checkbox(f"{refeicao}: {descricao}", key=f"{dia}_{refeicao}")

st.subheader("🏋️ Exercícios do Treino")
for exercicio, link in treinos[treino_do_dia]:
    st.checkbox(f"[{exercicio}]({link})", key=f"{dia}_{exercicio}")

st.markdown("---")
st.caption("Desenvolvido com ❤️ por Eric | Pronto para integração com n8n e Google Sheets")


