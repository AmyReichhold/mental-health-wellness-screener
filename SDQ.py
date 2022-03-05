"""
Script Name:    SDQ

Description:    The SDQ module creates and keeps track of all questions, and
                sends the questions to the result module

Authors:        Quinn Fetrow, Luke Vandecasteele

Last Edited:    03/01/2022
Last Edit by:   Luke Vandecasteele

Credits: 
"""
from results import *
from question import Question
import os.path


class SDQ:

    def __init__(self):
        # Generates questions on startup
        self.questions = self.generate_survey()
        self.results = Results()

    def generate_survey(self):
        # Reads and parses question information from local questionnaire.txt
        # file
        if (not os.path.exists('questionnaire.txt')):
            print("File not found")
            return
        qfile = open('questionnaire.txt', 'r')
        lines = qfile.readlines()
        questions = []
        for line in lines:
            # Each line contains semicolons that separate the question
            # information
            line_parse = line.split(';')
            # Ensure no out of range/user errors
            if len(line_parse) == 3:
                message = line_parse[0]
                category = line_parse[1].strip()
                # The third parameter in the input file is either
                # "normal_order" or "reversed_order"
                # these correspond to how the question will be scored
                if line_parse[2].strip() == "normal_order":
                    answer_array = [0, 1, 2]
                else:
                    answer_array = [2, 1, 0]
                questions.append(Question(category, message, answer_array))
        if len(questions) != 25:
            print("Data corrupted/Changed")
        return questions

    def submit(self):
        # Calculate and store results, called from Survey Interface when
        # answers are submitted
        for question in self.questions:
            question.set_value()
        self.results.get_results(self.questions)
        self.results.store_results(self.questions)
