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
        with open(database, 'r') as file:
            lines = file.readlines()
        for line in lines:
            self.words.append(line.strip())

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
    game.read_words('word.txt')
    game.play()