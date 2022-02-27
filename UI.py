"""
Script Name:    UI

Description:    The user interface for administering the screener and
                displaying the results

Authors:        Luke Vandecasteele

Last Edited:    2/27/2022
Last Edit by:   Luke Vandecasteele
"""


from tkinter import *


#Global Variables
PROJECT = "Mental Health and Wellness Personal Screener: SDQ"
TITLE = "Strengths and Difficulties Questionnaire"
INSTRUCTIONS = "\nFor each item, please mark the box for Not True, Somewhat True " \
               "or Certainly True. It would help us if you answered all items " \
               "as best you can even if you are not absolutely certain . Please " \
               "give your answers on the basis of how things have been for you " \
               "over the last six months.\n"
INSTRUCTIONS2 = "\nThese instructions will be provided on the next page as well for" \
                " your convenience.\n"
WARNING = "This screener is only for personal use. Do NOT share the results" \
          ". Only complete this screener by yourself or with the " \
          "help of a psychologist. Mental health is very personal and should " \
          "be respected."

class UI():
    """
    root =Tk()

    option = ["luke", "quinnkjhlkjhlkhj", "amy"]
    r1 = Radiobutton(root, value=1).grid(row=0,column=0)
    r2 = Radiobutton(root, value=2).grid(row=0,column=1)
    r3 = Radiobutton(root, value=3).grid(row=0,column=2)
    root.mainloop()
    """

    def __init__(self):
        self.start = None
        self.survey = None
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
        warning = Label(self.start, text=WARNING, wraplength=800,
                        font=("Times New Roman", 20), justify=LEFT,
                        bg="turquoise", fg='black').pack()
        instructions2 = Label(self.start, text=INSTRUCTIONS2, wraplength=800,
                              font=("Times New Roman", 20), justify=LEFT,
                              bg="turquoise", fg='black').pack()
        begin = Button(self.start, text="Begin Screener", font=("Times New Roman", 20),
                       command=lambda:[self.start.destroy(), self.display_survey()],
                       cursor="plus", padx=5, pady=10).pack()
        self.start.mainloop()

    def display_survey(self):
        self.survey = Tk()
        self.survey.title(PROJECT)
        self.survey.geometry("500x500+100+100")
        test = Label(self.survey, text="Begin test")
        self.survey.mainloop()

if __name__ == "__main__":
    test = UI()