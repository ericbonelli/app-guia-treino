import streamlit as st
from datetime import datetime

st.set_page_config(layout="centered")
st.title("📆 Guia Diário de Treino e Cardápio")

dias_semana = [
    "Segunda-feira", "Terça-feira", "Quarta-feira",
    "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"
]

treinos = {
    "Segunda-feira": ["🏋️ Musculação", "🏃 Corrida"],
    "Terça-feira": ["🏋️ Musculação", "🏊 Natação"],
    "Quarta-feira": ["🏋️ Musculação", "🏊 Natação"],
    "Quinta-feira": ["🏋️ Musculação", "🏊 Natação"],
    "Sexta-feira": ["🏋️ Musculação", "🏃 Corrida"],
    "Sábado": ["🏃 Corrida"],
    "Domingo": ["🏃 Corrida"]
}

cardapio = {
    "Segunda-feira": [
        ("Jejum", "Dia de jejum com até 500 calorias"),
        ("Almoço", "150g filé frango/carne + arroz integral + legumes + salada + azeite"),
        ("Lanche", "Whey com água ou iogurte + morangos"),
        ("Jantar", "Opções: Omelete 4 ovos, Wrap integral com frango, ou Frango + arroz + legumes")
    ],
    "Terça-feira": [
        ("Café da manhã", "2 ovos, pão integral, queijo branco ou shake"),
        ("Almoço", "Frango ou carne + arroz integral + feijão + legumes + azeite"),
        ("Lanche", "Whey com água ou wrap leve"),
        ("Jantar", "Wrap com carne moída ou omelete com folhas")
    ],
    "Quarta-feira": [
        ("Jejum", "Dia de jejum com até 500 calorias"),
        ("Almoço", "150g filé frango/carne + arroz integral + legumes + salada + azeite"),
        ("Lanche", "Whey com água ou iogurte + morangos"),
        ("Jantar", "Opções: Omelete 4 ovos, Wrap integral com frango, ou Frango + arroz + legumes")
    ],
    "Quinta-feira": [
        ("Café da manhã", "Shake de whey com frutas vermelhas + linhaça"),
        ("Almoço", "Peixe ou carne + arroz integral + legumes + azeite"),
        ("Lanche", "Whey ou pão com frango e ricota"),
        ("Jantar", "Omelete ou wrap integral com vegetais")
    ],
    "Sexta-feira": [
        ("Jejum", "Dia de jejum com até 500 calorias"),
        ("Almoço", "150g filé frango/carne + arroz integral + legumes + salada + azeite"),
        ("Lanche", "Whey com água ou iogurte + morangos"),
        ("Jantar", "Opções: Omelete 4 ovos, Wrap integral com frango, ou Frango + arroz + legumes")
    ],
    "Sábado": [
        ("Café da manhã", "2 ovos, pão integral, queijo branco ou shake"),
        ("Almoço", "Frango, arroz integral, legumes, salada"),
        ("Lanche", "Mix de nozes ou whey"),
        ("Jantar", "Frango ao forno, sopa ou prato leve com vegetais")
    ],
    "Domingo": [
        ("Café da manhã", "Crepioca de queijo cottage + café"),
        ("Almoço", "Peixe ou frango, arroz, legumes e salada"),
        ("Lanche", "Shake de proteína ou pão integral com frango"),
        ("Jantar", "Omelete ou sopa leve de legumes")
    ]
}

dia_hoje = datetime.now().strftime("%A")
mapa_dia = {
    "Monday": "Segunda-feira",
    "Tuesday": "Terça-feira",
    "Wednesday": "Quarta-feira",
    "Thursday": "Quinta-feira",
    "Friday": "Sexta-feira",
    "Saturday": "Sábado",
    "Sunday": "Domingo"
}
dia = mapa_dia.get(dia_hoje, "Segunda-feira")

st.header(f"📋 {dia}")

st.subheader("🍽️ Cardápio do Dia")
for refeicao, descricao in cardapio.get(dia, []):
    st.checkbox(f"{refeicao}: {descricao}", key=f"{dia}_{refeicao}")

st.subheader("🏋️ Treino do Dia")
for treino in treinos.get(dia, []):
    st.checkbox(treino, key=f"{dia}_{treino}")

st.markdown("---")
st.markdown("✅ Marque as opções conforme completar sua rotina.")
st.markdown("_Integração futura com painel histórico e analytics_ 📊")
