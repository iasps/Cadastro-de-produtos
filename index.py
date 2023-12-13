from templates.produtosUI import ProdutosUI
from templates.gruposUI import GruposUI
from templates.fabricantesUI import FabricantesUI
from templates.loginUI import LoginUI
from templates.manterprodutoUI import ManterProdutoUI
from templates.mantergrupoUI import ManterGrupoUI
from templates.manterfabricanteUI import ManterFabricanteUI
from templates.manteradmUI import ManterAdmUI
from templates.editarperfilUI import EditarPerfilUI
# from views import View
import streamlit as st

class IndexUI:

  def menu_visitante():
    op = st.sidebar.selectbox("Menu", ["Produtos", "Grupos", "Fabricantes", "Login"])
    if op == "Produtos": ProdutosUI.main()
    if op == "Grupos": GruposUI.main()
    if op == "Fabricantes": FabricantesUI.main()
    if op == "Login": LoginUI.main()

  def menu_adm():
    op = st.sidebar.selectbox("Menu", ["Manter Produto", "Manter Grupo", "Manter Fabricante",  "Manter Adm","Editar perfil"])
    if op == "Manter Produto": ManterProdutoUI.main()
    if op == "Manter Grupo": ManterGrupoUI.main()
    if op == "Manter Fabricante": ManterFabricanteUI.main()
    if op == "Manter Adm": ManterAdmUI.main()
    if op == "Editar perfil": EditarPerfilUI.main()


  def btn_logout():
    if st.sidebar.button("Logout"):
      del st.session_state["adm_id"]
      # del st.session_state["cliente_nome"]
#      st.rerun()

  def sidebar():
    if "adm_id" not in st.session_state:
      IndexUI.menu_visitante()   
    else:
      st.sidebar.write("Bem-vindo(a), " + st.session_state["adm_nome"])
      if st.session_state["adm_nome"] == "adm": IndexUI.menu_adm()
      else: IndexUI.menu_visitante()
      IndexUI.btn_logout()  

  def main():
    # View.adm()
    IndexUI.sidebar()

IndexUI.main()