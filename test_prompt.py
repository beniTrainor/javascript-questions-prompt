import unittest
import prompt

class TestPrompt(unittest.TestCase):

    def test_parse_questions_file(self):
        """
        Check whether the file is parsed correctly.
        """
        questions = prompt.parse_questions_file("./questions.md")
        self.assertIsInstance(questions, list)

        if len(questions) == 0:
            raise Exception("Empty questions file.")

        question = questions[0]
        self.assertIsInstance(question, dict)
        self.assertIn("question_lines", question)
        self.assertIsInstance(question["question_lines"], list)
        self.assertIn("answer_lines", question)
        self.assertIsInstance(question["answer_lines"], list)
        self.assertIn("options", question)
        self.assertIsInstance(question["options"], dict)
        self.assertIn("answer", question)
        self.assertIsInstance(question["answer"], str)

    def test_ignore_line(self):
        """
        Check whether a given string should be ignored.
        """
        self.assertTrue(prompt.ignore_line("<details>"))
        self.assertTrue(prompt.ignore_line("</details>"))
        self.assertTrue(prompt.ignore_line("<p>"))
        self.assertTrue(prompt.ignore_line("</p>"))
        self.assertTrue(prompt.ignore_line("---"))


if __name__ == "__main__":
    unittest.main()
