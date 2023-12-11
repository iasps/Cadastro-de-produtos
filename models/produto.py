import json

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

    def set_id(self, id): self.__id
    def set_nome(self, nome): self.__nome
    def set_descricao(self, descricao): self.__descricao
    def set_preco(self, preco): self.__preco
    def set_id_grupo(self, id_grupo): self.__id_grupo
    def set_id_fabricante(self, id_fabricante): self.__id_fabricante


class NProduto:
    __produtos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.__produtos:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        cls.__produtos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__produtos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.__produtos:
            if obj.get_id() == id: return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            aux.set_nome(obj.get_nome())
            aux.set_descricao(obj.get_descricao())
            aux.set_preco(obj.get_preco())
            aux.set_id_grupo(obj.get_id_grupo())
            aux.set_id_fabricante(obj.get_id_fabricante())
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            cls.__produtos.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__produtos = []
        try:
            with open("produtos.json", mode="r") as arquivo:
                produtos_json = json.load(arquivo)
                for obj in produtos_json:
                    aux = Produto(obj["Produto_id"], 
                                  obj["Produto_nome"],
                                  obj["Produto_descricao"],
                                  obj["Produto_preco"])
                    cls.__produtos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump(cls.__produtos, arquivo, default=vars)