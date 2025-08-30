import streamlit as st
import datetime

st.set_page_config(page_title="Guia de Treino e Alimentação", layout="wide")
st.title("📘 Guia de Treino + Alimentação Diária")
st.markdown("Acompanhe sua rotina de treinos e alimentação. Marque os itens concluídos e salve seu progresso!")

dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
hoje = datetime.datetime.now().strftime("%A")
hoje_pt = dias_semana[datetime.datetime.today().weekday()]
dia = st.selectbox("📅 Escolha o dia da semana", dias_semana, index=dias_semana.index(hoje_pt))

cardapio = {
    "Segunda-feira": [
        ("Café da manhã", "Jejum Intermitente (até 12h ou até 18h)"),
        ("Almoço", "150g frango grelhado ou carne magra, 80g arroz integral ou raízes, salada e legumes à vontade"),
        ("Lanche", "Whey com água ou iogurte + whey + morangos"),
        ("Jantar", "Opções:
- Omelete 4 ovos + salada
- Wrap de frango com creme de ricota
- Frango grelhado + legumes")
    ],
    "Terça-feira": [
        ("Café da manhã", "2 ovos + pão integral + queijo branco ou shake de whey"),
        ("Almoço", "Frango ou carne + arroz + feijão + legumes + azeite"),
        ("Lanche", "Iogurte ou pão + frango + ricota"),
        ("Jantar", "Wrap ou omelete + salada")
    ],
    "Quarta-feira": [
        ("Café da manhã", "Jejum Intermitente (até 12h ou até 18h)"),
        ("Almoço", "Frango ou carne + arroz + legumes + azeite"),
        ("Lanche", "Whey com água ou iogurte + whey + morangos"),
        ("Jantar", "Omelete ou wrap + salada")
    ],
    "Quinta-feira": [
        ("Café da manhã", "Shake de whey + frutas vermelhas + linhaça"),
        ("Almoço", "Peixe ou carne + arroz + legumes + azeite"),
        ("Lanche", "Whey + morangos ou pão + proteína"),
        ("Jantar", "Omelete ou prato leve com salada")
    ],
    "Sexta-feira": [
        ("Café da manhã", "Jejum Intermitente (até 12h ou até 18h)"),
        ("Almoço", "Frango ou carne + arroz + legumes + salada"),
        ("Lanche", "Whey + morangos ou iogurte com whey"),
        ("Jantar", "Wrap ou omelete + folhas verdes")
    ],
    "Sábado": [
        ("Café da manhã", "2 ovos + pão integral + queijo branco"),
        ("Almoço", "Carne magra + arroz integral + legumes + azeite"),
        ("Lanche", "Mix de castanhas ou whey + fruta"),
        ("Jantar", "Frango assado + salada")
    ],
    "Domingo": [
        ("Café da manhã", "Crepioca com queijo cottage + café"),
        ("Almoço", "Peixe + batata-doce + legumes"),
        ("Lanche", "Whey + pão integral ou shake"),
        ("Jantar", "Sopa de legumes + frango desfiado")
    ]
}

st.subheader("🍽️ Cardápio do Dia")
with st.form("form_cardapio"):
    for refeicao, descricao in cardapio[dia]:
        st.checkbox(f"{refeicao}: {descricao}", key=f"refeicao_{refeicao}_{dia}")
    st.form_submit_button("✅ Salvar refeições concluídas")

st.markdown("---")
st.caption("🔁 Integração futura com painel histórico e analytics | Desenvolvido com ❤️ no Streamlit")

