import streamlit as st
from views import View
import time

class LoginUI:
  def main():
    st.header("Entrar no Sistema")
    LoginUI.entrar()
    
  def entrar():
    email = st.text_input("Informe o e-mail")
    senha = st.text_input("Informe a senha")
    # st.button("Login")
    if st.button("Login"):
      adm = View.adm_login(email, senha) 
      if adm is not None:
        st.success("Login realizado com sucesso")
        st.success("Bem-vindo(a), " + adm.get_nome())
        st.session_state["adm_id"] = adm.get_id()
        st.session_state["adm_nome"] = adm.get_nome()
        time.sleep(2)
        st.rerun()
      else:
        st.error("Usuário ou senha inválido(s)")