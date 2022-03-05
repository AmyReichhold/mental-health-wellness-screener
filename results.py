"""
Script Name:    Results

Description:    The Results class for the Mental Health & Wellness
                Screener Program.
                Calculates the SDQ score. The score is broken down into 
                5 scale scores and the total difficulties score.

Authors:        Amy Reichhold, Michael Gao, Luke Vandecasteele

Last Edited:    3/4/2022
Last Edit by:   Luke Vandecasteele
"""
from typing import Iterable

from question import Question


# There scoring process is composed of 5 scales (listed below).
# The indices below are the questions that belong to each scale. 
EMOTIONAL_INDICES = (2, 8, 12, 15, 23)
CONDUCT_INDICES = (4, 6, 11, 17, 21)
HYPERACTIVITY_INDICES = (1, 9, 14, 20, 24)
PEER_INDICES = (5, 10, 13, 18, 22)
PROSOCIAL_INDICES = (0, 3, 8, 16, 19)

# This keeps track of the 5 questions that are scored differently
SCORE_2_1_0_INDICES = (6, 20, 24, 10, 13)

# The scoring process varies with certain questions.
# 20/25 questions use the 0_1_2 scoring methode.
MAPPING_0_1_2 = {'n': 0, 's': 1, 'c': 2}

# 5/25 questions use the 2_1_0 scoring method. 
# (Which 5 is shown in SCORE_2_1_0_INDICES) 
MAPPING_2_1_0 = {'n': 2, 's': 1, 'c': 0}


##############################################################################

class Results:

    # stores overall scores for each section of the SDQ
    def __init__(self):
        self.emotional_score = 0
        self.conduct_score = 0
        self.hyper_score = 0
        self.peer_score = 0
        self.prosocial_score = 0
        self.total_difficulty_score = 0

    # checks which category each question belongs too and increments the
    # respective category based upon the users answer
    def get_results(self, questions: Iterable[Question]):

        for question in questions:
            if question.category == 'emotional':
                self.emotional_score += question.value
            elif question.category == 'conduct':
                self.conduct_score += question.value
            elif question.category == 'hyperactivity':
                self.hyper_score += question.value
            elif question.category == 'peer':
                self.peer_score += question.value
            elif question.category == 'prosocial':
                self.prosocial_score += question.value
            else:
                # all questions must belong to one of the categories
                raise ValueError('Invalid category.')

        # The SDQ website says the total difficulties score is the sum of 
        # all scales except the prosocial scale.
        self.total_difficulty_score = self.emotional_score \
                                      + self.conduct_score \
                                      + self.hyper_score \
                                      + self.peer_score

        return None

    # a new file called results.txt is created if it doesn't exist. If it
    # exists, it is overwritten to give us a clean results.txt file.
    def create_file(self):
        file = open('results.txt', 'w')
        return file

    # returns the range that a certain categories score falls into
    def get_result(self, scoretype, ranges):
        for i in range(0, len(ranges)):
            if scoretype in ranges[i]:
                return i

    # generates the text versions of the results that are printed to the
    # output file for the user to view
    def store_results(self, questions: Iterable[Question]):

        # create/replace result file
        file = self.create_file()

        # titles for each section and the corresponding scores
        name = ['Emotional Score', 'Conduct Score', 'Hyper Score',
                'Peer Score', 'Prosocial Score', 'Total Difficulty Score']
        score = [self.emotional_score, self.conduct_score, self.hyper_score,
                 self.peer_score, self.prosocial_score,
                 self.total_difficulty_score]

        # labels for the different risk ranges
        array = ['Close to Average', 'Slightly Raised', 'High', 'Very High']

        # 4 risk ranges for each of the 6 different categories
        range1 = [range(0, 15), range(15, 18), range(18, 20),
                  range(20, 41)]  # total
        range2 = [range(0, 5), range(5, 6), range(6, 7),
                  range(7, 11)]  # emotional
        range3 = [range(0, 4), range(4, 5), range(5, 6),
                  range(6, 10)]  # conduct
        range4 = [range(0, 6), range(6, 7), range(7, 8), range(8, 11)]  # hyper
        range5 = [range(0, 3), range(3, 4), range(4, 5), range(5, 11)]  # peer
        range6 = [range(7, 11), range(6, 7), range(5, 6),
                  range(0, 5)]  # prosocial

        # for each category, find the amount of risk based off the score in
        # the category, and the ranges for that category
        emo_res = array[self.get_result(self.emotional_score, range2)]
        cond_res = array[self.get_result(self.conduct_score, range3)]
        hyp_res = array[self.get_result(self.hyper_score, range4)]
        peer_res = array[self.get_result(self.peer_score, range5)]
        pros_res = array[self.get_result(self.prosocial_score, range6)]
        tds_res = array[self.get_result(self.total_difficulty_score, range1)]

        # store the amount of risk in a list for easier access
        comparison = [emo_res, cond_res, hyp_res, peer_res, pros_res, tds_res]

        # store the questions:answers as key:value pairs
        # these will also be printed to the result file to remind the user of
        # their answers
        question = {}
        for qs in questions:
            msg = qs.message
            ans = qs.value_to_plaintext()
            question[msg] = ans

        # first print the users risk for each of the sections
        for i in range(0, len(name)):
            file.write(f'{name[i]}: {score[i]}, Risk Amount: {comparison[i]}\n')

        # print questions and the users answers
        file.write(
            f'\n_____________________Questions & '
            f'Answers_____________________\n')
        for i in question:
            file.write(f'Question: {i}\nAnswer: {question[i]}\n')

        # close the result file
        file.close()
