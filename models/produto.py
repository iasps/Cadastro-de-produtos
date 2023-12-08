import json

class Produto:
    def __init__(self, id, nome, descricao, preco, data_de_fabricacao, data_de_validade, id_grupo, id_fabricante):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__preco = preco
        self.__data_de_fabricacao = data_de_fabricacao
        self.__data_de_validade = data_de_validade
        self.__id_grupo = id_grupo
        self.__id_fabricante = id_fabricante

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_descricao(self): return self.__descricao
    def get_preco(self): return self.__preco
    def get_data_de_fabricacao(self): return self.__data_de_fabricacao
    def get_data_de_validade(self): return self.__data_de_validade
    def get_id_grupo(self): return self.__id_grupo
    def get_id_fabricante(self): return self.__id_fabricante

    def set_id(self, id): self.__id
    def set_nome(self, nome): self.__nome
    def set_descricao(self, descricao): self.__descricao
    def set_preco(self, preco): self.__preco
    def set_data_de_fabricacao(self, data_de_fabricacao): self.__data_de_fabricacao
    def set_data_de_validade(self, data_de_validade): self.__data_de_validade
    def set_id_grupo(self, id_grupo): self.__id_grupo
    def set_id_fabricante(self, id_fabricante): self.__id_fabricante


# class NProduto:
