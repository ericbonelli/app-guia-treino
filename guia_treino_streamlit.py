
import streamlit as st

st.set_page_config(page_title="Guia de Treino e Alimentação", layout="wide")

dias_semana = [
    "Segunda-feira", "Terça-feira", "Quarta-feira",
    "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"
]

cardapio = {
    "Segunda-feira": [
        "Café da manhã: Omelete + pão integral + café",
        "Lanche manhã: Iogurte + castanhas",
        "Almoço: Frango + arroz integral + salada",
        "Lanche tarde: Shake de whey + banana",
        "Jantar: Tilápia + purê batata-doce + legumes",
        "Ceia: Chá + queijo branco"
    ],
    "Terça-feira": [
        "Café da manhã: Tapioca + frango + queijo + café",
        "Lanche manhã: Maçã + amêndoas",
        "Almoço: Carne magra + quinoa + brócolis",
        "Lanche tarde: Iogurte + aveia + mel",
        "Jantar: Omelete de atum + arroz + rúcula",
        "Ceia: Iogurte natural"
    ],
    "Quarta-feira": [
        "Café da manhã: Panqueca de banana + whey",
        "Lanche manhã: Castanhas + café",
        "Almoço: Frango + batata-doce + salada",
        "Lanche tarde: Shake de whey + pasta de amendoim",
        "Jantar: Tilápia + arroz negro + cenoura",
        "Ceia: Chá verde + ovo cozido"
    ],
    "Quinta-feira": [
        "Café da manhã: Mingau de aveia + whey",
        "Lanche manhã: Castanhas + café",
        "Almoço: Salmão + purê mandioquinha + aspargos",
        "Lanche tarde: Iogurte + frutas vermelhas",
        "Jantar: Frango ao curry + arroz basmati + salada",
        "Ceia: Leite de amêndoas + pasta de amendoim"
    ],
    "Sexta-feira": [
        "Café da manhã: 3 ovos + pão integral + café",
        "Lanche manhã: Amêndoas + chá verde",
        "Almoço: Strogonoff fit + arroz integral + salada",
        "Lanche tarde: Shake de whey + banana",
        "Jantar: Omelete + arroz negro + espinafre",
        "Ceia: Iogurte + linhaça"
    ],
    "Sábado": [
        "Café da manhã: Cuscuz + ovo mexido + café",
        "Lanche manhã: Iogurte + chia",
        "Almoço: Filé mignon + quinoa + brócolis",
        "Lanche tarde: Nozes + suco natural",
        "Jantar: Frango assado + arroz integral + salada",
        "Ceia: Leite + chocolate 70%"
    ],
    "Domingo": [
        "Café da manhã: Crepioca + café",
        "Lanche manhã: Amendoins + chá verde",
        "Almoço: Peixe + batata-doce + legumes",
        "Lanche tarde: Shake + pão integral",
        "Jantar: Sopa de legumes + frango",
        "Ceia: Pasta de amendoim + leite"
    ],
}

treinos = {
    "Segunda-feira": "Treino A – Pernas e Core:
"
        "- [Agachamento Livre](https://www.youtube.com/watch?v=sqk1DJv5H-g)
"
        "- [Leg Press 45°](https://www.youtube.com/watch?v=wE6P5sUvb6M)
"
        "- [Stiff com Halteres](https://www.youtube.com/watch?v=1uDiW5--rAE)
"
        "- [Afundo com Passada](https://www.youtube.com/watch?v=QOVaHwm-Q6U)
"
        "- [Elevação de Panturrilha no Smith](https://www.youtube.com/watch?v=YMmgqO8Jo-k)
"
        "- [Prancha Abdominal](https://www.youtube.com/watch?v=pSHjTRCQxIw)",
    "Terça-feira": "Treino B – Peito, Tríceps e Ombros:
"
        "- [Supino Reto com Barra](https://www.youtube.com/watch?v=vthMCtgVtFw)
"
        "- [Supino Inclinado com Halteres](https://www.youtube.com/watch?v=8iPEnn-ltC8)
"
        "- [Desenvolvimento Militar](https://www.youtube.com/watch?v=B-aVuyhvLHU)
"
        "- [Tríceps Testa com Barra EZ](https://www.youtube.com/watch?v=ir5PsbniVSc)
"
        "- [Tríceps Corda no Cross](https://www.youtube.com/watch?v=2-LAMcpzODU)
"
        "- [Abdominal Oblíquo com Peso](https://www.youtube.com/watch?v=KTOfDkXcO9Q)",
    "Quarta-feira": "🏊 Natação 45 min + Mobilidade",
    "Quinta-feira": "Treino C – Costas e Bíceps:
"
        "- [Barra Fixa](https://www.youtube.com/watch?v=1nRRlk6264I)
"
        "- [Remada Curvada com Barra](https://www.youtube.com/watch?v=vT2GjY_Umpw)
"
        "- [Pulldown Pegada Aberta](https://www.youtube.com/watch?v=lueEJGjTuPQ)
"
        "- [Rosca Direta com Barra EZ](https://www.youtube.com/watch?v=kwG2ipFRgfo)
"
        "- [Rosca Martelo com Halteres](https://www.youtube.com/watch?v=zC3nLlEvin4)
"
        "- [Hiperextensão Lombar](https://www.youtube.com/watch?v=2tnATDflg4o)",
    "Sexta-feira": "🏊 Natação 45 min + Flexibilidade",
    "Sábado": "Treino D – Full Body Metabólico:
"
        "- [Deadlift](https://www.youtube.com/watch?v=op9kVnSso6Q)
"
        "- [Agachamento Frontal](https://www.youtube.com/watch?v=8QZIC_4d3M8)
"
        "- [Supino Fechado](https://www.youtube.com/watch?v=vR1QfYVEh0w)
"
        "- [Remada Unilateral com Halteres](https://www.youtube.com/watch?v=pYcpY20QaE8)
"
        "- [Ab Wheel](https://www.youtube.com/watch?v=1f8yoFFdkcY)",
    "Domingo": "🚶 Cardio leve + Alongamento"
}

st.title("🏋️ Guia de Treino e Alimentação - 7 Dias")

dia = st.selectbox("📅 Escolha o dia da semana:", dias_semana)

st.header(f"🍽️ Cardápio de {dia}")
for refeicao in cardapio[dia]:
    st.markdown(f"- {refeicao}")

st.header(f"🏋️ Treino do dia")
st.markdown(treinos[dia])

st.subheader("📊 Monitoramento")
peso = st.number_input("📌 Peso do dia (kg):", min_value=0.0, format="%.1f")
sono = st.slider("🛌 Horas de sono:", 0, 12, 7)
qualidade = st.slider("😴 Qualidade do sono (0 a 10):", 0, 10, 7)
