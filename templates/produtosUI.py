import streamlit as st
import pandas as pd
from views import View
import datetime

class ProdutosUI:
   def main():
      st.header("Produtos")
      tab1, tab2, tab3, tab4 = st.tabs(["Todos", "Mais vendidos", "Novidade", "Em alta"])
      with tab1: ProdutosUI.listar()
      with tab2: ProdutosUI.mais_vendidos()
      # with tab3: ProdutosUI.novidade()
      with tab4: ProdutosUI.em_alta()

   def listar():
      produtos = View.produto_listar()
      if len(produtos) == 0:
         st.write("Nenhum produto cadastrado")
      else:
         dic = []
         for obj in produtos: dic.append(obj.__dict__)
         df = pd.DataFrame(dic)
         st.dataframe(df)

   # def novidade():

   def mais_vendidos():
      st.write("Nenhum produto vendido")

   def em_alta():
      st.write("Nenhum produto em alta")