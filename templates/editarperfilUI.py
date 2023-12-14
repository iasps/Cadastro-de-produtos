import streamlit as st
from views import View

class EditarPerfilUI:
    def main():
        st.header("Editar perfil")
        EditarPerfilUI.atualizar()

    def atualizar():
        op = View.adm_listar_id(st.session_state["adm_id"])
        nome = "adm"
        # if op.get_nome() != "adm":        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        senha = st.text_input("Informe a nova senha")
        if st.button("Editar"):
            id = op.get_id()
            View.adm_atualizar(id, nome, email, senha)
            st.success("Perfil editado com sucesso")