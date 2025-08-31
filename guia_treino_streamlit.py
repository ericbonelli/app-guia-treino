import streamlit as st
import datetime
import gspread
from google.oauth2.service_account import Credentials 
from datetime import datetime as dt

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Guia de Treino e Alimentação", layout="wide")
st.title("📘 Guia de Treino + Alimentação Diária")
st.markdown("Acompanhe sua rotina de treinos e alimentação. Marque os itens concluídos e salve seu progresso!")

# --- SELEÇÃO DO DIA ---
dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
hoje = datetime.datetime.today().weekday()
dia = st.selectbox("📅 Escolha o dia da semana", dias_semana, index=hoje)

# --- CARDÁPIO ---
cardapio = {
    "Segunda-feira": [("Jejum", "Dia de jejum com até 500 calorias"),
                      ("Almoço", "150g frango grelhado + 80g arroz integral + salada com azeite"),
                      ("Lanche", "Whey protein com água ou iogurte desnatado com morangos"),
                      ("Jantar", "Omelete 4 ovos ou wrap integral com frango e ricota")],
    "Terça-feira": [("Café da manhã", "2 ovos + pão integral + queijo branco"),
                    ("Almoço", "Filé de frango + arroz integral + feijão + legumes + salada"),
                    ("Lanche", "Whey com água ou iogurte desnatado + morangos ou wrap"),
                    ("Jantar", "Omelete ou wrap integral com carne moída e vegetais")],
    "Quarta-feira": [("Jejum", "Dia de jejum com até 500 calorias"),
                     ("Almoço", "Frango grelhado + arroz + legumes + azeite"),
                     ("Lanche", "Iogurte ou pão com frango e requeijão light"),
                     ("Jantar", "Wrap de Rap10 com carne moída + alface + tomate")],
    "Quinta-feira": [("Café da manhã", "Shake de whey + frutas vermelhas + linhaça"),
                     ("Almoço", "Peixe ou carne + arroz integral + legumes + salada"),
                     ("Lanche", "Whey com morangos ou pão integral com proteína"),
                     ("Jantar", "Omelete ou prato leve com proteína + salada")],
    "Sexta-feira": [("Jejum", "Dia de jejum com até 500 calorias"),
                    ("Almoço", "Frango grelhado + arroz integral + legumes + salada"),
                    ("Lanche", "Whey com morangos ou iogurte com whey"),
                    ("Jantar", "Wrap ou omelete com folhas verdes e azeite")],
    "Sábado": [("Café da manhã", "Crepioca de queijo cottage + café"),
               ("Almoço", "Peito de frango ao forno + arroz integral + salada"),
               ("Lanche", "Mix de nozes + suco de laranja natural"),
               ("Jantar", "Tilápia assada + legumes + azeite")],
    "Domingo": [("Café da manhã", "Cuscuz com ovo mexido + café"),
                ("Almoço", "Peixe grelhado + batata-doce + salada"),
                ("Lanche", "Iogurte + frutas"),
                ("Jantar", "Sopa de legumes com frango desfiado")]
}

# --- TREINOS ---
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

# --- CHECKBOXES: Alimentação ---
st.subheader("🍽️ Cardápio do Dia")
refeicoes_dia = []
for refeicao, descricao in cardapio[dia]:
    if st.checkbox(f"{refeicao}: {descricao}", key=f"ref_{refeicao}_{dia}"):
        refeicoes_dia.append(f"{refeicao}: {descricao}")

# --- CHECKBOXES: Treinos ---
st.subheader("🏋️ Exercícios de Musculação")
tipo_treino = st.selectbox("Escolha o tipo de treino", list(treinos.keys()))
treinos_dia = []
for exercicio, link in treinos[tipo_treino]:
    if st.checkbox(f"[{exercicio}]({link})", key=f"ex_{exercicio}_{dia}"):
        treinos_dia.append(exercicio)

# --- CHECKBOXES: Cardio ---
st.subheader("🏃 Cardio")
cardio_dia = []
if dia in ["Segunda-feira", "Sábado", "Domingo"]:
    if st.checkbox("Corrida (30-40min)", key=f"corrida_{dia}"):
        cardio_dia.append("Corrida")
elif dia in ["Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"]:
    if st.checkbox("Natação (45min)", key=f"natacao_{dia}"):
        cardio_dia.append("Natação")

# --- ENVIO PARA GOOGLE SHEETS ---
st.markdown("### 📤 Salvar e Enviar para Google Sheets")

if st.button("📤 Enviar Dia para Registro"):
    try:
        # 1. Autenticação com credenciais do Streamlit secrets
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = Credentials.from_service_account_info(
            st.secrets["gcp_service_account"],
            scopes=scopes 
        )

        client = gspread.authorize(creds)

        # 2. Abrir planilha e aba
        sheet = client.open("Guia_Treino_Alimentacao")  # Nome da planilha no Google Drive
        aba = sheet.worksheet("Dados")  # Nome da aba

        # 3. Dados a registrar
        linha = [
            dt.now().strftime("%Y-%m-%d %H:%M:%S"),
            dia,
            ", ".join(refeicoes_dia),
            ", ".join(treinos_dia),
            ", ".join(cardio_dia)
        ]

        # 4. Inserir nova linha
        aba.append_row(linha)
        st.success("✅ Dados salvos com sucesso na planilha!")

    except Exception as e:
        st.error(f"❌ Erro ao salvar na planilha: {e}")

st.markdown("---")
st.caption("🔁 Integração com Google Sheets ativada | Desenvolvido com ❤️ no Streamlit")
