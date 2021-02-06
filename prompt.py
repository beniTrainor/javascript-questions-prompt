"""
Shows the list of [questions made by Lydia Hallie](https://github.com/lydiahallie/javascript-questions).
"""

import os
import re
import random

def main():

    filename = "./questions.md"
    if not os.path.exists(filename):
        print("File '{}' does not exist.".format(filename))
        exit(1)

    questions = parse_questions_file(filename)

    clear_term()

    total_answered = 0
    total_correct = 0

    while len(questions) > 0:
        index = random.randint(0, len(questions) - 1)
        question = questions.pop(index)

        for line in question["qlines"]:
            print(line)

        answer = ""
        while answer == "":
            answer = input("Your answer: ").upper()
        total_answered += 1

        print("")
        for line in question["alines"]:
            if line.startswith("#### Answer"):
                print(line.replace("Answer", "Correct answer"))
            else:
                print(line)

        if answer == question["answer"]:
            total_correct += 1
            print("\033[92m✓ Correct!\033[00m ({} out of {})\n"
                    .format(total_correct, total_answered))
        else:
            print("\033[91m✗ Incorrect\033[00m. Read the explanation above" +
                "to learn more about it.\n")

        kbi = input("Continue (<ENTER>/n)? ")
        if kbi.lower() == "n":
            break

        clear_term()

    print("\n---\n")
    print("Stats:")
    print("- Total answered:  ", total_answered)
    print("- Total correct:   ", total_correct)
    print("- Percent correct: ",
        round((total_correct / total_answered) * 100, 2))


def parse_questions_file(filename):

    # Store the questions in a list of dictionaries with the following
    # structure:
    # qlines: [] # answer lines
    # alines: [] # question lines
    # answer: "" # answer (e.g., "A")
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
                questions.append({"qlines": [], "alines": []})
                questions[-1]["qlines"].append(line)
                is_question = True
                is_answer = False

            elif line.startswith("#### Answer"):
                questions[-1]["alines"].append(line)
                questions[-1]["answer"] = line.split(" ")[-1]
                is_question = False
                is_answer = True

            elif is_question:
                questions[-1]["qlines"].append(line)
            elif is_answer:
                questions[-1]["alines"].append(line)

    return questions


def ignore_line(line):

    omit_patterns = [
        "^\<details\>",
        "^\<\/details\>",
        "^\<p\>",
        "^\<\/p\>",
        "^---"
    ]

    for pattern in omit_patterns:
        if re.match(pattern, line):
            return True

    return False


def clear_term():
    os.system("clear")

if __name__ == "__main__":
    main()
