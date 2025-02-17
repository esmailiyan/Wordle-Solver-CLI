class Game:
    def __init__(self):
        self.words = []
        self.filtered_words = []
        self.fix = "-----"
        self.have = []
        self.not_have = []
        self.end = False
    def read_words(self, database):
        with open(database, 'r') as file:
            lines = file.readlines()
        for line in lines:
            self.words.append(line.strip())
    def update(self, suggest, result):
        for i in range(5):
            if result[i] == 'g':
                self.fix = self.fix[:i] + suggest[i] + self.fix[i+1:]
            elif result[i] == 'y':
                self.have.append((suggest[i], i))
        for i in range(5):
            if result[i] == 'b' and suggest[i] not in self.fix:
                self.not_have.append(suggest[i])
        print(self.fix)
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