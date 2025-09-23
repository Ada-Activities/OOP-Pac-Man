class Pacman:
    def __init__(self):
        self.name = "Pacman"
        self.color = "Yellow"
        self.lives = 3

    def move(self):
        print(f"{self.name} is moving!")

    def eat(self, target):
        print(f"{self.name} ate {target.name}")
