import streamlit as st
import cola 
def calcula_media(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) / 4

def tabela_nota(media):
    if media >= 7:
        return "aprovado"
    elif 5 <= media < 7:
        return "recuperaçao"
    else:
        return "reprovado"

st.title("Calculadora de Média Escolar")

with st.form("formulario_boletim2"):
    nota1 = st.number_input("Nota 1:", min_value=0.0, max_value=10.0, step=0.1)
    nota2 = st.number_input("Nota 2:", min_value=0.0, max_value=10.0, step=0.1)
    nota3 = st.number_input("Nota 3:", min_value=0.0, max_value=10.0, step=0.1)
    nota4 = st.number_input("Nota 4:", min_value=0.0, max_value=10.0, step=0.1)

    calcular = st.form_submit_button("Calcular Média")

if calcular:
    media = calcula_media(nota1, nota2, nota3, nota4)
    status = tabela_nota(media)

    if status == "aprovado":
        st.success(f"Média Final: {media:.2f} — Aprovado 🎉")
    elif status == "recuperaçao":
        st.warning(f"Média Final: {media:.2f} — Recuperação ⚠️")
    else:
        st.error(f"Média Final: {media:.2f} — Reprovado ❌")

# Barra lateral
with st.sidebar:
    st.header("Painel do Aluno")
    st.write("- Histórico Escolar")
    st.write("- Notas por Bimestre")
    st.write("- Média Final do Ano")
    st.write("- Contato com a Coordenação")
    import streamlit as st

st.title("Sistema Escolar Completo")

# Menu lateral com mais opções
menu = st.sidebar.radio("Menu", ["Calcular Média", "Histórico Escolar", "Estatísticas", "Contato", "Configurações"])

# --- FUNÇÕES AUXILIARES ---
def mostrar_historico():
    st.header("Histórico Escolar")

    # Dados fictícios mais detalhados
    historico = {
        "Disciplina": ["Matemática", "Português", "Ciências", "História", "Geografia"],
        "1º Bimestre": [7.5, 8.0, 6.5, 7.0, 7.2],
        "2º Bimestre": [6.8, 7.5, 7.0, 6.5, 7.0],
        "3º Bimestre": [8.2, 7.8, 7.3, 7.7, 7.4],
        "4º Bimestre": [7.0, 8.5, 7.5, 7.8, 7.9],
    }

    st.table(historico)

def mostrar_estatisticas():
    st.header("Estatísticas do Aluno")

    # Estatísticas fictícias
    notas = [7.5, 6.8, 8.2, 7.0, 7.2, 7.5, 7.0, 7.8, 7.4, 7.9]
    media_geral = sum(notas) / len(notas)
    st.write(f"Média geral: {media_geral:.2f}")
    st.write(f"Nota máxima: {max(notas):.2f}")
    st.write(f"Nota mínima: {min(notas):.2f}")

    st.bar_chart(notas)

def contato():
    st.header("Contato com a Coordenação")
    nome = st.text_input("Seu nome")
    email = st.text_input("Seu e-mail")
    mensagem = st.text_area("Mensagem")

    if st.button("Enviar"):
        if nome and email and mensagem:
            st.success("Mensagem enviada com sucesso! Entraremos em contato.")
            # Aqui você pode adicionar código para enviar email real se quiser
        else:
            st.error("Por favor, preencha todos os campos.")

def configuracoes():
    st.header("Configurações")
    tema = st.selectbox("Tema do Aplicativo", ["Claro", "Escuro"])
    st.write(f"Você escolheu o tema: {tema}")
    # Poderia guardar essa configuração em arquivo ou cookie, mas é só exemplo

# --- CONTROLE DO MENU ---
if menu == "Calcular Média":
    st.header("Calculadora de Média Escolar")
    with st.form("formulario_boletim"):
        nota1 = st.number_input("Nota 1:", min_value=0.0, max_value=10.0, step=0.1)
        nota2 = st.number_input("Nota 2:", min_value=0.0, max_value=10.0, step=0.1)
        nota3 = st.number_input("Nota 3:", min_value=0.0, max_value=10.0, step=0.1)
        nota4 = st.number_input("Nota 4:", min_value=0.0, max_value=10.0, step=0.1)

        calcular = st.form_submit_button("Calcular Média")

    if calcular:
        media = calcula_media(nota1, nota2, nota3, nota4)
        status = tabela_nota(media)

        if status == "aprovado":
            st.success(f"Média Final: {media:.2f} — Aprovado 🎉")
        elif status == "recuperaçao":
            st.warning(f"Média Final: {media:.2f} — Recuperação ⚠️")
        else:
            st.error(f"Média Final: {media:.2f} — Reprovado ❌")

elif menu == "Histórico Escolar":
    mostrar_historico()

elif menu == "Estatísticas":
    mostrar_estatisticas()

elif menu == "Contato":
    contato()

elif menu == "Configurações":
    configuracoes()
