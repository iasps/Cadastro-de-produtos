# from models.grupo import Grupo, NGrupo
from models.produto import Produto, NProduto
# from models.fabricante import Fabricante, NFabricante
from models.adm import Adm, NAdm
# import datetime

class View:

  def adm_inserir(nome, email, senha):
    adm = Adm(0, nome, email, senha)
    NAdm.inserir(adm)

  def adm_listar():
    return NAdm.listar()
  
  def adm_listar_id(id):
    return NAdm.listar_id(id)

  def adm_atualizar(id, nome, email, senha):
    adm = Adm(id, nome, email, senha)
    NAdm.atualizar(adm)
    
  def adm_excluir(id):
    adm = Adm(id, "", "", "")
    NAdm.excluir(adm)    

  def adm_adm():
    for adm in View.adm_listar():
      if adm.get_nome() == "adm": return
    View.adm_inserir("adm", "adm", "adm")  

  def adm_login(email, senha):
    for adm in View.adm_listar():
      if adm.get_email() == email and adm.get_senha() == senha:
        return adm
    return None




  def produto_listar():
    return NProduto.listar()

  def produto_listar_id(id):
    return NProduto.listar_id(id)

  def produto_inserir(nome, descricao, preco, id_grupo, id_fabricante):
    if preco < 0: raise ValueError("Preço inválido")
    NProduto.inserir(Produto(0, nome, descricao, preco, id_grupo, id_fabricante))

  def produto_atualizar(id, nome, descricao, preco, id_grupo, id_fabricante):
    if preco < 0: raise ValueError("Preço inválido")
    NProduto.atualizar(Produto(id, nome, descricao, preco, id_grupo, id_fabricante))

  def produto_excluir(id):
    NProduto.excluir(Produto(id, "", "", 0, 0, 0))





