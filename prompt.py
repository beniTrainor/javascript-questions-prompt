"""
Shows the list of [questions made by Lydia Hallie](https://github.com/lydiahallie/javascript-questions).
"""

import os
import re
import random

def main():

    questions = parse_questions()

    clear_term()

    questions_answered = 0
    questions_answered_correctly = 0

    while len(questions) > 0:
        index = random.randint(0, len(questions) - 1)
        question = questions.pop(index)

        for line in question["qlines"]:
            print(line)

        answer = input("Answer: ").upper()
        if answer == question["answer"]:
            questions_answered_correctly += 1
        questions_answered += 1

        print("")
        for line in question["alines"]:
            print(line)

        if answer == question["answer"]:
            print("Correct! ✓ \n")

        kbi = input()
        if kbi.lower() in ["exit", "x", "quit", "q"]:
            break

        clear_term()

    print("\n---\n")
    print("Stats:")
    print("- Answered: ", questions_answered)
    print("- Correct:", questions_answered_correctly)
    print("- Percent: ", 
        round((questions_answered_correctly / questions_answered) * 100, 2))


def parse_questions():

    # Store the questions in a list of dictionaries with the following
    # structure:
    # qlines: [] # answer lines
    # alines: [] # question lines
    # answer: "" # answer (e.g., "A")
    questions = []

    # Track whether the lines refer to a question/answer statement
    is_question = False
    is_answer = False

    filename = "./questions.md"
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
