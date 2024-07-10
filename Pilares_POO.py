
# ____ Herança ____
# Quando as classes "Cachorro" e "Gato" referenciaram o pai "Animal"

class Animal:
  def __init__(self, nome) -> None:
    self.nome = nome

  def andar(self):
    print(f"O animal {self.nome} andou.")
    return

  def emitir_som(self):
    pass

class Cachorro(Animal):
  def emitir_som(self):
    return "Au Au !"

class Gato(Animal):
  def emitir_som(self):
    return "Miau !"

dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")


# ____ Polimorfismo ____
# Quando o método "emitir_som" foi subrescrevido nas classes "Cachorro" e "Gato"

animais = [dog, cat]

for animal in animais:
  print(f"{animal.nome} faz: {animal.emitir_som()}")

# ____ Encapsulamento ____
# Quando usa o '__' antes do nome do atributo, significa que ele é privado, 
# portanto, apenas poderá ser acessado dentro da classe.

class ContaBancaria:
  def __init__(self, saldo) -> None:
    self.__saldo = saldo # Atributo privado ( tem os 2 underlines )

  def depositar(self, valor):
    if valor > 0:
      self.__saldo += valor

  def sacar(self, valor):
    if valor > 0 and valor <= self.__saldo:
      self.__saldo -= valor

  def consultar_saldo(self):
    return self.__saldo


conta = ContaBancaria(saldo=1000)
print(f"Saldo: {conta.consultar_saldo()}")

conta.depositar(valor=500)
print(f"Saldo: {conta.consultar_saldo()}")

conta.depositar(valor=-500)
print(f"Saldo: {conta.consultar_saldo()}")

conta.sacar(valor=200)
print(f"Saldo: {conta.consultar_saldo()}")

# ____ Abstração ____
# * Classes abstradas não pode ser iniciada
# Essa classe é basicamente uma interface para as classes filhas

from abc import ABC, abstractmethod

class Veiculo(ABC):

  @abstractmethod
  def ligar(self):
    pass

  @abstractmethod
  def desligar(self):
    pass

class Carro(Veiculo):
  def __init__(self) -> None:
    pass

  def ligar(self):
    return "Carro ligado usando a chave"

  def desligar(self):
    return "Carro desligado usando a chave"

meu_carro = Carro()

print(meu_carro.ligar())
print(meu_carro.desligar())