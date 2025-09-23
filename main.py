from classes.ghost import Ghost
from classes.pacman import Pacman

player_1 = Pacman()
blinky = Ghost("Blinky", "Red")
pinky = Ghost("Pinky", "Pink")
inky = Ghost("Inky", "Cyan")
clyde = Ghost("Clyde", "Orange")

player_1.move()
player_1.eat(clyde)

pinky.touch(player_1)
