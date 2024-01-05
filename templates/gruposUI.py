import streamlit as st

from views import View
import pandas as pd
from views import View

class GruposUI:
  def main():
    st.header("Grupos")
    tabs = []
    grupos = View.grupo_listar()
    if len(grupos) == 0:
      st.write("Nenhum grupo cadastrado")
    else:
      for grupo in grupos:
        nome = grupo.get_nome()
        tabs.append(nome)

      tabsui = st.tabs(tabs)

      for i in range(len(tabs)):
        with tabsui[i]:
          data = View.produto_do_grupo(tabs[i])
          df = pd.DataFrame(data)
          st.dataframe(df, hide_index=True)
