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
def carregar_dados(forcar=False):
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

# --- IMPORTAÇÕES FIXAS PARA CARDÁPIO E TREINOS (sem alteração aqui, por limitação do diff) ---
# ... (mantido como está)

# --- ENVIO PARA GOOGLE SHEETS ---
st.markdown("### 📤 Salvar e Enviar para Google Sheets")

if st.button("📤 Enviar Dia para Registro"):
    try:
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = Credentials.from_service_account_info(
            st.secrets["gcp_service_account"],
            scopes=scopes 
        )
        client = gspread.authorize(creds)
        sheet = client.open("Guia_Treino_Alimentacao")
        aba = sheet.worksheet("Dados")
        linha = [
            data_escolhida.strftime("%Y-%m-%d"),
            dia,
            ", ".join(refeicoes_dia),
            ", ".join(treinos_dia),
            ", ".join(cardio_dia)
        ]
        aba.append_row(linha)
        st.success("✅ Dados salvos com sucesso na planilha!")
        st.cache_data.clear()
        st.rerun()
    except Exception as e:
        st.error(f"❌ Erro ao salvar na planilha: {e}")

# --- DASHBOARD E ANÁLISE DE PROGRESSO ---
st.markdown("---")
st.header("📊 Progresso e Análises")

df = carregar_dados()

if not df.empty:
    df['Data'] = pd.to_datetime(df['Timestamp'], errors='coerce').dt.date
    df['Treinos'] = df['Treinos'].apply(lambda x: str(x).split(", ") if isinstance(x, str) else [])
    df['Qtd_Treinos'] = df['Treinos'].apply(lambda x: len(x))
    df['Data'] = df['Data'].apply(lambda x: x if isinstance(x, datetime.date) else x.date())

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
        fig_dias = px.histogram(df, x='Data')
        fig_dias.update_xaxes(type='category')
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
        df_agrupado = df.groupby('Data', as_index=False)['Qtd_Treinos'].sum()
        fig_evo = px.line(df_agrupado, x='Data', y='Qtd_Treinos', markers=True)
        fig_evo.update_xaxes(type='category')
        st.plotly_chart(fig_evo, use_container_width=True)

        st.subheader("📆 Últimos 7 dias")
        st.write(f"🏋️ Treinos: {resumo7['Qtd_Treinos'].sum()} exercícios")
        st.write(f"🍽️ Dias com refeições: {resumo7['Refeições'].apply(lambda x: len(x) > 0).sum()} dias")
        st.write(f"🏃 Cardio: {resumo7['Cardio'].apply(lambda x: len(str(x).strip()) > 0).sum()} dias")
else:
    st.info("Nenhum dado registrado ainda.")

# --- EDIÇÃO DE REGISTROS ANTERIORES ---
st.markdown("---")
st.subheader("✏️ Editar Registros Anteriores")

with st.expander("Editar Registro Existente"):
    if not df.empty:
        datas_existentes = sorted(df['Data'].unique(), reverse=True)
        data_edicao = st.selectbox("Escolha a data para editar:", datas_existentes)
        linha_original = df[df['Data'] == data_edicao].iloc[0]

        st.write(f"### {linha_original['Dia']} – {data_edicao}")

        refeicoes_antigas = str(linha_original['Refeições']).split(", ")
        treinos_antigos = str(linha_original['Treinos']).split(", ")
        cardio_antigo = str(linha_original['Cardio'])

        refeicoes_editadas = st.text_area("🍽️ Refeições:", value=", ".join(refeicoes_antigas))
        treinos_editados = st.text_area("🏋️ Treinos:", value=", ".join(treinos_antigos))
        cardio_editado = st.text_input("🏃 Cardio:", value=cardio_antigo)

        if st.button("💾 Salvar Edição"):
            try:
                creds = Credentials.from_service_account_info(
                    st.secrets["gcp_service_account"],
                    scopes=scopes 
                )
                client = gspread.authorize(creds)
                aba = client.open("Guia_Treino_Alimentacao").worksheet("Dados")
                todas = aba.get_all_records()

                idx = next((i for i, row in enumerate(todas) if row['Timestamp'].startswith(str(data_edicao))), None)
                if idx is not None:
                    aba.delete_rows(idx + 2)
                    nova = [
                        str(data_edicao),
                        linha_original['Dia'],
                        refeicoes_editadas,
                        treinos_editados,
                        cardio_editado
                    ]
                    aba.insert_row(nova, idx + 2)
                    st.success("Registro atualizado com sucesso!")
                    st.cache_data.clear()
                    st.rerun()
                else:
                    st.warning("Registro não localizado.")
            except Exception as e:
                st.error(f"Erro ao editar: {e}")

st.markdown("---")
st.caption("🔁 Integração com Google Sheets ativada | Desenvolvido com ❤️ no Streamlit")


