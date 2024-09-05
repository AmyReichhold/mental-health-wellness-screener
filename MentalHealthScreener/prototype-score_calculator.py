"""
Script Name:    Score Calculator

Description:    The Scorer class for the Mental Health & Wellness
                Screener Program.
                Calculates the SDQ score. The score is broken down into 
                5 scale scores and the total difficulties score.

Authors:        Amy Reichhold

Last Edited:    2/23/2022
Last Edit by:   Amy Reichhold
"""
from typing import Iterable

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

class ScoreCalculator:
    """
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
    """

    def __init__(self):
        pass

    def calculate(self, scores: Iterable):
        # Just to be sure the scores are lower-case.
        scores = [choice.lower() for choice in scores]

        # Initialize the 5 scales scores and total difficulties score 
        # to be zero.
        emotional_problems_score = 0
        conduct_problems_score = 0
        hyperactivity_score = 0
        peer_problems_score = 0
        prosocial_problems_score = 0
        total_difficulties_score = 0

        for i in EMOTIONAL_INDICES:
            choice = scores[i]
            if i in SCORE_2_1_0_INDICES:
                emotional_problems_score += MAPPING_2_1_0[choice]
            else:
                emotional_problems_score += MAPPING_0_1_2[choice]

        for i in CONDUCT_INDICES:
            choice = scores[i]
            if i in SCORE_2_1_0_INDICES:
                conduct_problems_score += MAPPING_2_1_0[choice]
            else:
                conduct_problems_score += MAPPING_0_1_2[choice]

        for i in HYPERACTIVITY_INDICES:
            choice = scores[i]
            if i in SCORE_2_1_0_INDICES:
                hyperactivity_score += MAPPING_2_1_0[choice]
            else:
                hyperactivity_score += MAPPING_0_1_2[choice]

        for i in PEER_INDICES:
            choice = scores[i]
            if i in SCORE_2_1_0_INDICES:
                peer_problems_score += MAPPING_2_1_0[choice]
            else:
                peer_problems_score += MAPPING_0_1_2[choice]

        for i in PROSOCIAL_INDICES:
            choice = scores[i]
            if i in SCORE_2_1_0_INDICES:
                prosocial_problems_score += MAPPING_2_1_0[choice]
            else:
                prosocial_problems_score += MAPPING_0_1_2[choice]

        # The SDQ website says the total difficulties score is the sum of 
        # all scales except the prosocial scale.
        total_difficulties_score = emotional_problems_score \
                                   + conduct_problems_score \
                                   + hyperactivity_score \
                                   + peer_problems_score

        # Using a dictionary to store the scores in order to easily 
        # access specific scores.
        scores = {'emotional': emotional_problems_score, 
                  'conduct': conduct_problems_score,
                  'hyperactivity': hyperactivity_score,
                  'peer': peer_problems_score,
                  'prosocial': prosocial_problems_score,
                  'total': total_difficulties_score}

        return scores
        '''
        return emotional_problems_score, \
               conduct_problems_score, \
               hyperactivity_score, \
               peer_problems_score, \
               prosocial_problems_score, \
               total_difficulties_score
        '''


#test_scores = 'c'*25
test_scores = 'csnnnscssscnnsnscnnscncns'
scorer = ScoreCalculator()
print(scorer.calculate(test_scores))
