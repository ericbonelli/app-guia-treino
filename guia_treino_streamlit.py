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
    ],
    "Quarta-feira": [
        ("Café da manhã", "Panqueca de banana com aveia"),
        ("Almoço", "Peito de frango + batata-doce assada + salada"),
        ("Lanche", "Shake de whey + pasta de amendoim"),
        ("Jantar", "Tilápia assada com arroz negro + cenoura cozida")
    ],
    "Quinta-feira": [
        ("Café da manhã", "Mingau de aveia com whey + canela"),
        ("Almoço", "Salmão grelhado + purê de mandioquinha + aspargos"),
        ("Lanche", "Iogurte proteico + frutas vermelhas"),
        ("Jantar", "Frango ao curry + arroz basmati + salada")
    ],
    "Sexta-feira": [
        ("Café da manhã", "3 ovos cozidos + pão integral + café preto"),
        ("Almoço", "Strogonoff de frango fit + arroz integral + salada"),
        ("Lanche", "Whey protein + banana"),
        ("Jantar", "Omelete com queijo feta e espinafre + arroz negro")
    ],
    "Sábado": [
        ("Café da manhã", "Cuscuz com ovo mexido + café preto"),
        ("Almoço", "Filé mignon grelhado + quinoa + brócolis"),
        ("Lanche", "Mix de nozes + suco de laranja"),
        ("Jantar", "Peito de frango ao forno + arroz integral + salada")
    ],
    "Domingo": [
        ("Café da manhã", "Crepioca de queijo cottage + café"),
        ("Almoço", "Peixe grelhado + batata-doce + legumes assados"),
        ("Lanche", "Shake de proteína + 1 fatia de pão integral"),
        ("Jantar", "Sopa de legumes com frango desfiado")
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

st.subheader("🏋️ Treino d

