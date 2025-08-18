import streamlit as st

st.set_page_config(page_title="Guia de Treinos e Cardápio", layout="centered")

dias = [
    "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira",
    "Sexta-feira", "Sábado", "Domingo"
]

treinos = {
    "Segunda-feira": '''Treino A – Pernas e Core
1️⃣ Agachamento Livre – 4x10 [🔗](https://youtu.be/aclHkVaku9U)
2️⃣ Leg Press 45° – 3x12 [🔗](https://youtu.be/IZxyjW7MPJQ)
3️⃣ Stiff com Halteres – 3x12 [🔗](https://youtu.be/RZp4L-PF7RE)
4️⃣ Afundo com Passada – 3x10 por perna [🔗](https://youtu.be/QOVaHwm-Q6U)
5️⃣ Elevação de Panturrilha no Smith – 4x15 [🔗](https://youtu.be/-M4-G8p8fmc)
6️⃣ Prancha Abdominal – 3x40s [🔗](https://youtu.be/pSHjTRCQxIw)
💥 Finalizador: 2 min de Agachamento com Salto + Corrida no lugar (20s ON / 10s OFF)
''',
    "Terça-feira": '''Treino B – Peito, Tríceps e Ombros
1️⃣ Supino Reto com Barra – 4x10 [🔗](https://youtu.be/vcBIG73ojpE)
2️⃣ Supino Inclinado com Halteres – 3x12 [🔗](https://youtu.be/8iPEnn-ltC8)
3️⃣ Desenvolvimento Militar com Barra – 3x10 [🔗](https://youtu.be/2yjwXTZQDDI)
4️⃣ Tríceps Testa com Barra EZ – 3x12 [🔗](https://youtu.be/_gsUck-7M74)
5️⃣ Tríceps Corda no Cross – 3x12 [🔗](https://youtu.be/2-LAMcpzODU)
6️⃣ Abdominal Oblíquo com Peso – 3x15 por lado [🔗](https://youtu.be/5c6vvZQ44iE)
💥 Finalizador: 3x (Flexão Explosiva + Burpees – 30s cada)
''',
    "Quarta-feira": '''Natação (45 min)
• Aquecimento: 10 min nado leve
• 5x100m moderado (pausa 30s)
• 4x50m forte (pausa 15s)
• 10 min nado regenerativo
''',
    "Quinta-feira": '''Treino C – Costas e Bíceps
1️⃣ Barra Fixa – 4x6-8 [🔗](https://youtu.be/eGo4IYlbE5g)
2️⃣ Remada Curvada com Barra – 3x12 [🔗](https://youtu.be/vT2GjY_Umpw)
3️⃣ Pulldown na Polia Alta – 3x10 [🔗](https://youtu.be/lueEJGjTuPQ)
4️⃣ Rosca Direta com Barra EZ – 3x12 [🔗](https://youtu.be/kwG2ipFRgfo)
5️⃣ Rosca Martelo com Halteres – 3x12 [🔗](https://youtu.be/zC3nLlEvin4)
6️⃣ Hiperextensão Lombar com Peso – 3x15 [🔗](https://youtu.be/gsnoPHQ1HFM)
💥 Finalizador: Kettlebell Swing + Remada TRX – 30s cada
''',
    "Sexta-feira": '''Natação (45 min)
• Aquecimento: 10 min nado leve
• 5x100m moderado (pausa 30s)
• 4x50m forte (pausa 15s)
• 10 min nado regenerativo
''',
    "Sábado": '''Treino D – Full Body Metabólico
1️⃣ Deadlift – 4x8 [🔗](https://youtu.be/ytGaGIn3SjE)
2️⃣ Agachamento Frontal – 3x10 [🔗](https://youtu.be/t2b8UdqmlFs)
3️⃣ Supino Fechado – 3x12 [🔗](https://youtu.be/d_Ru3h1TgqM)
4️⃣ Remada Unilateral com Halteres – 3x12 [🔗](https://youtu.be/pYcpY20QaE8)
5️⃣ Ab Wheel – 3x15 [🔗](https://youtu.be/_FVZtZO2-1o)
💥 Finalizador: Sled + Corda Naval – 3x 30s
''',
    "Domingo": '''Cardio Leve + Mobilidade
• Caminhada acelerada 45 min ou pedal 30 min  
• Alongamento ou Yoga guiado [🔗](https://youtu.be/v7AYKMP6rOE)
'''
}

st.title("🏋️ Guia de Treinos e Cardápio Semanal")

dia_escolhido = st.selectbox("📅 Escolha o dia da semana:", dias)

st.subheader(f"🧠 Treino do dia – {dia_escolhido}")
st.markdown(treinos.get(dia_escolhido, "Treino não encontrado."), unsafe_allow_html=True)
