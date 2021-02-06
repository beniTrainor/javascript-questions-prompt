# javascript-questions-prompt

A simple Python script that shows randomly selected questions from [Lydia Hallie's repository of JavaScript questions](https://github.com/lydiahallie/javascript-questions).

![JavaScript questions prompt screencast](screencast.gif)

## Usage

0. Clone [Lydia Hallie's repository of JavaScript questions](https://github.com/lydiahallie/javascript-questions) and rename it to `questions.md`. (Note: I've already included a `questions.md` file with the questions available at the time of writing. For up-to-date questions I suggest replacing that file with the one from Lydia Hallie's.)
1. Run the script: `python3 prompt.py`.
2. Write answers (e.g., `A`) in the prompt below the question and press enter.

The prompt will continue to run until all questions have been shown or an exit keyword (e.g., `q`, `quit`, `x`, `exit`) is entered after showing the answer.

A list of statistics (e.g., questions answered correctly) will show when the prompt stops.
