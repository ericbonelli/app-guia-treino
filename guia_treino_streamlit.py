import streamlit as st
import datetime
import requests
from datetime import datetime as dt

# Configuração da página
st.set_page_config(page_title="Guia de Treino e Alimentação", layout="wide")
st.title("📘 Guia de Treino + Alimentação Diária")
st.markdown("Acompanhe sua rotina de treinos e alimentação. Marque os itens concluídos e salve seu progresso!")

# Dia da semana (padrão: hoje)
dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
hoje_pt = dias_semana[datetime.datetime.today().weekday()]
dia = st.selectbox("📅 Escolha o dia da semana", dias_semana, index=dias_semana.index(hoje_pt))

# Cardápio com jejum seg/qua/sex
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

# Treinos musculação
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

# Cardápio com checkbox
st.subheader("🍽️ Cardápio do Dia")
refeicoes_dia = []
for refeicao, descricao in cardapio[dia]:
    marcado = st.checkbox(f"{refeicao}: {descricao}", key=f"ref_{refeicao}_{dia}")
    if marcado:
        refeicoes_dia.append(f"{refeicao}: {descricao}")

# Treinos com checkbox
st.subheader("🏋️ Exercícios de Musculação")
tipo_treino = st.selectbox("Escolha o tipo de treino", list(treinos.keys()))
treinos_dia = []
for exercicio, link in treinos[tipo_treino]:
    marcado = st.checkbox(f"[{exercicio}]({link})", key=f"ex_{exercicio}_{dia}")
    if marcado:
        treinos_dia.append(exercicio)

# Cardio do dia
st.subheader("🏃 Cardio")
cardio_dia = []
if dia in ["Segunda-feira", "Sábado", "Domingo"]:
    if st.checkbox("Corrida (30-40min)", key=f"corrida_{dia}"):
        cardio_dia.append("Corrida")
if dia in ["Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"]:
    if st.checkbox("Natação (45min)", key=f"natacao_{dia}"):
        cardio_dia.append("Natação")

# Envio único
st.markdown("### 📤 Salvar e Enviar")
if st.button("📤 Enviar Dia para Registro"):
    webhook_url = "https://1bfd4a66ff01.ngrok-free.app/webhook/guia-treino"
    payload = {
        "dia": dia,
        "refeicoes": refeicoes_dia,
        "treino": treinos_dia,
        "cardio": cardio_dia,
        "timestamp": dt.now().isoformat()
    }
    try:
        r = requests.post(webhook_url,json=payload,headers={"Content-Type": "application/json"})
        if r.status_code == 200:
            st.success("✅ Dados enviados com sucesso ao n8n!")
        else:
            st.warning(f"⚠️ Erro {r.status_code} ao enviar para o n8n.")
    except Exception as e:
        st.error(f"Erro ao conectar com webhook: {e}")

st.markdown("---")
st.caption("🔁 Integração futura com painel histórico e analytics | Desenvolvido com ❤️ no Streamlit")
