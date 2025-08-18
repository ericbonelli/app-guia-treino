import streamlit as st
import datetime

# -------------------------
# Dados simulados do plano
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

cardapio = {
    "Segunda-feira": [
        ("Café da manhã", "Omelete com 3 ovos + pão integral + café"),
        ("Almoço", "Frango grelhado + arroz integral + salada verde"),
        ("Lanche", "Shake de whey + banana"),
        ("Jantar", "Tilápia grelhada + purê de batata-doce + legumes")
    ],
    "Terça-feira": [
        ("Café da manhã", "Tapioca com queijo branco + café preto"),
        ("Almoço", "Carne vermelha magra + quinoa + brócolis"),
        ("Lanche", "Iogurte grego + aveia + mel"),
        ("Jantar", "Omelete de atum + arroz integral + rúcula")
    ]
}

# ------------------
# Interface principal
# ------------------
st.title("📘 Guia de Treino + Alimentação")
st.markdown("Selecione o **dia da semana** para ver seu treino e cardápio personalizado.")

dia = st.selectbox("Dia da semana", list(cardapio.keys()))
tipo_treino = st.selectbox("Tipo de Treino", list(treinos.keys()))

st.subheader("🍽️ Cardápio do Dia")
for refeicao, item in cardapio[dia]:
    st.markdown(f"**{refeicao}:** {item}")

st.subheader("🏋️ Treino do Dia")
for exercicio, link in treinos[tipo_treino]:
    st.markdown(f"- [{exercicio}]({link})")

# Marcação de shake com creatina
st.subheader("🥤 Shake com Creatina")
whey = st.checkbox("Whey com Banana")
creatina = st.checkbox("Whey com Abacate")
if whey or creatina:
    st.success("Suplemento marcado para hoje! 🥤")

# Progresso de peso
st.subheader("⚖️ Acompanhamento de Progresso")
peso = st.number_input("Peso atual (kg)", 0.0, 200.0, 75.0)
sono = st.slider("Horas de sono", 0, 12, 7)
st.write(f"Hoje você registrou {peso} kg e {sono}h de sono.")

# Final
st.markdown("---")
st.caption("Desenvolvido com ❤️ no Streamlit")
