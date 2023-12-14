import streamlit as st
import pandas as pd
from views import View

class ManterFabricanteUI:
  def main():
    st.header("Cadastro de Fabricante")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterFabricanteUI.listar()
    with tab2: ManterFabricanteUI.inserir()
    with tab3: ManterFabricanteUI.atualizar()
    with tab4: ManterFabricanteUI.excluir()    

  def listar():
    fabricantes = View.fabricante_listar()
    if len(fabricantes) == 0:
      st.write("Nenhum fabricante cadastrado")
    else:
      dic = []
      for obj in fabricantes: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def inserir():
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    endereco = st.text_input("Informe o endereço")
    telefone = st.text_input("Informe o telefone")
    if st.button("Inserir"):
      View.fabricante_inserir(nome, email, endereco, telefone)
      st.success("Fabricante inserido com sucesso")

  def atualizar():
    fabricantes = View.fabricante_listar()
    if len(fabricantes) == 0:
      st.write("Nenhum fabricante cadastrado")
    else:
      op = st.selectbox("Atualização de Fabricantes", fabricantes)
      nome = st.text_input("Informe o novo nome", op.get_nome())
      email = st.text_input("Informe o novo e-mail", op.get_email())
      endereco = st.text_input("Informe o novo endereço", op.get_endereco())
      telefone = st.text_input("Informe o novo telefone", op.get_telefone())
      if st.button("Atualizar"):
        id = op.get_id()
        View.fabricante_atualizar(id, nome, email, endereco, telefone)
        st.success("Fabricante atualizado com sucesso")


  def excluir():
    fabricantes = View.fabricante_listar()
    if len(fabricantes) == 0:
      st.write("Nenhum fabricante cadastrado")
    else:
      op = st.selectbox("Exclusão de Fabricantes", fabricantes)
      if st.button("Excluir"):
        id = op.get_id()
        View.fabricante_excluir(id)
        st.success("Fabricante excluído com sucesso")