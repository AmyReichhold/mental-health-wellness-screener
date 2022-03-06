"""
Script Name:    question

Description:    The question module that creates a question class

Authors:        Nick Onofrei, Quinn Fetrow

Last Edited:    3/1/2022
Last Edit by:   Quinn Fetrow
"""

import tkinter


# Question class that instantiates the behavior of a question
class Question():

    # init method to create properties of the question such as
    # The question category, question, and correspong answer array
    def __init__(self, question_caategory, question_message, answer_array):
        self.category = question_caategory
        self.message = question_message
        self.answer_array = answer_array
        self.answerstate = None  # This will be assigned a tkinter value
        # mapped to the radio buttons
        self.value = None

    # set_value method is made to be able to change the value stored for the
    # question
    # This is used to change the value according to what the user pressed
    def set_value(self):
        self.value = self.answer_array[self.answerstate.get()]

    def set_answerstate(self, value):
        self.answerstate = value

    def value_to_plaintext(self) -> str:
        # Returns a plaintext representation of the answer value, used by
        # Results module
        # convert value back to initial value through array
        answervalue = self.answer_array[self.value]
        plaintext = ["Not True", "Somewhat True", "Certainly True"]
        return plaintext[answervalue]
