import streamlit as st

st.set_page_config(page_title="Guia de Treino e Alimentação", layout="wide")

st.title("🏋️ Guia Diário de Treino e Cardápio")
st.write("Selecione o dia da semana para visualizar o treino e o cardápio.")

dias = [
    "Segunda-feira", "Terça-feira", "Quarta-feira",
    "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"
]

dia_selecionado = st.selectbox("📅 Escolha o dia:", dias)

treinos = {
    "Segunda-feira": {
        "titulo": "Treino A – Pernas e Core",
        "detalhes": [
            "[1️⃣ Agachamento Livre – 4x10](https://www.youtube.com/watch?v=U3HlEF_E9fo)",
            "[2️⃣ Leg Press 45° – 3x12](https://www.youtube.com/watch?v=IZxyjW7MPJQ)",
            "[3️⃣ Stiff com Halteres – 3x12](https://www.youtube.com/watch?v=OPwB0Gf7kzU)",
            "[4️⃣ Afundo com Passada – 3x10 por perna](https://www.youtube.com/watch?v=wrwwXE_x-pQ)",
            "[5️⃣ Elevação de Panturrilha no Smith – 4x15](https://www.youtube.com/watch?v=YMmgqO8Jo-k)",
            "[6️⃣ Prancha Abdominal com carga – 3x40s](https://www.youtube.com/watch?v=pSHjTRCQxIw)",
            "**💥 Finalizador**: Agachamento com Salto + Corrida no lugar (20s ON / 10s OFF – 2 min)"
        ]
    },
    "Terça-feira": {
        "titulo": "Treino B – Peito, Tríceps e Ombros",
        "detalhes": [
            "[1️⃣ Supino Reto com Barra – 4x10](https://www.youtube.com/watch?v=rT7DgCr-3pg)",
            "[2️⃣ Supino Inclinado com Halteres – 3x12](https://www.youtube.com/watch?v=8iPEnn-ltC8)",
            "[3️⃣ Desenvolvimento Militar – 3x10](https://www.youtube.com/watch?v=qEwKCR5JCog)",
            "[4️⃣ Tríceps Testa com Barra EZ – 3x12](https://www.youtube.com/watch?v=vB5OHsJ3EME)",
            "[5️⃣ Tríceps Corda no Cross – 3x12](https://www.youtube.com/watch?v=vB5OHsJ3EME)",
            "[6️⃣ Abdominal Oblíquo com Peso – 3x15 por lado](https://www.youtube.com/watch?v=DJQGX2J4IVw)",
            "**💥 Finalizador**: Flexão Explosiva + Burpees (30s cada x3)"
        ]
    },
    "Quarta-feira": {
        "titulo": "🏊 Natação + Core",
        "detalhes": [
            "🔹 Aquecimento: 10 min nado leve",
            "🔹 5x100m ritmo moderado com 30s de pausa",
            "🔹 4x50m tiros fortes com 15s de pausa",
            "🔹 Nado regenerativo: 10 min",
            "🔹 Extra: Abdominais e prancha 3x"
        ]
    },
    "Quinta-feira": {
        "titulo": "Treino C – Costas e Bíceps",
        "detalhes": [
            "[1️⃣ Barra Fixa – 4x6-8](https://www.youtube.com/watch?v=eGo4IYlbE5g)",
            "[2️⃣ Remada Curvada com Barra – 3x12](https://www.youtube.com/watch?v=vT2GjY_Umpw)",
            "[3️⃣ Pulldown na Polia Alta – 3x10](https://www.youtube.com/watch?v=lueEJGjTuPQ)",
            "[4️⃣ Rosca Direta com Barra – 3x12](https://www.youtube.com/watch?v=kwG2ipFRgfo)",
            "[5️⃣ Rosca Martelo com Halteres – 3x12](https://www.youtube.com/watch?v=zC3nLlEvin4)",
            "[6️⃣ Hiperextensão Lombar com Peso – 3x15](https://www.youtube.com/watch?v=2SzjLs5bNok)",
            "**💥 Finalizador**: Kettlebell Swing + Remada TRX (30s x2)"
        ]
    },
    "Sexta-feira": {
        "titulo": "🏊 Natação + Core",
        "detalhes": [
            "🔹 Repetir protocolo de quarta-feira"
        ]
    },
    "Sábado": {
        "titulo": "Treino D – Full Body Metabólico",
        "detalhes": [
            "[1️⃣ Deadlift – 4x8](https://www.youtube.com/watch?v=op9kVnSso6Q)",
            "[2️⃣ Agachamento Frontal – 3x10](https://www.youtube.com/watch?v=t2b8UdqmlFs)",
            "[3️⃣ Supino Fechado – 3x12](https://www.youtube.com/watch?v=tKjcgfu44sI)",
            "[4️⃣ Remada Unilateral – 3x12](https://www.youtube.com/watch?v=roCP6wCXPqo)",
            "[5️⃣ Ab Wheel – 3x15](https://www.youtube.com/watch?v=QvR1B8KxFhA)",
            "**💥 Finalizador**: Sled + Corda Naval (30s x3)"
        ]
    },
    "Domingo": {
        "titulo": "Cardio + Mobilidade",
        "detalhes": [
            "🚶 Caminhada acelerada 45 min ou 🚴 Pedal leve 30 min",
            "🧘 Sessão de alongamentos ou yoga leve"
        ]
    }
}

cardapio = {
    "Segunda-feira": "Omelete, iogurte, frango com arroz, shake com banana, tilápia grelhada, chá com queijo branco",
    "Terça-feira": "Tapioca, maçã, carne magra com quinoa, iogurte com aveia, omelete de atum, caseína",
    "Quarta-feira": "Panqueca de banana, castanhas, frango e batata-doce, shake + pasta amendoim, tilápia assada, ovo cozido",
    "Quinta-feira": "Mingau com whey, castanhas, salmão e mandioquinha, iogurte + frutas, frango ao curry, pasta de amendoim",
    "Sexta-feira": "Ovos cozidos, amêndoas, strogonoff fit, shake + banana, omelete + arroz negro, iogurte com linhaça",
    "Sábado": "Cuscuz + ovo, iogurte + chia, mignon + quinoa, nozes + suco, frango assado, leite + chocolate",
    "Domingo": "Crepioca, amendoim, peixe + batata-doce, shake + pão integral, sopa de legumes, leite + pasta amendoim"
}

st.subheader(f"🏋️ {treinos[dia_selecionado]['titulo']}")
for item in treinos[dia_selecionado]['detalhes']:
    st.markdown(f"- {item}")

st.markdown("---")
st.subheader("🍽️ Cardápio do Dia")
st.markdown(f"**{cardapio[dia_selecionado]}**")
