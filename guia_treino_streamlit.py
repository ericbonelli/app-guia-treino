import streamlit as st
import datetime
import pandas as pd

st.set_page_config(page_title="Guia de Treino e Alimentação", layout="wide")

st.title("📘 Guia de Treino + Alimentação Diária")
st.markdown("Acompanhe sua rotina de treinos e alimentação. Marque os itens concluídos e salve seu progresso!")

# ------------------------------------------
# Dia da semana atual (padrão)
# ------------------------------------------
dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
hoje = datetime.datetime.now().strftime("%A")
hoje_pt = dias_semana[datetime.datetime.today().weekday()]

dia = st.selectbox("📅 Escolha o dia da semana", dias_semana, index=dias_semana.index(hoje_pt))

# ------------------------------------------
# Dados do cardápio diário (do PDF adaptado)
# ------------------------------------------
cardapio = {
    "Segunda-feira": [
        ("Café da manhã", "JEJUM (até 12h - 18h)"), "JEJUM (até 12h - 18h)"), "JEJUM (até 12h - 18h)"), "2 ovos grandes, pão integral, queijo branco ou shake de whey + frutas vermelhas + linhaça"),
        ("Almoço", "Strogonoff de frango fit + arroz integral + salada"), "150g peito de frango + 100g batata-doce + salada"), "150g frango grelhado + 80g arroz integral + folhas verdes + azeite"), "Frango grelhado (150g), arroz integral (80g), feijão (80g), legumes (50g), azeite, salada à vontade"),
        ("Lanche", "Whey protein com água"), "Shake de whey com água"), "Shake de whey com água"), "Whey protein com água gelada ou iogurte + whey + morangos"),
        ("Jantar", "Omelete com queijo feta e espinafre + arroz negro"), "Tilápia assada + arroz negro + legumes cozidos"), "Omelete com 4 ovos + salada verde com azeite"), "Omelete com 4 ovos ou frango grelhado + salada + azeite")
    ],
    "Terça-feira": [
        ("Café da manhã", "JEJUM (até 12h - 18h)"), "JEJUM (até 12h - 18h)"), "JEJUM (até 12h - 18h)"), "2 ovos grandes, pão integral, queijo branco ou shake de whey + frutas vermelhas + linhaça"),
        ("Almoço", "Strogonoff de frango fit + arroz integral + salada"), "150g peito de frango + 100g batata-doce + salada"), "150g frango grelhado + 80g arroz integral + folhas verdes + azeite"), "Frango grelhado (150g), arroz integral (80g), feijão (80g), legumes (50g), azeite, salada à vontade"),
        ("Lanche", "Whey protein com água"), "Shake de whey com água"), "Shake de whey com água"), "Whey protein com água gelada ou iogurte + whey + morangos"),
        ("Jantar", "Omelete com queijo feta e espinafre + arroz negro"), "Tilápia assada + arroz negro + legumes cozidos"), "Omelete com 4 ovos + salada verde com azeite"), "Rap10 com frango desfiado, creme de ricota, tomate, orégano")
    ],
    "Quarta-feira": [
        ("Café da manhã", "JEJUM (até 12h - 18h)"), "JEJUM (até 12h - 18h)"), "JEJUM (até 12h - 18h)"), "2 ovos grandes, pão integral, queijo branco ou shake de whey + frutas vermelhas + linhaça"),
        ("Almoço", "Strogonoff de frango fit + arroz integral + salada"), "150g peito de frango + 100g batata-doce + salada"), "150g frango grelhado + 80g arroz integral + folhas verdes + azeite"), "Frango grelhado (150g), arroz integral (80g), feijão (80g), legumes (50g), azeite, salada à vontade"),
        ("Lanche", "Whey protein com água"), "Shake de whey com água"), "Shake de whey com água"), "Whey protein com água gelada ou iogurte + whey + morangos"),
        ("Jantar", "Omelete com queijo feta e espinafre + arroz negro"), "Tilápia assada + arroz negro + legumes cozidos"), "Omelete com 4 ovos + salada verde com azeite"), "Omelete com 4 ovos, tomate picado, salada de folhas")
    ],
    "Quinta-feira": [
        ("Café da manhã", "JEJUM (até 12h - 18h)"), "JEJUM (até 12h - 18h)"), "JEJUM (até 12h - 18h)"), "2 ovos grandes, pão integral, queijo branco ou shake de whey + frutas vermelhas + linhaça"),
        ("Almoço", "Strogonoff de frango fit + arroz integral + salada"), "150g peito de frango + 100g batata-doce + salada"), "150g frango grelhado + 80g arroz integral + folhas verdes + azeite"), "Frango grelhado (150g), arroz integral (80g), feijão (80g), legumes (50g), azeite, salada à vontade"),
        ("Lanche", "Whey protein com água"), "Shake de whey com água"), "Shake de whey com água"), "Whey protein com água gelada ou iogurte + whey + morangos"),
        ("Jantar", "Omelete com queijo feta e espinafre + arroz negro"), "Tilápia assada + arroz negro + legumes cozidos"), "Omelete com 4 ovos + salada verde com azeite"), "Rap10 com carne moída e creme de ricota, alface, tomate")
    ],
    "Sexta-feira": [
        ("Café da manhã", "JEJUM (até 12h - 18h)"), "JEJUM (até 12h - 18h)"), "JEJUM (até 12h - 18h)"), "2 ovos grandes, pão integral, queijo branco ou shake de whey + frutas vermelhas + linhaça"),
        ("Almoço", "Strogonoff de frango fit + arroz integral + salada"), "150g peito de frango + 100g batata-doce + salada"), "150g frango grelhado + 80g arroz integral + folhas verdes + azeite"), "Frango grelhado (150g), arroz integral (80g), feijão (80g), legumes (50g), azeite, salada à vontade"),
        ("Lanche", "Whey protein com água"), "Shake de whey com água"), "Shake de whey com água"), "Whey protein com água gelada ou iogurte + whey + morangos"),
        ("Jantar", "Omelete com queijo feta e espinafre + arroz negro"), "Tilápia assada + arroz negro + legumes cozidos"), "Omelete com 4 ovos + salada verde com azeite"), "Frango grelhado ou omelete com salada e azeite")
    ],
    "Sábado": [
        ("Café da manhã", "JEJUM (até 12h - 18h)"), "JEJUM (até 12h - 18h)"), "JEJUM (até 12h - 18h)"), "2 ovos grandes, pão integral, queijo branco ou shake de whey + frutas vermelhas + linhaça"),
        ("Almoço", "Strogonoff de frango fit + arroz integral + salada"), "150g peito de frango + 100g batata-doce + salada"), "150g frango grelhado + 80g arroz integral + folhas verdes + azeite"), "Filé mignon + quinoa + brócolis"),
        ("Lanche", "Whey protein com água"), "Shake de whey com água"), "Shake de whey com água"), "Mix de nozes + suco de laranja natural"),
        ("Jantar", "Omelete com queijo feta e espinafre + arroz negro"), "Tilápia assada + arroz negro + legumes cozidos"), "Omelete com 4 ovos + salada verde com azeite"), "Peito de frango ao forno + arroz integral + salada")
    ],
    "Domingo": [
        ("Café da manhã", "JEJUM (até 12h - 18h)"), "JEJUM (até 12h - 18h)"), "JEJUM (até 12h - 18h)"), "Crepioca de queijo cottage + café"),
        ("Almoço", "Strogonoff de frango fit + arroz integral + salada"), "150g peito de frango + 100g batata-doce + salada"), "150g frango grelhado + 80g arroz integral + folhas verdes + azeite"), "Peixe grelhado + batata-doce + legumes assados"),
        ("Lanche", "Whey protein com água"), "Shake de whey com água"), "Shake de whey com água"), "Shake de proteína + pão integral"),
        ("Jantar", "Omelete com queijo feta e espinafre + arroz negro"), "Tilápia assada + arroz negro + legumes cozidos"), "Omelete com 4 ovos + salada verde com azeite"), "Sopa de legumes com frango desfiado")
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



