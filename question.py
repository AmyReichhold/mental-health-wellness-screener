"""
Script Name:    question

Description:    The question module that creates a question class

Authors:        Nick Onofrei

Last Edited:    3/1/2022
Last Edit by:   Nick Onofrei
"""

# Question class that instantiates the behavior of a question
class Question():

    # init method to create properties of the question such as
    # The question category, question, and correspong answer array
    def __init__(self, question_caategory, question_message, answer_array):
        self.category = question_caategory
        self.message = question_message
        self.answer_array = answer_array
        self.value = None
        self.button1 = None
        self.button2 = None
        self.button3 = None
    
    # set_value method is made to be able to change the value stored for the question
    # This is used to change the value according to what the user pressed
    def set_value(self, value):
        self.value = value