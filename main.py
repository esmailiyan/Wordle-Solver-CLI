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
        if result == "ggggg":
            self.end = True
        for i in range(5):
            if result[i] == 'g':
                self.fix = self.fix[:i] + suggest[i] + self.fix[i+1:]
            elif result[i] == 'y':
                self.have.append((suggest[i], i))
        for i in range(5):
            if result[i] == 'b' and suggest[i] not in self.fix:
                self.not_have.append(suggest[i])
    def filter(self):
        self.filtered_words = []
        for word in self.words:
            flag = True
            for i in range(5):
                if self.fix[i] != '-' and word[i] != self.fix[i]:
                    flag = False
                    break
            for (x, i) in self.have:
                if x not in word or word[i] == x:
                    flag = False
                    break
            for x in self.not_have:
                if x in word:
                    flag = False
                    break
            if flag:
                self.filtered_words.append(word)
    def suggest(self):
        pass
    def play(self):
        while not self.end:
            self.filter()
            suggestion = self.suggest()
            result = input("Inter Result [y/g/b]: ")
            self.update(suggestion, result)
    def likely(self, word):
        sum = 0
        for a in self.filtered_words:
            for i in range(5):
                if word[i] == a[i]:
                    sum += 1

        temp = ""
        for c in word:
            if c not in temp:
                temp += c
        word = temp

        for a in self.filtered_words:
            for i in range(len(word)):
                if word[i] in a:
                    sum += 1.5
        return sum


if __name__ == "__main__":
    game = Game()
    game.read_words('word.txt')
    game.play()