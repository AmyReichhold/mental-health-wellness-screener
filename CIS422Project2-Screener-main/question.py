# Contributors - Nick Onofrei

class Question():

    def __init__(self, question_caategory, question_message, answer_array):
        self.category = question_caategory
        self.message = question_message
        self.answer_array = answer_array
        self.value = None
        self.button1 = None
        self.button2 = None
        self.button3 = None

    def set_value(self, value):
        self.value = value