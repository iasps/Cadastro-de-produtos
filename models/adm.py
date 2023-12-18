import json
from models.crud import CRUD

class Adm:
  def __init__(self, id, nome, email, senha):
    self.__id = id
    self.__nome = nome
    self.__email = email
    self.__senha = senha

  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_email(self): return self.__email
  def get_senha(self): return self.__senha

  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome = nome
  def set_email(self, email): self.__email = email
  def set_senha(self, senha): self.__senha = senha

class NAdm(CRUD):
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("adms.json", mode="r") as arquivo:
        adms_json = json.load(arquivo)
        for obj in adms_json:
          aux = Adm(obj["_Adm__id"], 
                        obj["_Adm__nome"], 
                        obj["_Adm__email"],
                        obj["_Adm__senha"])
          cls.objetos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("adms.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default=vars)











  # __adms = []  # lista de adms inicia vazia

  # @classmethod
  # def inserir(cls, obj):
  #   cls.abrir()
  #   id = 0  # encontrar o maior id já usado
  #   for aux in cls.__adms:
  #     if aux.get_id() > id: id = aux.get_id()
  #   obj.set_id(id + 1)
  #   cls.__adms.append(obj)  # insere um adm (obj) na lista
  #   cls.salvar()

  # @classmethod
  # def listar(cls):
  #   cls.abrir()
  #   return cls.__adms  # retorna a lista de adms

  # @classmethod
  # def listar_id(cls, id):
  #   cls.abrir()
  #   for obj in cls.__adms:
  #     if obj.get_id() == id: return obj
  #   return None

  # @classmethod
  # def atualizar(cls, obj):
  #   cls.abrir()
  #   aux = cls.listar_id(obj.get_id())
  #   if aux is not None:
  #     aux.set_nome(obj.get_nome())
  #     aux.set_email(obj.get_email())
  #     aux.set_senha(obj.get_senha())
  #     cls.salvar()

  # @classmethod
  # def excluir(cls, obj):
  #   cls.abrir()
  #   aux = cls.listar_id(obj.get_id())
  #   if aux is not None:
  #     cls.__adms.remove(aux)
  #     cls.salvar()

  # @classmethod
  # def abrir(cls):
  #   cls.__adms = []
  #   try:
  #     with open("adms.json", mode="r") as arquivo:
  #       adms_json = json.load(arquivo)
  #       for obj in adms_json:
  #         aux = Adm(obj["_Adm__id"], 
  #                       obj["_Adm__nome"], 
  #                       obj["_Adm__email"],
  #                       obj["_Adm__senha"])
  #         cls.__adms.append(aux)
  #   except FileNotFoundError:
  #     pass

  # @classmethod
  # def salvar(cls):
  #   with open("adms.json", mode="w") as arquivo:
  #     json.dump(cls.__adms, arquivo, default=vars)