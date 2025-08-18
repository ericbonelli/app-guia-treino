import streamlit as st

st.set_page_config(page_title="Guia de Treino e Alimentação", layout="wide")

dias_semana = [
    "Segunda-feira", "Terça-feira", "Quarta-feira",
    "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"
]

treinos = {
    "Segunda-feira": '''**Treino A – Pernas e Core**
1️⃣ [Agachamento Livre – 4x10](https://www.youtube.com/watch?v=sqk1DJv5H-g)
2️⃣ [Leg Press 45° – 3x12](https://www.youtube.com/watch?v=IZxyjW7MPJQ)
3️⃣ [Stiff com Halteres – 3x12](https://www.youtube.com/watch?v=6TSP1TRMUzs)
4️⃣ [Afundo com Passada – 3x10 por perna](https://www.youtube.com/watch?v=QOVaHwm-Q6U)
5️⃣ [Elevação de Panturrilha no Smith – 4x15](https://www.youtube.com/watch?v=YMmgqO8Jo-k)
6️⃣ [Prancha Abdominal com Carga – 3x40s](https://www.youtube.com/watch?v=pSHjTRCQxIw)
💥 Finalizador: Agachamento com salto + corrida no lugar (2 min, 20s ON / 10s OFF)''',

    "Terça-feira": '''**Treino B – Peito, Tríceps e Ombros**
1️⃣ [Supino Reto com Barra – 4x10](https://www.youtube.com/watch?v=rT7DgCr-3pg)
2️⃣ [Supino Inclinado com Halteres – 3x12](https://www.youtube.com/watch?v=8iPEnn-ltC8)
3️⃣ [Desenvolvimento Militar com Barra – 3x10](https://www.youtube.com/watch?v=qEwKCR5JCog)
4️⃣ [Tríceps Testa com Barra EZ – 3x12](https://www.youtube.com/watch?v=vB5OHsJ3EME)
5️⃣ [Tríceps Corda no Cross – 3x12](https://www.youtube.com/watch?v=vB5OHsJ3EME)
6️⃣ [Abdominal Oblíquo com Peso – 3x15 por lado](https://www.youtube.com/watch?v=DJQGX2J4IVw)
💥 Finalizador: Flexão Explosiva + Burpees (3x30s cada)''',

    "Quarta-feira": '''**Natação**
🏊 10 min de aquecimento (nado leve)
🏊 5x100m com 30s de pausa (ritmo moderado)
🏊 4x50m tiros com 15s de pausa
🏊 10 min regenerativo''',

    "Quinta-feira": '''**Treino C – Costas e Bíceps**
1️⃣ [Barra Fixa – 4x6-8](https://www.youtube.com/watch?v=3YvfRx31xDE)
2️⃣ [Remada Curvada com Barra – 3x12](https://www.youtube.com/watch?v=vT2GjY_Umpw)
3️⃣ [Pulldown Polia Alta – 3x10](https://www.youtube.com/watch?v=CAwf7n6Luuc)
4️⃣ [Rosca Direta com Barra EZ – 3x12](https://www.youtube.com/watch?v=kwG2ipFRgfo)
5️⃣ [Rosca Martelo com Halteres – 3x12](https://www.youtube.com/watch?v=zC3nLlEvin4)
6️⃣ [Hiperextensão Lombar com Peso – 3x15](https://www.youtube.com/watch?v=ph3pddpKzzw)
💥 Finalizador: Kettlebell Swing + Remada TRX (2x30s cada)''',

    "Sexta-feira": '''**Natação**
🏊 10 min de aquecimento (nado leve)
🏊 5x100m com 30s de pausa (ritmo moderado)
🏊 4x50m tiros com 15s de pausa
🏊 10 min regenerativo''',

    "Sábado": '''**Treino D – Full Body Metabólico**
1️⃣ [Levantamento Terra – 4x8](https://www.youtube.com/watch?v=ytGaGIn3SjE)
2️⃣ [Agachamento Frontal – 3x10](https://www.youtube.com/watch?v=5iDHTnIjwYg)
3️⃣ [Supino Fechado – 3x12](https://www.youtube.com/watch?v=EVvE2JDFK1Q)
4️⃣ [Remada Unilateral com Halteres – 3x12](https://www.youtube.com/watch?v=pYcpY20QaE8)
5️⃣ [Ab Wheel – 3x15](https://www.youtube.com/watch?v=VO2oTjqay9Y)
💥 Finalizador: Sled + Corda Naval (3x30s cada)''',

    "Domingo": '''**Recuperação Ativa**
🚶 Caminhada acelerada 45 min ou bike 30 min  
🧘 Alongamento, mobilidade ou yoga'''
}

st.title("📅 Guia de Treino e Alimentação")
dia = st.selectbox("Selecione o dia da semana:", dias_semana)

st.subheader(f"🏋️ Treino do dia - {dia}")
st.markdown(treinos[dia])
