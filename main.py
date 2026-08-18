"""Command-line entry point for the Wordle Solver."""

from pathlib import Path

from wordle_solver import WordleSolver


def main() -> None:
    word_list = Path(__file__).parent / "data" / "words.txt"
    WordleSolver.from_word_list(word_list).play()


if __name__ == "__main__":
    main()
