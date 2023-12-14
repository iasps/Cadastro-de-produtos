import streamlit as st
import pandas as pd
from views import View

class ManterGrupoUI:
  def main():
    st.header("Cadastro de Grupo")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterGrupoUI.listar()
    with tab2: ManterGrupoUI.inserir()
    with tab3: ManterGrupoUI.atualizar()
    with tab4: ManterGrupoUI.excluir()


  def grupos_fixos():
    grupos_fixos = ["Todos", "Alimentos e Bebidas", "Automotivos", "Eletrônicos", "Eletrodomésticos", "Móveis", "Brinquedos", "Outros"]

  def listar():
    grupos = View.grupo_listar()
    if len(grupos) == 0:
      st.write("Nenhum grupo cadastrado")
    else:
      dic = []
      for obj in grupos: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def inserir():
    nome = st.text_input("Informe o nome")
    if st.button("Inserir"):
      View.grupo_inserir(nome)
      st.success("Grupo inserido com sucesso")

  def atualizar():
    grupos = View.grupo_listar()
    if len(grupos) == 0:
      st.write("Nenhum grupo cadastrado")
    else:
      op = st.selectbox("Atualização de Grupos", grupos)
      nome = st.text_input("Informe o novo nome", op.get_nome())
      if st.button("Atualizar"):
        id = op.get_id()
        View.grupo_atualizar(id, nome)
        st.success("Grupo atualizado com sucesso")


  def excluir():
    grupos = View.grupo_listar()
    if len(grupos) == 0:
      st.write("Nenhum grupo cadastrado")
    else:
      op = st.selectbox("Exclusão de Grupos", grupos)
      if st.button("Excluir"):
        id = op.get_id()
        View.grupo_excluir(id)
        st.success("Grupo excluído com sucesso")