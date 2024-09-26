class Pacman:
  def __init__(self):
    self.name = 'pacman'
    self.color = 'yellow'
    self.lives = 3
  
  
  def move(self):
    print(f'{self.name} is moving!')
  
  
  def eat(self, victim):
    print(f'{self.name} ate a {victim.name}')