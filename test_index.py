"""Tests for Student teacher activity"""
import unittest
from index import (
  Group,
  Teacher,
  Student,
  Quiz,
  Question,
  ASSIGN_QUIZ_RESPONSE,
  CALC_ACCUM_SCORE_RESPONSE,
  SOLVE_QUESTION_RESPONSE,
  QUIZ_ASSIGNMENT_DENIED_TEXT
)

class DataTestCase(unittest.TestCase):

    def setUp(self):
        self.group = Group("F1")
        self.teacher1 = Teacher("John", self.group.id)
        self.teacher2 = Teacher("Doe", self.group.id)
        self.student1 = Student("Sarah", self.group.id)
        self.student2 = Student("Geofrey", self.group.id)
        self.question1 = Question(
          "Choose the odd man out?",
          ["Man", "woman", "boy", "girl", "uncle"], ["uncle"])
        self.question2 = Question(
          "Which of the following is a programming language?",
          ["python", "crocodile", "lizard"], ["python"])
        self.quiz = Quiz("BOT", [self.question1,self.question2],self.teacher1.id)
        self.teacher1.assign_quiz(self.quiz.id, self.student1.id)

    def test_assign_quiz(self):
        response = self.teacher1.assign_quiz(self.quiz.id, self.student1.id)
        self.assertEqual(response, ASSIGN_QUIZ_RESPONSE)
        self.assertEqual(self.student1.assigned_quiz, self.quiz)

    def test_teacher_assign_quiz_not_authored(self):
        response = self.teacher2.assign_quiz(self.quiz.id, self.student1.id)
        self.assertEqual(response, QUIZ_ASSIGNMENT_DENIED_TEXT)

    def test_assign_a_non_existent_quiz(self):
        with self.assertRaises(Exception):
            response = self.teacher1.assign_quiz(67867878, self.student2.id)

    def test_solve_question(self):
        response = self.student1.solve_question(self.question1.id, ["uncle"])
        self.assertEqual(response, SOLVE_QUESTION_RESPONSE)
        response = self.student1.solve_question(self.question2.id, ["python"])
        self.assertEqual(response, SOLVE_QUESTION_RESPONSE)

    def test_calc_accum_score(self):
        self.student1.solve_question(self.question1.id, ["uncle"])
        self.student1.solve_question(self.question2.id, ["python"])
        response = self.teacher1.calc_accum_score(self.student1.id)

if __name__ == '__main__':
    unittest.main()