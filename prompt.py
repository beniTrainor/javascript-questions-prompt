"""
Shows the list of [questions made by Lydia Hallie](https://github.com/lydiahallie/javascript-questions).
"""

import os
import re
import random
from datetime import datetime


def main():

    filename = "./questions.md"
    if not os.path.exists(filename):
        print("File '{}' does not exist.".format(filename))
        exit(1)

    clear_terminal_screen()

    total_answered = 0
    total_correct = 0
    questions = parse_questions_file(filename)

    while len(questions) > 0:
        index = random.randint(0, len(questions) - 1)
        question = questions.pop(index)

        # Remove empty lines from the end
        while question["question_lines"][-1] == "":
            question["question_lines"].pop()

        for line in question["question_lines"]:
            print(line)

        options = question["options"]
        option_letters = list(options.keys())
        random.shuffle(option_letters)
        print("")
        for letter in option_letters:
            print("- {}: {}".format(letter, options[letter]))
        print("")

        answer = ""
        while answer == "":
            answer = input("Your answer: ").upper()
        total_answered += 1

        print("")
        for line in question["answer_lines"]:
            if line.startswith("#### Answer"):
                print(line.replace("Answer", "Correct answer"))
            else:
                print(line)

        if answer[0] == question["answer"]:
            total_correct += 1
            print("\033[92m✓ Correct!\033[00m ({} out of {})\n"
                    .format(total_correct, total_answered))
        else:
            print("\033[91m✗ Incorrect\033[00m. Read the explanation above " +
                "to learn more about it.\n")
            write_question_to_file(question)

        kbi = input("Continue (<ENTER>/n)? ")
        if kbi.lower() == "n":
            break

        clear_terminal_screen()

    print("\n---\n")
    print("Stats:")
    print("- Total answered:  ", total_answered)
    print("- Total correct:   ", total_correct)
    print("- Percent correct: ",
        round((total_correct / total_answered) * 100, 2))


def parse_questions_file(filename):
    """
    Parse a file with questions into a list of dictionaries holding the
    question data.

    The file should have the following format:
    - It may include a header of miscellaneous content.
    - Each question should be started with a *question statement* denoted by
      a heading level 6 in Markdown ('######') and ended when a new question
      statement is encountered.
    - An answer statement may be encountered while parsing the question but
      at this time it's not strictly necessary. (TODO: make this a requirement)
      The answer statement is denoted by a heading level 4 in Markdown ('####').
    """

    questions = []

    # Track whether the lines refer to a question/answer statement
    is_question = False
    is_answer = False

    with open(filename) as ifile:

        for line in ifile.readlines():
            line = line.strip("\n")

            if ignore_line(line):
                continue

            if line.startswith("######"):
                questions.append({"question_lines": [], "answer_lines": []})
                questions[-1]["question_lines"].append(line)
                questions[-1]["options"] = {}
                is_question = True
                is_answer = False

            elif line.startswith("#### Answer"):
                questions[-1]["answer_lines"].append(line)
                questions[-1]["answer"] = line.split(" ")[-1]
                is_question = False
                is_answer = True

            elif is_question:
                if re.match("- [A-Z]:", line):
                    letter, text, *rest = line.split(":")
                    letter = letter[2:]
                    text = ":".join([text[1:], *rest])
                    questions[-1]["options"][letter] = text
                else:
                    questions[-1]["question_lines"].append(line)
            elif is_answer:
                questions[-1]["answer_lines"].append(line)

    return questions


def ignore_line(line):

    omit_patterns = [
        "^<details>",
        "^</details>",
        "^<p>",
        "^</p>",
        "^---"
    ]

    for pattern in omit_patterns:
        if re.match(pattern, line):
            return True

    return False


def write_question_to_file(question):
    """
    Writes question data to a file in exactly the same structure as the
    original document from which they came, except for the HTML tags.
    """

    current_date = datetime.now().strftime("%Y-%m-%d")
    output_filename = "./wrong-answers-{}.md".format(current_date)

    with open(output_filename, "a") as f:
        for line in question["question_lines"]:
            f.write(line + "\n")
        f.write("\n")
        options = question["options"]
        for letter in sorted(options.keys()):
            f.write("- {}: {}\n".format(letter, options[letter]))
        f.write("\n")
        for line in question["answer_lines"]:
            f.write(line + "\n")


def clear_terminal_screen():
    os.system("clear")

if __name__ == "__main__":
    main()
