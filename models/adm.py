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

  def __eq__(self, x):
    if self.__id == x.__id and self.__nome == x.__nome and self.__email == x.__email and self.__senha == x.__senha:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__email} - {self.__senha}"

  def to_json(self):
    return {
      'Id' : self.__id,
      'Nome' : self.__nome,
      'E-mail' : self.__email,
      'Senha' : self.__senha}

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




