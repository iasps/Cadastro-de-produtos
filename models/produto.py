import json
from models.crud import CRUD


class Produto:
    def __init__(self, id, nome, descricao, preco, id_grupo, id_fabricante):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__preco = preco
        self.__id_grupo = id_grupo
        self.__id_fabricante = id_fabricante

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_descricao(self): return self.__descricao
    def get_preco(self): return self.__preco
    def get_id_grupo(self): return self.__id_grupo
    def get_id_fabricante(self): return self.__id_fabricante

    def set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome
    def set_descricao(self, descricao): self.__descricao = descricao
    def set_preco(self, preco): self.__preco = preco
    def set_id_grupo(self, id_grupo): self.__id_grupo = id_grupo
    def set_id_fabricante(self, id_fabricante): self.__id_fabricante = id_fabricante

    def __eq__(self, x):
        if self.__id == x.__id and self.__nome == x.__nome and self.__descricao == x.__descricao and self.__preco == x.__preco and self.__id_grupo == x.__id_grupo and self.__id_fabricante == x.__id_fabricante:
            return True
        return False
    
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__descricao} - {self.__preco} - {self.__id_grupo} - {self.__id_fabricante}"

    def to_json(self):
        return {
            'Id' : self.__id,
            'Nome' : self.__nome,
            'Descricao' : self.__descricao,
            'Preco' : self.__preco,
            'Id_grupo' : self.__id_grupo,
            'Id_fabricante' : self.__id_fabricante}


class NProduto(CRUD):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("produtos.json", mode="r") as arquivo:
                produtos_json = json.load(arquivo)
                for obj in produtos_json:
                    aux = Produto(obj["_Produto__id"], 
                                  obj["_Produto__nome"],
                                  obj["_Produto__descricao"],
                                  obj["_Produto__preco"],
                                  obj["_Produto__id_grupo"],
                                  obj["_Produto__id_fabricante"])
                    cls.objetos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)