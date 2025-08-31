import streamlit as st

st.set_page_config(layout="centered")

dias = [
    "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira",
    "Sexta-feira", "Sábado", "Domingo"
]

cardapio = {
    "Segunda-feira": [
        ("Jejum", "Dia de jejum com até 500 calorias"),
        ("Almoço", "150g filé de frango grelhado ou carne magra, 80g arroz integral, mix de folhas, legumes cozidos, 1 col chá azeite"),
        ("Lanche", "Whey protein com água ou iogurte desnatado + 7 morangos"),
        ("Jantar", "Opções:
1. Omelete com 4 ovos, tomate, salada
2. 150g frango ou carne, folhas + azeite
3. Wrap de Rap10 com frango + creme ricota + tomate")
    ],
    "Terça-feira": [
        ("Café da manhã", "2 ovos grandes, pão integral, queijo branco ou shake"),
        ("Almoço", "Frango grelhado, arroz integral, feijão, legumes, azeite, salada"),
        ("Lanche", "Whey com água ou iogurte + morangos"),
        ("Jantar", "Omelete ou wrap integral com carne moída, vegetais")
    ],
    "Quarta-feira": [
        ("Jejum", "Dia de jejum com até 500 calorias"),
        ("Almoço", "150g filé de frango ou carne, 80g arroz integral, folhas, legumes, azeite"),
        ("Lanche", "Whey com água ou iogurte + morangos"),
        ("Jantar", "1. Omelete com 4 ovos + salada
2. Frango + arroz + legumes
3. Wrap com frango + creme ricota")
    ],
    "Quinta-feira": [
        ("Café da manhã", "Shake: whey + frutas vermelhas + linhaça + água"),
        ("Almoço", "Peixe ou carne, arroz integral, legumes e salada"),
        ("Lanche", "Whey ou pão integral com frango"),
        ("Jantar", "Omelete ou prato leve com salada")
    ],
    "Sexta-feira": [
        ("Jejum", "Dia de jejum com até 500 calorias"),
        ("Almoço", "Frango grelhado, arroz integral, legumes, salada"),
        ("Lanche", "Whey com morangos ou iogurte + whey"),
        ("Jantar", "Wrap ou omelete com folhas verdes e azeite")
    ],
    "Sábado": [
        ("Café da manhã", "2 ovos, pão integral, queijo branco ou shake"),
        ("Almoço", "Frango, arroz integral, legumes, salada"),
        ("Lanche", "Mix de nozes ou whey"),
        ("Jantar", "Frango ao forno, sopa ou prato leve com vegetais")
    ],
    "Domingo": [
        ("Café da manhã", "Crepioca com queijo cottage + café"),
        ("Almoço", "Peixe grelhado, batata-doce, legumes"),
        ("Lanche", "Shake de proteína + pão integral"),
        ("Jantar", "Sopa de legumes com frango desfiado")
    ]
}

treinos = {
    "Segunda-feira": ["🏋️‍♀️ Musculação (Peito e Tríceps)", "🏃 Corrida"],
    "Terça-feira": ["🏋️‍♀️ Musculação (Costas e Bíceps)", "🏊 Natação"],
    "Quarta-feira": ["🏋️‍♀️ Musculação (Pernas)", "🏊 Natação"],
    "Quinta-feira": ["🏋️‍♀️ Musculação (Ombro e Abdômen)", "🏊 Natação"],
    "Sexta-feira": ["🏋️‍♀️ Musculação (Full Body)", "🏊 Natação"],
    "Sábado": ["🏃 Corrida"],
    "Domingo": []
}

st.title("📒 Guia Diário de Treino e Cardápio")

dia_escolhido = st.selectbox("Escolha o dia da semana:", dias)
st.header(f"🍽️ Cardápio do Dia - {dia_escolhido}")

for refeicao, texto in cardapio[dia_escolhido]:
    st.checkbox(f"{refeicao}: {texto}")

if treinos[dia_escolhido]:
    st.header("🏋️‍♂️ Treino do Dia")
    for t in treinos[dia_escolhido]:
        st.checkbox(t)

st.markdown("✅ Marque as opções conforme completar sua rotina.")

