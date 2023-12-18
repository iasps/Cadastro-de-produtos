import json
from models.crud import CRUD


class Fabricante:
    def __init__(self, id, nome, email, endereco, telefone):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__endereco = endereco
        self.__telefone = telefone

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_endereco(self): return self.__endereco
    def get_telefone(self): return self.__telefone

    def set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome
    def set_email(self, email): self.__email = email
    def set_endereco(self, endereco): self.__endereco = endereco
    def set_telefone(self, telefone): self.__telefone = telefone

class NFabricante(CRUD):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("grupos.json", mode="r") as arquivo:
                fabricante_json = json.load(arquivo)
                for obj in fabricante_json:
                    aux = Fabricante(obj["Fabricante_id"], 
                                     obj["Fabricante_nome"],
                                     obj["Fabricante_email"],
                                     obj["Fabricante_endereco"],
                                     obj["Fabricante_telefone"])
                    cls.objetos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("fabricantes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)






            
    # __fabricantes = []

    # @classmethod
    # def inserir(cls, obj):
    #     cls.abrir()
    #     id = 0
    #     for aux in cls.__fabricantes:
    #         if aux.get_id() > id: id = aux.get_id()
    #     obj.set_id(id + 1)
    #     cls.__fabricantes.append(obj)
    #     cls.salvar()

    # @classmethod
    # def listar(cls):
    #     cls.abrir()
    #     return cls.__fabricantes

    # @classmethod
    # def listar_id(cls, id):
    #     cls.abrir()
    #     for obj in cls.__fabricantes:
    #         if obj.get_id() == id: return obj
    #     return None

    # @classmethod
    # def atualizar(cls, obj):
    #     cls.abrir()
    #     aux = cls.listar_id(obj.get_id())
    #     if aux is not None:
    #         aux.set_nome(obj.get_nome())
    #         aux.set_email(obj.get_email())
    #         aux.set_endereço(obj.get_endereço())
    #         aux.set_telefone(obj.get_telefone())
    #         cls.salvar()

    # @classmethod
    # def excluir(cls, obj):
    #     cls.abrir()
    #     aux = cls.listar_id(obj.get_id())
    #     if aux is not None:
    #         cls.__fabricantes.remove(aux)
    #         cls.salvar()

    # @classmethod
    # def abrir(cls):
    #     cls.__fabricantes = []
    #     try:
    #         with open("grupos.json", mode="r") as arquivo:
    #             fabricante_json = json.load(arquivo)
    #             for obj in fabricante_json:
    #                 aux = Fabricante(obj["Fabricante_id"], 
    #                                  obj["Fabricante_nome"],
    #                                  obj["Fabricante_email"],
    #                                  obj["Fabricante_endereco"],
    #                                  obj["Fabricante_telefone"])
    #                 cls.__fabricantes.append(aux)
    #     except FileNotFoundError:
    #         pass

    # @classmethod
    # def salvar(cls):
    #     with open("fabricantes.json", mode="w") as arquivo:
    #         json.dump(cls.__fabricantes, arquivo, default=vars)