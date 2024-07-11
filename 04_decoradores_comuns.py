"""
@classmethod

Método da classe permite ser acessado sem a necessidade de intancia-la,
no te que não será possível acessar valores dentro do __init__,
mas consegue acessar atributos de classe.

Ele deve receber a classe como argumento, no caso abaixo será o "cls"
"""

"""
@staticmethod

Bem parecido com o @classmethod, porém não consegue acessar os atributos de classe
"""

class MinhaClasse:
  valor = 10 # Atributo de classe

  def __init__(self, nome) -> None:
    self.nome = nome # Atributo da instância

  # requer uma instância para ser chamado
  def metodo_instancia(self):
    return f"Método de instância chamado para {self.nome}"

  @classmethod
  def metodo_classe(cls):
    return f"Método de classe chamado para valor={cls.valor}"

  @staticmethod
  def metodo_estatico():
    return "Método estático chamado"

obj = MinhaClasse(nome="Classe Exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

class Carro:
  def __init__(self, marca, modelo, ano) -> None:
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  ## Esse método de classe, irá retornar uma instancia nova com uma string recebida.
  @classmethod
  def criar_carro(cls, configuracao):
    marca, modelo, ano = configuracao.split(",")
    return cls(marca, modelo, int(ano))

configuracao1 = "Toyota, Corolla,2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")

class Matematica:

  @staticmethod
  def somar(a, b):
    return a + b

print(Matematica.somar(a=10, b=15))