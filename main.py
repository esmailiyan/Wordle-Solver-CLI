class Game:
    def __init__(self):
        self.words = []
        self.filtered_words = []
        self.fixed = "-----"
        self.not_fixed = [[],[],[],[],[]]
        self.have = []
        self.not_have = []
        self.end = False
    def read_words(self, database):
        pass 
    def update(self, result):
        pass
    def filter(self):
        pass
    def suggest(self):
        pass
    def play(self):
        pass

if __name__ == "__main__":
    game = Game()
    game.play()