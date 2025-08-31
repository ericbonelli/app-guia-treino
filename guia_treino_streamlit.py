import streamlit as st
import datetime
import requests

st.set_page_config(page_title="Guia Diário de Treino e Cardápio", layout="wide")
st.title("📘 Guia Diário de Treino e Cardápio")

dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
hoje = datetime.datetime.today().weekday()
dia = st.selectbox("📅 Selecione o dia", dias_semana, index=hoje)

# --- CARDÁPIO ---
st.markdown("## 🍽️ Cardápio do Dia")
check_cafe = st.checkbox("☑️ Café da manhã: 2 ovos, pão integral, queijo branco ou shake")
check_almoco = st.checkbox("☑️ Almoço: Frango, arroz integral, legumes, salada")
check_lanche = st.checkbox("☑️ Lanche: Mix de nozes ou whey")
check_jantar = st.checkbox("☑️ Jantar: Frango ao forno, sopa ou prato leve com vegetais")

# JEJUM (aparece só seg/qua/sex)
jejum = False
if dia in ["Segunda-feira", "Quarta-feira", "Sexta-feira"]:
    jejum = st.checkbox("⏱️ Dia de Jejum (Seg/Qua/Sex)")

# --- TREINO ---
st.markdown("## 🏋️ Treino do Dia")
check_treino_a = st.checkbox("Treino A – Pernas e Core")
check_treino_b = st.checkbox("Treino B – Peito e Tríceps")
check_treino_c = st.checkbox("Treino C – Costas e Bíceps")

# --- CARDIO ---
st.markdown("## 🏃 Cardio")
check_corrida = st.checkbox("🏃 Corrida")
check_natacao = st.checkbox("🏊 Natação")

# --- BOTÃO DE ENVIO ---
if st.button("💾 Salvar Dia"):
    dados = {
        "dia": dia,
        "jejum": jejum,
        "cardapio": {
            "cafe": check_cafe,
            "almoco": check_almoco,
            "lanche": check_lanche,
            "jantar": check_jantar
        },
        "treino": {
            "treino_a": check_treino_a,
            "treino_b": check_treino_b,
            "treino_c": check_treino_c
        },
        "cardio": {
            "corrida": check_corrida,
            "natacao": check_natacao
        }
    }

    try:
        webhook_url = "https://1bfd4a66ff01.ngrok-free.app/webhook/guia-treino"  # sua URL do n8n via ngrok
        res = requests.post(webhook_url, json=dados)
        if res.status_code == 200:
            st.success("✅ Dados enviados com sucesso!")
        else:
            st.error(f"❌ Erro ao enviar dados: {res.status_code}")
    except Exception as e:
        st.error(f"Erro de conexão com webhook: {e}")
