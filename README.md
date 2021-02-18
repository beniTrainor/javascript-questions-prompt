# javascript-questions-prompt

A CLI prompt that provides an interactive way to answer JavaScript questions from [Lydia Hallie's repository of JavaScript questions](https://github.com/lydiahallie/javascript-questions) (or similarly formatted file).

* All questions are randomly shuffled and shown only once.
* The prompt can be stopped at any time by typing `n` after a question is answered.
* Wrong questions are written to a file to keep track of them.
* Stats are shown as you answer questions correctly and when the prompt stops.

![JavaScript questions prompt screencast](screencast.gif)

## Usage

0. Download [Lydia Hallie's JavaScript questions page](https://github.com/lydiahallie/javascript-questions):

`wget https://raw.githubusercontent.com/lydiahallie/javascript-questions/master/README.md -O questions.md`

1. Run the script: `python3 prompt.py`.
2. Write answers (e.g., `a`|`A`) in the prompt below the question and press enter.
