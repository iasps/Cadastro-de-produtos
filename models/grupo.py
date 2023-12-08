import json

class Grupo:
    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome

    def set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome


class NGrupo:
    __grupos = []
    
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.__grupos:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        cls.__grupos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__grupos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.__grupos:
            if obj.get_id() == id: return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            aux.set_nome(obj.get_nome())
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            cls.__grupos.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__grupos = []
        try:
            with open("grupos.json", mode="r") as arquivo:
                grupos_json = json.load(arquivo)
                for obj in grupos_json:
                    aux = Grupo(obj["_Grupo__id"], 
                        obj["_Grupo__nome"])
                    cls.__grupos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("grupos.json", mode="w") as arquivo:
            json.dump(cls.__grupos, arquivo, default=vars)