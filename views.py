# from models.grupo import Grupo, NGrupo
# from models.produto import Produto, NProduto
# from models.fabricante import Fabricante, NFabricante
# from models.adm import Adm, NAdm
# import datetime

# class View:


#     def adm():
#         for adm in View.adm_listar():
#             if adm.get_nome() == "adm": return
#         View.adm_inserir("adm", "adm")  

#     def adm_login(email, senha):
#         for adm in View.adm_listar():
#             if adm.get_email() == email and adm.get_senha() == senha: return adm
#         return None




#     def grupo_inserir(nome):
#         grupo = Grupo(0, nome)
#         NGrupo.inserir(grupo)

#     def grupo_listar():
#         return NGrupo.listar()
  
#     def grupo_listar_id(id):
#         return NGrupo.listar_id(id)

#     def grupo_atualizar(id, nome):
#         grupo = Grupo(id, nome)
#         NGrupo.atualizar(grupo)
    
#     def grupo_excluir(id):
#         grupo = Grupo(id, "")
#         NGrupo.excluir(grupo)    



    # def produto_listar():
    #     return NProduto.listar()

#     def produto_listar_id(id):
#         return NProduto.listar_id(id)

#     def produto_inserir(nome, descricao, preco, data_de_fabricacao, data_de_validade):
#         hoje = datetime.datetime.today()
#         if preco < 0: raise ValueError("Preço inválido")
#         if data_de_fabricacao > hoje: raise ValueError("Data de fabricação inválida")
#         if data_de_validade < hoje: raise ValueError("O produto já está vencido!")
#         NProduto.inserir(Produto(0, descricao, preco, data_de_fabricacao, data_de_validade))

#     def produto_atualizar(id, nome, descricao, preco, data_de_fabricacao, data_de_validade):
#         hoje = datetime.datetime.today()
#         if preco < 0: raise ValueError("Preço inválido")
#         if data_de_fabricacao > hoje: raise ValueError("Data de fabricação inválida")
#         if data_de_validade < hoje: raise ValueError("O produto já está vencido!")
#         NProduto.atualizar(Produto(0, descricao, preco, data_de_fabricacao, data_de_validade))

#     def produto_excluir(id):
#         NProduto.excluir(Produto(id, "", "", 0, "", "", 0, 0))




#     def fabricante_listar():
#         return NFabricante.listar()

#     def fabricante_listar_id(id):
#         return NFabricante.listar_id()

    # def fabricante_grupo(grupo, horario, produto):
    #     NFabricante.atualizar(Fabricante(horario.get_id(), horario.get_data(), False, grupo, produto.get_id()))

    # def fabricante_listarsemana():
    #     r = []
    #     hoje = datetime.datetime.today()
    #     fds = hoje + datetime.timedelta(days = 7)
    #     for horario in View.fabricante_listar():
    #         if horario.get_confirmado() == False and fds.date() >= horario.get_data().date() >= hoje.date():
    #             r.append(horario)
    #     return r   

    # def fabricante_listargrupo(grupo):
    #     r = []
    #     for horario in View.fabricante_listar():
    #         if horario.get_id_grupo() == grupo.get_id():
    #             r.append(horario)
    #     return r

    # def fabricante_inserir(nome, email, endereco, telefone):
    #     NFabricante.inserir(Fabricante(0, nome, email, endereco, telefone))

    # def fabricante_atualizar(id, nome, email, endereco, telefone):
    #     NFabricante.atualizar(Fabricante(id, nome, email, endereco, telefone))

    # def fabricante_excluir(id):
    #     NFabricante.excluir(Fabricante(id, "", "", "", ""))

