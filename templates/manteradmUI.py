import streamlit as st
import pandas as pd
from views import View

class ManterAdmUI:
  def main():
    st.header("Cadastro de Adm")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterAdmUI.listar()
    with tab2: ManterAdmUI.inserir()
    with tab3: ManterAdmUI.atualizar()
    with tab4: ManterAdmUI.excluir()    

  def listar():
    adms = View.adm_listar()
    if len(adms) == 0:
      st.write("Nenhum adm cadastrado")
    else:
      dic = []
      for obj in adms: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def inserir():
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    senha = st.text_input("Informe a senha")
    if st.button("Inserir"):
      View.adm_inserir(nome, email, senha)
      st.success("Adm inserido com sucesso")

  def atualizar():
    adms = View.adm_listar()
    if len(adms) == 0:
      st.write("Nenhum adm cadastrado")
    else:
      op = st.selectbox("Atualização de Adms", adms)
      nome = st.text_input("Informe o novo nome", op.get_nome())
      email = st.text_input("Informe o novo e-mail", op.get_email())
      senha = st.text_input("Informe a nova senha")
      if st.button("Atualizar"):
        id = op.get_id()
        View.adm_atualizar(id, nome, email, senha)
        st.success("Adm atualizado com sucesso")


  def excluir():
    adms = View.adm_listar()
    if len(adms) == 0:
      st.write("Nenhum adm cadastrado")
    else:
      op = st.selectbox("Exclusão de Adms", adms)
      if st.button("Excluir"):
        id = op.get_id()
        if len(adms) == 1:
          st.error("Não é possível excluir o adm. São necessários no mínimo dois adm's para poder excluir um.")
        else:
          View.adm_excluir(id)
          st.success("Adm excluído com sucesso")
        # id = op.get_id()
        # View.adm_excluir(id)
        # st.success("Adm excluído com sucesso")