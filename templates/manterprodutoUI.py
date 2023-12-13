import streamlit as st
import pandas as pd
from views import View

class ManterProdutoUI:
  def main():
    st.header("Cadastro de Produtos")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterProdutoUI.listar()
    with tab2: ManterProdutoUI.inserir()
    with tab3: ManterProdutoUI.atualizar()
    with tab4: ManterProdutoUI.excluir()    

  def listar():
    produtos = View.produto_listar()
    if len(produtos) == 0:
      st.write("Nenhum produto cadastrado")
    else:  
      dic = []
      for obj in produtos: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def inserir():
    nome = st.text_input("Informe o nome")
    descricao = st.text_input("Informe a descrição")
    preco = st.text_input("Informe o preço (R$)")
    grupos = View.grupo_listar()
    grupo = st.selectbox("Selecione o grupo", grupos)
    fabricantes = View.fabricante_listar()
    fabricante = st.selectbox("Selecione o fabricante", fabricantes)
    if st.button("Inserir"):
      try:
        View.produto_inserir(nome, descricao, float(preco), grupo.get_id(), fabricante.get_id())
        st.success("Produto inserido com sucesso")
      except:
        st.error("Preço inválido!")  

  def atualizar():
    produtos = View.produto_listar()
    if len(produtos) == 0:
      st.write("Nenhum produto cadastrado")
    else:  
      op = st.selectbox("Atualização de Produtos", produtos)
      nome = st.text_input("Informe o novo nome", op.get_nome())
      descricao = st.text_input("Informe a nova descrição", op.get_descricao())
      preco = st.text_input("Informe o novo preço (R$)", op.get_preco())
      grupos = View.grupo_listar()
      grupo_atual = View.grupo_listar_id(op.get_id_grupo())
      if grupo_atual is not None:
        grupo = st.selectbox("Selecione o novo grupo", grupos, grupos.index(grupo_atual))
      else:  
      grupo = st.selectbox("Selecione o novo grupo", grupos)
      fabricantes = View.servico_listar()
      fabricante_atual = View.servico_listar_id(op.get_id_fabricante())
      if fabricante_atual is not None:
        fabricante = st.selectbox("Selecione o novo fabricante", fabricantes, fabricantes.index(fabricante_atual))
      else:
        fabricante = st.selectbox("Selecione o novo fabricante", fabricantes)
      if st.button("Atualizar"):
        id = op.get_id()
        View.produto_atualizar(id, nome, descricao, float(preco), grupo.get_id(), fabricante.get_id())
        st.success("Produto atualizado com sucesso")

  def excluir():
    produtos = View.produto_listar()
    if len(produtos) == 0:
      st.write("Nenhum produto cadastrado")
    else:  
      op = st.selectbox("Exclusão de Produtos", produtos)
      if st.button("Excluir"):
        id = op.get_id()
        View.produto_excluir(id)
        st.success("Produto excluído com sucesso")