from ast import Return
import json
from models.crud import CRUD


class Grupo:
    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome

    def set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome

    def __eq__(self, x):
        if self.__id == x.__id and self.__nome == x.__nome:
            return True
        return False

    def __str__(self):
        return f"{self.__id} - {self.__nome}"

    def to_json(self):
        return {
            'Id' : self.__id, 
            'Nome' : self.__nome}


class NGrupo(CRUD):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("grupos.json", mode="r") as arquivo:
                grupos_json = json.load(arquivo)
                for obj in grupos_json:
                    aux = Grupo(obj["_Grupo__id"], 
                                obj["_Grupo__nome"])
                    cls.objetos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("grupos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)
