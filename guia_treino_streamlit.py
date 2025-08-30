import streamlit as st
from datetime import datetime

st.set_page_config(layout="centered")
st.title("📘 Guia Diário de Treino e Cardápio")

dias_semana = [
    "Segunda-feira", "Terça-feira", "Quarta-feira",
    "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"
]

cardapio = {
    "Segunda-feira": [
        ("Café da manhã", "Dia de jejum até 12h ou 18h — jejum intermitente 4x3."),
        ("Almoço", "150g frango grelhado ou carne magra + 80g arroz integral ou raízes + salada e azeite"),
        ("Lanche", "Whey com água gelada ou iogurte + whey + 7 morangos"),
        ("Jantar", "Opções: 1) Frango + arroz + salada; 2) Omelete 4 ovos + folhas verdes; 3) Rap10 com frango, creme de ricota e tomate")
    ],
    "Terça-feira": [
        ("Café da manhã", "2 ovos grandes + pão integral + queijo branco ou shake de whey"),
        ("Almoço", "Filé de frango + arroz + feijão + legumes + salada com azeite"),
        ("Lanche", "Whey ou wrap com frango + pão integral"),
        ("Jantar", "Omelete ou wrap integral com carne moída e vegetais")
    ],
    "Quarta-feira": [
        ("Café da manhã", "Dia de jejum até 12h ou 18h — jejum intermitente 4x3."),
        ("Almoço", "150g frango grelhado ou carne magra + 80g arroz integral ou raízes + salada e azeite"),
        ("Lanche", "Whey com água gelada ou iogurte + whey + 7 morangos"),
        ("Jantar", "Opções: 1) Frango + arroz + salada; 2) Omelete 4 ovos + folhas verdes; 3) Rap10 com frango, creme de ricota e tomate")
    ],
    "Quinta-feira": [
        ("Café da manhã", "Shake de whey + frutas vermelhas + linhaça"),
        ("Almoço", "Peixe ou carne + arroz integral + legumes + salada com azeite"),
        ("Lanche", "Whey ou pão com frango e ricota"),
        ("Jantar", "Omelete ou prato leve com proteína + salada")
    ],
    "Sexta-feira": [
        ("Café da manhã", "Dia de jejum até 12h ou 18h — jejum intermitente 4x3."),
        ("Almoço", "150g frango grelhado ou carne magra + 80g arroz integral ou raízes + salada e azeite"),
        ("Lanche", "Whey com água gelada ou iogurte + whey + 7 morangos"),
        ("Jantar", "Opções: 1) Frango + arroz + salada; 2) Omelete 4 ovos + folhas verdes; 3) Rap10 com frango, creme de ricota e tomate")
    ],
    "Sábado": [
        ("Café da manhã", "2 ovos, pão integral, queijo branco ou shake"),
        ("Almoço", "Frango, arroz integral, legumes, salada"),
        ("Lanche", "Mix de nozes ou whey"),
        ("Jantar", "Frango ao forno, sopa ou prato leve com vegetais")
    ],
    "Domingo": [
        ("Café da manhã", "Crepioca com queijo cottage ou ovos + shake"),
        ("Almoço", "Peixe grelhado, arroz ou batata, legumes e salada"),
        ("Lanche", "Shake de proteína ou pão integral com frango"),
        ("Jantar", "Omelete ou sopa de legumes com proteína")
    ]
}

treino = {
    "Segunda-feira": ["🏃 Corrida"],
    "Terça-feira": ["🏋️‍♀️ Musculação - Peito e Tríceps", "🏊‍♂️ Natação"],
    "Quarta-feira": ["🏃 Corrida"],
    "Quinta-feira": ["🏋️‍♂️ Musculação - Costas e Bíceps", "🏊‍♂️ Natação"],
    "Sexta-feira": ["🏃 Corrida"],
    "Sábado": ["🏃 Corrida"],
    "Domingo": ["🧘 Livre ou descanso ativo"]
}

hoje = datetime.today().weekday()
dia_atual = dias_semana[hoje]

st.header(f"📅 {dia_atual}")

st.subheader("🍽️ Cardápio do Dia")
for refeicao, descricao in cardapio[dia_atual]:
    st.checkbox(f"{refeicao}: {descricao}", key=f"{refeicao}_{dia_atual}")

st.subheader("🏋️ Treino do Dia")
for atividade in treino[dia_atual]:
    st.checkbox(f"{atividade}", key=f"{atividade}_{dia_atual}")

st.markdown("✅ Marque as opções conforme completar sua rotina.")
