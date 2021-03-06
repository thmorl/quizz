# -*- coding: utf-8 -*-
"""Quizz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d0y2bOEu67r9HwTZ-VOn_oV7Pe_gy6ci
"""



class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "Capital de la Chine?\n(a) Pékin\n(b)Tokyo",
     "Capital France?\n(a) Paris\n(b)Lyon",
     "Capital de la Belgique?\n(a) Bruxelle\n(b)Berlin"
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[2], "a"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))

run_quiz(questions)