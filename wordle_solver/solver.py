"""Interactive Wordle-solving logic."""

from __future__ import annotations

from collections import Counter
from pathlib import Path


class WordleSolver:
    """Suggest Wordle guesses based on feedback from previous attempts."""

    WORD_LENGTH = 5
    VALID_FEEDBACK = {"g", "y", "b"}

    def __init__(self, words: list[str]) -> None:
        self.words = words
        self.history: list[tuple[str, str]] = []
        self.solved = False

    @classmethod
    def from_word_list(cls, path: Path) -> "WordleSolver":
        """Build a solver from a newline-separated list of five-letter words."""
        with path.open(encoding="utf-8") as file:
            words = [line.strip().upper() for line in file]
        valid_words = [word for word in words if len(word) == cls.WORD_LENGTH and word.isalpha()]
        if not valid_words:
            raise ValueError(f"No valid {cls.WORD_LENGTH}-letter words found in {path}")
        return cls(valid_words)

    def candidates(self) -> list[str]:
        """Return words consistent with every recorded piece of feedback."""
        return [word for word in self.words if all(
            self.feedback_for(guess, word) == feedback for guess, feedback in self.history
        )]

    @classmethod
    def feedback_for(cls, guess: str, answer: str) -> str:
        """Calculate Wordle-style feedback for a guess against a possible answer."""
        feedback = ["b"] * cls.WORD_LENGTH
        remaining = Counter()
        for index, (guessed, actual) in enumerate(zip(guess, answer)):
            if guessed == actual:
                feedback[index] = "g"
            else:
                remaining[actual] += 1
        for index, guessed in enumerate(guess):
            if feedback[index] == "b" and remaining[guessed] > 0:
                feedback[index] = "y"
                remaining[guessed] -= 1
        return "".join(feedback)

    def suggest(self, explore: bool = False) -> str:
        """Choose the strongest candidate, or an information-gathering guess."""
        candidates = self.candidates()
        if not candidates:
            raise ValueError("No possible words remain. Check the feedback you entered.")
        pool = self.words if explore else candidates
        return max((self.score(word, candidates, explore), word) for word in pool)[1]

    def score(self, word: str, candidates: list[str], explore: bool) -> float:
        """Score positional matches and useful distinct letters."""
        position_score = sum(word[index] == candidate[index] for candidate in candidates for index in range(5))
        letter_score = sum(letter in candidate for candidate in candidates for letter in set(word))
        repeat_penalty = len(word) - len(set(word))
        exploration_bonus = len(set(word)) * len(candidates) if explore else 0
        return position_score + (1.5 * letter_score) + exploration_bonus - repeat_penalty

    def record_feedback(self, guess: str, feedback: str) -> None:
        """Store validated feedback for a suggestion."""
        normalized = feedback.strip().lower()
        if len(normalized) != 5 or not set(normalized) <= self.VALID_FEEDBACK:
            raise ValueError("Feedback must contain exactly five letters: g, y, or b.")
        self.history.append((guess, normalized))
        self.solved = normalized == "ggggg"

    def play(self) -> None:
        """Run the interactive terminal experience."""
        print("Wordle Solver — enter g (green), y (yellow), or b (gray) for each tile.")
        turn = 0
        while not self.solved:
            turn += 1
            candidates = self.candidates()
            if not candidates:
                print("No candidates remain. Please restart and check your feedback.")
                return
            if len(candidates) <= 10:
                print(f"Candidates: {', '.join(candidates)}")
            explore = len(candidates) > 1 and input("Use exploratory strategy? [y/N]: ").strip().lower() == "y"
            guess = self.suggest(explore=explore)
            print(f"Turn {turn}: {'exploratory guess' if explore else 'suggestion'}: {guess}")
            while True:
                try:
                    self.record_feedback(guess, input("Feedback [g/y/b]: "))
                    break
                except ValueError as error:
                    print(error)
        print(f"Solved in {turn} turn{'s' if turn != 1 else ''}!")
