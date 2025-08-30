import streamlit as st
import datetime

st.set_page_config(page_title="Guia de Treino e Alimentação", layout="wide")

st.title("📘 Guia de Treino + Alimentação Diária")
st.markdown("Acompanhe sua rotina de treinos e alimentação. Marque os itens concluídos e salve seu progresso!")

# ------------------------------------------
# Dia da semana atual (padrão)
# ------------------------------------------
dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
hoje_pt = dias_semana[datetime.datetime.today().weekday()]
dia = st.selectbox("📅 Escolha o dia da semana", dias_semana, index=dias_semana.index(hoje_pt))

# -------------------------
# Cardápio atualizado com jejum (Seg, Qua, Sex)
# -------------------------
cardapio = {
    "Segunda-feira": [
        ("Jejum", "Dia de jejum com até 500 calorias"),
        ("Almoço", "150g frango grelhado + 80g arroz integral + salada com azeite"),
        ("Lanche", "Whey protein com água ou iogurte desnatado com morangos"),
        ("Jantar", "Omelete 4 ovos ou wrap integral com frango e ricota")
    ],
    "Terça-feira": [
        ("Café da manhã", "2 ovos + pão integral + queijo branco"),
        ("Almoço", "Filé de frango + arroz integral + feijão + legumes + salada"),
        ("Lanche", "Whey com água ou iogurte desnatado + morangos ou wrap"),
        ("Jantar", "Omelete ou wrap integral com carne moída e vegetais")
    ],
    "Quarta-feira": [
        ("Jejum", "Dia de jejum com até 500 calorias"),
        ("Almoço", "Frango grelhado + arroz + legumes + azeite"),
        ("Lanche", "Iogurte ou pão com frango e requeijão light"),
        ("Jantar", "Wrap de Rap10 com carne moída + alface + tomate")
    ],
    "Quinta-feira": [
        ("Café da manhã", "Shake de whey + frutas vermelhas + linhaça"),
        ("Almoço", "Peixe ou carne + arroz integral + legumes + salada"),
        ("Lanche", "Whey com morangos ou pão integral com proteína"),
        ("Jantar", "Omelete ou prato leve com proteína + salada")
    ],
    "Sexta-feira": [
        ("Jejum", "Dia de jejum com até 500 calorias"),
        ("Almoço", "Frango grelhado + arroz integral + legumes + salada"),
        ("Lanche", "Whey com morangos ou iogurte com whey"),
        ("Jantar", "Wrap ou omelete com folhas verdes e azeite")
    ],
    "Sábado": [
        ("Café da manhã", "Crepioca de queijo cottage + café"),
        ("Almoço", "Peito de frango ao forno + arroz integral + salada"),
        ("Lanche", "Mix de nozes + suco de laranja natural"),
        ("Jantar", "Tilápia assada + legumes + azeite")
    ],
    "Domingo": [
        ("Café da manhã", "Cuscuz com ovo mexido + café"),
        ("Almoço", "Peixe grelhado + batata-doce + salada"),
        ("Lanche", "Iogurte + frutas"),
        ("Jantar", "Sopa de legumes com frango desfiado")
    ]
}

# ------------------------------------------
# Treinos
# ------------------------------------------
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

# ----------------------------
# Checklists de alimentação
# ----------------------------
st.subheader("🍽️ Cardápio do Dia")
with st.form("form_cardapio"):
    for refeicao, descricao in cardapio[dia]:
        st.checkbox(f"{refeicao}: {descricao}", key=f"refeicao_{refeicao}_{dia}")
    st.form_submit_button("✅ Salvar refeições concluídas")

# ----------------------------
# Checklists de treino
# ----------------------------
st.subheader("🏋️ Exercícios de Musculação")
tipo_treino = st.selectbox("Escolha o tipo de treino", list(treinos.keys()))
with st.form("form_treino"):
    for exercicio, link in treinos[tipo_treino]:
        st.checkbox(f"[{exercicio}]({link})", key=f"ex_{exercicio}_{dia}")
    st.form_submit_button("✅ Salvar treino realizado")

# ----------------------------
# Cardio extra
# ----------------------------
st.subheader("🏃 Cardio")
if dia in ["Segunda-feira", "Sábado", "Domingo"]:
    st.checkbox("Corrida (30-40min)", key=f"corrida_{dia}")
if dia in ["Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"]:
    st.checkbox("Natação (45min)", key=f"natacao_{dia}")

st.markdown("---")
st.caption("🔁 Integração futura com painel histórico e analytics | Desenvolvido com ❤️ no Streamlit")
