# Wordle Solver

An interactive command-line helper that suggests strong guesses for the daily [Wordle](https://www.nytimes.com/games/wordle/index.html). Enter the tile feedback from each attempt and it narrows the possible answers, including correct handling of repeated letters.

## Features

- Filters a 2,300-word dictionary from Wordle feedback
- Suggests likely answers or exploratory guesses that reveal more letters
- Validates feedback before applying it
- Uses only the Python standard library

## Quick start

```bash
git clone https://github.com/esmailiyan/WordleSolver.git
cd WordleSolver
python3 main.py
```

No packages need to be installed.

## How to use it

1. Submit the suggested word in Wordle.
2. Enter one character for each tile when prompted:
   - `g` — green: correct letter and position
   - `y` — yellow: correct letter, wrong position
   - `b` — gray: letter is not present in that occurrence
3. Repeat until the solver finds the answer.

For example, gray, yellow, green, gray, gray feedback is entered as `bygbb`.

When several answers remain, choose `y` for the exploratory strategy. It may recommend a word that is not itself a likely answer, prioritizing information from untested letters instead.

## Project layout

```text
.
├── data/words.txt          # Five-letter word dictionary
├── wordle_solver/          # Solver package
│   └── solver.py           # Feedback, filtering, and suggestion logic
└── main.py                 # Command-line entry point
```

## Notes

This is a helper, not an automated Wordle player: submit guesses and feedback on the Wordle site yourself.

## License

Add a license file if you plan to publish or accept contributions.
