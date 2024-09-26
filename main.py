from classes.ghost import Ghost
from classes.pacman import Pacman

pacman_1 = Pacman()
pinky = Ghost("Pinky", "Pink")
blinky = Ghost("Blinky", "Red")
inky = Ghost("Inky", "Cyan")
clyde = Ghost("Clyde", "Orange")

pacman_1.move()
pacman_1.eat(clyde)
