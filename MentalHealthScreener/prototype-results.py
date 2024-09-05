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
            if question.category == 'emotional problems':
                self.emotional_score += question.value
            elif question.category == 'conduct problems':
                self.conduct_score += question.value
            elif question.category == 'hyperactivity':
                self.hyper_score += question.value
            elif question.category == 'peer problems':
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

