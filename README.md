# javascript-questions-prompt

A simple Python script that shows randomly selected questions from [Lydia Hallie's repository of JavaScript questions](https://github.com/lydiahallie/javascript-questions).

![JavaScript questions prompt screencast](screencast.gif)

## Usage

0. Download [Lydia Hallie's JavaScript questions page](https://github.com/lydiahallie/javascript-questions):

`wget https://raw.githubusercontent.com/lydiahallie/javascript-questions/master/README.md -O questions.md`

1. Run the script: `python3 prompt.py`.
2. Write answers (e.g., `a`|`A`) in the prompt below the question and press enter.

The prompt will continue to run until all questions have been shown or `n` is entered after showing the answer.

A list of statistics (e.g., questions answered correctly) will show when the prompt stops.
