class Game:
    def __init__(self):
        self.words = []
        self.filtered_words = []
        self.fix = "-----"
        self.have = []
        self.not_have = []
        self.end = False
        self.turn = 0
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
        value = 0
        suggest = ""
        for word in self.filtered_words:
            if self.likely(word) > value:
                value = self.likely(word)
                suggest = word
        print(f"I',m Suggesting [{suggest}]")
        return suggest
    def play(self):
        while not self.end:
            self.turn += 1
            self.filter()
            suggestion = ""
            
            if self.turn == 1:
                suggestion = self.suggest()
            elif len(self.filtered_words) == 1:
                suggestion = self.suggest()
            elif self.fix.count('-') > 3:
                suggestion = self.suggest()
            else :
                cmd = input("Do you want to use Alternative Strategy? [yes/no]: ")
                if cmd == "yes":
                    suggestion = self.suggest_altern()
                else:
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
    def suggest_altern(self):
        possible_char = []
        for word in self.filtered_words:
            for i in range(5):
                if self.fix[i] == '-':
                    possible_char.append(word[i])
        possible_char = list(set(possible_char))

        altern_words = []
        for word in self.words:
            flag = True
            for (x, i) in self.have:
                if x not in word or word[i] == x or self.fix[word.find(x)] != '-':
                    flag = False
                    break
            for x in self.not_have:
                if x in word:
                    flag = False
                    break
            if flag:
                altern_words.append(word)

        if len(altern_words) == 0:
            return self.suggest()

        value = 0
        suggestion = "-----"
        for word in altern_words:
            score = 0
            for c in possible_char:
                if c in word:
                    score += 1
            if score > value or (score == value and self.likely(suggestion) < self.likely(word)):
                value = score
                suggestion = word

        print(f"I',m Suggesting(Alt) [{suggestion}]")
        return suggestion

if __name__ == "__main__":
    game = Game()
    game.read_words('word.txt')
    game.play()