import player

class AIPlayer(player.Player):
    def move(self):
        # We'll first look for a good movement
        self.findBestMove()
        # Then call the base class method to act
        Player.move(self, dir)

    def findBestMove(self):
        pass