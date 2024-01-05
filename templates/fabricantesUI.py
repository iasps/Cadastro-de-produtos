import streamlit as st
import pandas as pd
from views import View

class FabricantesUI:
   def main():
      st.header("Fabricantes")
      FabricantesUI.listar()

   def listar():
      fabricantes = View.fabricante_listar()
      if len(fabricantes) == 0:
         st.write("Nenhum fabricante cadastrado")
      else:
         dic = []
         for obj in fabricantes: dic.append(obj.__dict__)
         df = pd.DataFrame(dic)
         st.dataframe(df)