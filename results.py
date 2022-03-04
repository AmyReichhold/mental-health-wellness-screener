"""
Script Name:    Results

Description:    The Results class for the Mental Health & Wellness
                Screener Program.
                Calculates the SDQ score. The score is broken down into 
                5 scale scores and the total difficulties score.

Authors:        Amy Reichhold

Last Edited:    2/25/2022
Last Edit by:   Amy Reichhold
"""
from typing import Iterable

from question import Question


# This section will go in the question.py; indices correspond with a 0-based
# index of the questions on the SDQ, reading from top to bottom.
# You might not need the emotional/conduct/etc. indices if you already know
# which category it is, but you can set the score_array for a question if you
# have a question index i like this:
#
#   if i in SCORE_2_1_0_INDICES:
#       question.score_array = list(MAPPING_2_1_0.values())
#   else:
#       question.score_array = list(MAPPING_0_1_2.values())
##############################################################################
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
    """
    A class to sum up all of the scores from the 25 questions from the 
    screener. There are 5 scales: emotional problems, conduct problems,
    hyperactivity, peer problems, and prosocial. Each scale is composed of
    5 questions.

    Attributes
    =========================================================================
    emotional_score
    conduct_score
    hyper_score
    peer_score
    prosocial_score
    total_difficulty_score

    Methods
    =========================================================================
    get_results(questions)
        Goes through every question and sums the question scores to the 
        respective categoriese each question belongs to. The function then 
        sums the first four scales to get the total difficulty score.

    """

    def __init__(self):
        self.emotional_score = 0
        self.conduct_score = 0
        self.hyper_score = 0
        self.peer_score = 0
        self.prosocial_score = 0
        self.total_difficulty_score = 0

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
                raise ValueError('Invalid category.')

        # The SDQ website says the total difficulties score is the sum of 
        # all scales except the prosocial scale.
        self.total_difficulty_score = self.emotional_score \
                                      + self.conduct_score \
                                      + self.hyper_score \
                                      + self.peer_score

        return None

    def create_file(self):
        # a new file called results.txt is created if it doesnt exist. If it exists,
        # it is overwritten to give us a clean results.txt file.
        file = open('results.txt', 'w')
        return file

    def get_result(self, scoretype, ranges):
        for i in range(0, len(ranges)):
            if scoretype in ranges[i]:
                return i


    def store_results(self, questions: Iterable[Question]):

        file = self.create_file()

        name = ['Emotional Score', 'Conduct Score', 'Hyper Score',
                'Peer Score','Prosocial Score', 'Total Difficulty Score']

        score = [self.emotional_score, self.conduct_score, self.hyper_score,
                 self.peer_score, self.prosocial_score, self.total_difficulty_score]

        range1 = [range(0,15), range(15,18), range(18,20), range(20,41)] #total

        range2 = [range(0,5) , range(5,6) , range(6,7), range(7,11)] #emotinal

        range3 = [range(0,4), range(4,5) , range(5, 6) , range(6,10)] #conduct

        range4 = [range(0,6), range(6, 7), range(7, 8), range(8,11)] #hyper

        range5 = [range(0,3), range(3, 4),  range(4, 5), range(5,11)] #peer

        range6 = [range(7, 11), range(6, 7), range(5, 6), range(0, 5)] #prosocial

        array = ['Close to Average', 'Slightly Raised', 'High', 'Very High']

        emo_res = array[self.get_result(self.emotional_score, range2)]

        cond_res = array[self.get_result(self.conduct_score, range3)]

        hyp_res = array[self.get_result(self.hyper_score, range4)]

        peer_res = array[self.get_result(self.peer_score, range5)]

        pros_res = array[self.get_result(self.prosocial_score, range6)]

        tds_res = array[self.get_result(self.total_difficulty_score, range1)]

        comparison = [emo_res,cond_res, hyp_res, peer_res, pros_res, tds_res]

        question = {}
        for qs in questions:
            msg = qs.message
            ans = qs.value_to_plaintext()
            question[msg] = ans


        for i in range(0, len(name)):
            file.write(f'{name[i]}: {score[i]}, Risk Amount: {comparison[i]}\n')
        file.write(f'\n_____________________Questions & Answers_____________________\n')

        for i in question:
            file.write(f'Question: {i}\nAnswer: {question[i]}\n')


        file.close()

#if __name__ == '__main__':
    #a = Results()
    #a.store_results()
