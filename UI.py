"""
Script Name:    UI

Description:    The user interface for administering the screener and
                displaying the results

Authors:        Luke Vandecasteele

Last Edited:    2/27/2022
Last Edit by:   Luke Vandecasteele
"""


from tkinter import *

# Place Holder questions
questions = []
for i in range(100):
    if i > 0:
        questions.append(f"Question {i}")


#Global Variables
PROJECT = "Mental Health and Wellness Personal Screener: SDQ"
TITLE = "Strengths and Difficulties Questionnaire (SDQ)"
INSTRUCTIONS = "\nFor each item, please mark the box for Not True, Somewhat True " \
               "or Certainly True. It would help us if you answered all items " \
               "as best you can even if you are not absolutely certain . Please " \
               "give your answers on the basis of how things have been for you " \
               "over the last six months.\n"
INSTRUCTIONS2 = "These instructions will be provided on the next page as well for" \
                " your convenience.\n"
WARNING = "This screener is only for personal use. Do NOT share the results" \
          ". Only complete this screener by yourself or with the " \
          "help of a psychologist. Mental health is very personal and should " \
          "be respected.\n"
SOURCES = "For more information on the SDQ please visit: https://sdqinfo.org.\n" \
          "To learn more about this project please visit the documentation " \
          "listed on the github repo at https://github.com/lvandeca/CIS422Project2-Screener"


class UI():

    def __init__(self):
        self.start = None
        self.survey = None
        self.question = questions   # this will be replaced with real question objects
        self.init_interface()

    def init_interface(self):
        self.start = Tk()
        self.start.title(PROJECT)
        self.start.geometry("1000x500+100+100")
        self.start.configure(bg="turquoise")
        title = Label(self.start, text=TITLE, font=("Times New Roman", 32, "bold"),
                      bg="turquoise", fg='black').pack()
        instructions = Label(self.start, text=INSTRUCTIONS, wraplength=800,
                             font=("Times New Roman", 20), justify=LEFT,
                             bg="turquoise", fg='black').pack()
        instructions2 = Label(self.start, text=INSTRUCTIONS2, wraplength=800,
                              font=("Times New Roman", 20), justify=LEFT,
                              bg="turquoise", fg='black').pack()
        warning = Label(self.start, text=WARNING, wraplength=800,
                        font=("Times New Roman", 20), justify=LEFT,
                        bg="turquoise", fg='black').pack()
        begin = Button(self.start, text="Begin Screener", font=("Times New Roman", 20),
                       command=lambda:[self.start.destroy(), self.display_survey()],
                       cursor="plus", padx=5, pady=10).pack()
        sources = Label(self.start, text=SOURCES, wraplength=800,
                        font=("Times New Roman", 12), justify=CENTER,
                        bg="turquoise", fg='black').pack(side=BOTTOM)
        self.start.mainloop()

    def display_survey(self):
        self.survey = Tk()
        self.survey.title(PROJECT)
        width1 = self.survey.winfo_screenwidth()
        height = self.survey.winfo_screenheight()
        width = width1 - (width1 / 3)
        self.survey.geometry("%dx%d+%d+0" % (width, height, width1/6))
        scrollbar = Scrollbar(self.survey)
        scrollbar.pack(side=RIGHT, fill=Y)
        border = Frame(self.survey, width = width - 75, height = height)
        border.pack(expand=True)
        border.pack_propagate(False)
        title = Label(border, text=TITLE, font=("Times New Roman", 28, "bold")).pack()
        instructions = Label(border, text=INSTRUCTIONS, wraplength=width-75,
                             font=("Times New Roman", 18),
                             justify=LEFT).pack()
        """
        column1 = Frame(border, width = 600, height = height, bg='blue')
        column1.pack_propagate(False)
        column1.pack(side = LEFT)
        for q in self.question:
            Label(column1, text=q, font=("Times New Roman", 18)).pack()
        """
        self.survey.mainloop()


if __name__ == "__main__":
    test = UI()