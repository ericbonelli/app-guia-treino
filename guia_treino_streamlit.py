import streamlit as st
import datetime
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime as dt
import pandas as pd
import plotly.express as px

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Guia de Treino e Alimentação", layout="wide")
st.title("📘 Guia de Treino + Alimentação Diária")
st.markdown("Acompanhe sua rotina de treinos e alimentação. Marque os itens concluídos e salve seu progresso!")

# CONEXÃO COM PLANILHA
@st.cache_data(ttl=300)
def carregar_dados():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=scopes 
    )
    client = gspread.authorize(creds)
    worksheet = client.open("Guia_Treino_Alimentacao").worksheet("Dados")
    registros = worksheet.get_all_records()
    return pd.DataFrame(registros)

# --- SELEÇÃO DA DATA (nova lógica) ---
data_escolhida = st.date_input("📅 Escolha a data do registro", value=datetime.date.today())
dia_semana = data_escolhida.strftime("%A")

# Traduzir dia da semana para PT-BR
dias_semana_pt = {
    "Monday": "Segunda-feira",
    "Tuesday": "Terça-feira",
    "Wednesday": "Quarta-feira",
    "Thursday": "Quinta-feira",
    "Friday": "Sexta-feira",
    "Saturday": "Sábado",
    "Sunday": "Domingo"
}
dia = dias_semana_pt.get(dia_semana, "Dia inválido")
st.markdown(f"🗓️ **Dia escolhido:** {dia} ({data_escolhida.strftime('%d/%m/%Y')})")

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
            data_escolhida.strftime("%Y-%m-%d),  # timestamp
            dia,  # dia da semana derivado
            ", ".join(refeicoes_dia),
            ", ".join(treinos_dia),
            ", ".join(cardio_dia)
        ]

        # 4. Inserir nova linha
        aba.append_row(linha)
        st.success("✅ Dados salvos com sucesso na planilha!")

    except Exception as e:
        st.error(f"❌ Erro ao salvar na planilha: {e}")
        
# DASHBOARD E ANÁLISE DE PROGRESSO
st.markdown("---")
st.header("📊 Progresso e Análises")
df = carregar_dados()

if not df.empty:
    df['Data'] = pd.to_datetime(df['Timestamp'], errors='coerce').dt.date
    df['Treinos'] = df['Treinos'].apply(lambda x: str(x).split(", ") if isinstance(x, str) else [])
    df['Qtd_Treinos'] = df['Treinos'].apply(lambda x: len(x))

    resumo7 = df[df['Data'] >= dt.now().date() - pd.Timedelta(days=7)]
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("📅 Dias registrados", f"{df['Data'].nunique()} dias")
    kpi2.metric("🏃 Cardio realizado", f"{df['Cardio'].apply(lambda x: len(str(x).strip()) > 0).sum()} dias")
    jejum_count = df['Refeições'].str.contains("Jejum").sum()
    jejum_pct = jejum_count / len(df) * 100
    kpi3.metric("⏳ Jejum", f"{jejum_count} dias", f"{jejum_pct:.1f}%")

    st.markdown("<hr style='border:1px solid #ccc'>", unsafe_allow_html=True)
    gr1, gr2 = st.columns(2)

    with gr1:
        st.subheader("📌 Dias com Registro")
        fig_dias = px.histogram(df, x='Data', nbins=10)
        st.plotly_chart(fig_dias, use_container_width=True)

        st.subheader("💪 Exercícios mais frequentes")
        treino_explodido = df.explode('Treinos')
        treino_explodido['Treinos'] = treino_explodido['Treinos'].str.strip()
        treino_counts = treino_explodido['Treinos'].value_counts().reset_index()
        treino_counts.columns = ['Exercício', 'Frequência']
        fig_freq = px.bar(treino_counts, x='Exercício', y='Frequência')
        st.plotly_chart(fig_freq, use_container_width=True)

    with gr2:
        st.subheader("📈 Evolução dos treinos")
        fig_evo = px.line(df, x='Data', y='Qtd_Treinos', markers=True)
        st.plotly_chart(fig_evo, use_container_width=True)

        st.subheader("📆 Últimos 7 dias")
        st.write(f"🏋️ Treinos: {resumo7['Qtd_Treinos'].sum()} exercícios")
        st.write(f"🍽️ Dias com refeições: {resumo7['Refeições'].apply(lambda x: len(x) > 0).sum()} dias")
        st.write(f"🏃 Cardio: {resumo7['Cardio'].apply(lambda x: len(str(x).strip()) > 0).sum()} dias")
else:
    st.info("Nenhum dado registrado ainda.")

st.markdown("---")
st.caption("🔁 Integração com Google Sheets ativada | Desenvolvido com ❤️ no Streamlit")
