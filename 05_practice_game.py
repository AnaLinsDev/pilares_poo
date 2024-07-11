"""
Classes: 
- Character: parent
- Hero: user
- Enemy: user enemy
"""

import random

class Character:
  def __init__(self, name, life, level):
    self.__name = name
    self.__life = life
    self.__level = level

  def get_name(self):
    return self.__name

  def get_life(self):
    return self.__life

  def get_level(self):
    return self.__level
  
  def receive_attack(self, damage):
    self.__life -= damage

    if self.__life < 0:
      self.__life = 0
  
  def attack(self, target):
    damage = self.__level * random.randint(self.get_level() * 2, self.get_level() * 4)
    target.receive_attack(damage)

    print(f"{self.get_name()} attacked {target.get_name()} and dealt {damage} damage!")

  def special_attack(self, target):
    damage = self.__level * random.randint(self.get_level() * 5, self.get_level() * 8)
    target.receive_attack(damage)

    print(f"{self.get_name()} used special attack on {target.get_name()} and dealt {damage} damage!")
  
  def show_details(self):
    return f"Name: {self.get_name()}\nLife: {self.get_life()}\nLevel: {self.get_level()}"

class Hero(Character):
  def __init__(self, name, life, level, skill):
    super().__init__(name, life, level)
    self.__skill = skill

  def get_skill(self):
    return self.__skill

  def show_details(self):
    return f"{super().show_details()}\nSkill: {self.get_skill()}\n"

class Enemy(Character):
  def __init__(self, name, life, level, type):
    super().__init__(name, life, level) # Must init so you can access the parents method.
    self.__type = type

  def get_type(self):
    return self.__type

  def show_details(self):
    return f"{super().show_details()}\nType: {self.get_type()}\n"


class Game:
  """ Game orchestrator class """

  def __init__(self) -> None:
    self.hero = Hero(name="Superman", life=100, level=5, skill="Super Força")
    self.enemy = Enemy(name="Lex Luthor", life=100, level=5, type="Intelligence")

  def initiate_match(self):
    """ Manage the battle in turns """
    print("Starting battle!")
    is_hero_turn = True

    while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
      
      print("\n\n__________________________________")

      print("\nCharacter Details:")
      print(self.hero.show_details())
      print(self.enemy.show_details())

      if is_hero_turn: 
        print("[HERO TURN]")

        choice = input("Choice (1 - Normal Attack, 2 - Special Attack): ")
      else:
        print("[ENEMY TURN]")

        choice = input("Choice (1 - Normal Attack): ")


      if choice == '1':
        if is_hero_turn: 
          self.hero.attack(self.enemy)
        else:
          self.enemy.attack(self.hero)
        print ("Normal Attack !")
      elif choice == '2':
        self.hero.special_attack(self.enemy)
      else:
        print ("Not a valid choice, Try Again.")
    
      is_hero_turn = not is_hero_turn
    
    if self.hero.get_life() > 0:
      print ("Hero Won !")
    else:
      print ("Enemy Won !")

# Create game instance and start battle
my_game = Game()
my_game.initiate_match()
