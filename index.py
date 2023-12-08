# from templates.manterclienteUI import ManterClienteUI
# from templates.manterservicoUI import ManterServicoUI
# from templates.manteragendaUI import ManterAgendaUI
# from templates.abriragendaUI import AbrirAgendaUI
# from templates.loginUI import LoginUI
# from templates.agendahojeUI import AgendaHojeUI
# from templates.servicoreajusteUI import ServicoReajusteUI
# from templates.abrircontaUI import AbrirContaUI
# from templates.veragendaUI import VerAgendaUI
# from templates.editarperfilUI import EditarPerfilUI
# from templates.agendarhorarioUI import AgendarHorarioUI
# from templates.confirmarUI import ConfirmaUI
# from views import View

import streamlit as st

class IndexUI:

  def menu_visitante():
    op = st.sidebar.selectbox("Menu", ["Login"])
    if op == "Login": LoginUI.main()

  def menu_adm():
    op = st.sidebar.selectbox("Menu", ["Manter Produto", "Manter Grupo", "Manter Fabricante"])
    if op == "Manter Produto": ManterProdutoUI.main()
    if op == "Manter Grupo": ManterGrupoUI.main()
    if op == "Manter Fabricante": ManterFabricanteUI.main()

  def menu_cliente():
    op = st.sidebar.selectbox("Menu", ["Produtos", "Grupos", "Fabricantes", "Editar perfil"])
    if op == "Produtos": ProdutosUI.main()
    if op == "Agendar Horário": AgendarHorarioUI.main()
    if op == "Meus agendamentos": VerAgendaUI.main()
    if op == "Editar perfil": EditarPerfilUI.main()


  def btn_logout():
    if st.sidebar.button("Logout"):
      del st.session_state["cliente_id"]
      del st.session_state["cliente_nome"]
#      st.rerun()

  def sidebar():
    if "cliente_id" not in st.session_state:
      IndexUI.menu_visitante()   
    else:
      st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
      if st.session_state["cliente_nome"] == "admin": IndexUI.menu_admin()
      else: IndexUI.menu_cliente()
      IndexUI.btn_logout()  

  def main():
    View.cliente_admin()
    IndexUI.sidebar()

IndexUI.main()