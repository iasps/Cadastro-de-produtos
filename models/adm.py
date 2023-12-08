import json

class Adm:
    def __init__(self, id, email, senha):
        self.__id = id
        self.__email = email
        self.__senha = senha

    def get_id(self): return self.__id
    def get_email(self): return self.__email
    def get_senha(self): return self.__senha

    def set_id(self, id): self.__id
    def set_email(self, email): self.__email
    def set_senha(self, senha): self.__senha

class NAdm:
    __adms = []
    
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.__adms:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        cls.__adms.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__adms

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.__adms:
            if obj.get_id() == id: return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            aux.set_email(obj.get_email())
            aux.set_senha(obj.get_senha())
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            cls.__adms.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__adms = []
        try:
            with open("adms.json", mode="r") as arquivo:
                adms_json = json.load(arquivo)
                for obj in adms_json:
                    aux = Adm(obj["_Adm__id"],
                              obj["_Adm__email"],
                              obj["_Adm__senha"])
                    cls.__adms.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("adms.json", mode="w") as arquivo:
            json.dump(cls.__adms, arquivo, default=vars)