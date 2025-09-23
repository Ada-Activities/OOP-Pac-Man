class Ghost:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.is_transformed = False

    def move(self):
        print(f"{self.name} is moving!")

    def touch(self, player):
        # could use player to tell the player to lose a life
        print("GAME OVER")
