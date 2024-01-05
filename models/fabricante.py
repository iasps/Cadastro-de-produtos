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

    def __eq__(self, x):
        if self.__id == x.__id and self.__nome == x.__nome and self.__email == x.__email and self.__endereco == x.__endereco and self.__telefone == x.__telefone:
            return True
        return False

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__endereco} - {self.__telefone}"

    def to_json(self):
        return {
            'Id' : self.__id,
            'Nome' : self.__nome,
            'Email' : self.__email,
            'Endereco' : self.__endereco,
            'Telefone' : self.__telefone}

class NFabricante(CRUD):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("fabricantes.json", mode="r") as arquivo:
                fabricante_json = json.load(arquivo)
                for obj in fabricante_json:
                    aux = Fabricante(obj["_Fabricante__id"], 
                                     obj["_Fabricante__nome"],
                                     obj["_Fabricante__email"],
                                     obj["_Fabricante__endereco"],
                                     obj["_Fabricante__telefone"])
                    cls.objetos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("fabricantes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)



