"""
Script Name:    UI

Description:    The user interface for administering the screener and
                displaying the results

Authors:        Luke Vandecasteele, Quinn Fetrow

Last Edited:    3/4/2022
Last Edit by:   Luke Vandecasteele

Credits: User Akash Shendage for his post on how to make a scrollbar using
         tkinter for an entire window.
         https://stackoverflow.com/questions/19860047/python-tkinter-scrollbar-for-entire-window
"""


from tkinter import *
from tkinter import ttk
from turtle import left
from SDQ import SDQ
from results import *

# Place Holder questions
temp_questions = []
for i in range(100):
    if i > 0:
        temp_questions.append(f"Question {i}")


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
FINAL_MESSAGE = "You have completed the SDQ mental health screener!\n\nTo view your results, you will" \
                " find a file labeled 'results.txt' " \
                "in the same folder as this application that will contain a complete " \
                "summary. Please remember, these results are intended for personal viewing, " \
                "or with the help of a psychologist.\n\nThank you for taking the SQD! Please select 'Take Again' " \
                "to take the screener again or select 'Finish' to close the application."


class UI():

    def __init__(self, questions):
        self.start = None
        self.survey = None
        self.final = None
        self.screener = SDQ()

    def run(self):
        if len(self.screener.questions) == 0:
            print("Error: No questions")
        else:
            self.init_interface()

    def init_interface(self):
        self.start = Tk()
        self.start.title(PROJECT)
        self.start.geometry("1000x500+375+175")
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
        # Create window
        self.survey = Tk()
        self.survey.title(PROJECT)
        height = self.survey.winfo_screenheight() - 10
        width = 1000
        self.survey.geometry("%dx%d+375+0" % (width, height))

        # Create A Main frame
        main_frame = Frame(self.survey)
        main_frame.pack(fill=BOTH, expand=1)

        # Create Frame for X Scrollbar
        sec = Frame(main_frame)
        sec.pack(fill=X, side=BOTTOM)

        # Create A Canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add Scrollbars to Canvas
        x_scrollbar = ttk.Scrollbar(sec, orient=HORIZONTAL, command=my_canvas.xview)
        x_scrollbar.pack(side=BOTTOM, fill=X)
        y_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        y_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        my_canvas.configure(xscrollcommand=x_scrollbar.set)
        my_canvas.configure(yscrollcommand=y_scrollbar.set)
        my_canvas.bind("<Configure>", lambda e: my_canvas.config(scrollregion=my_canvas.bbox(ALL)))

        # Frame for border
        border = Frame(my_canvas, width=width, height=height)

        # Add that New Frame a Window In The Canvas
        my_canvas.create_window((0, 0), window=border, anchor="nw")

        # title and instructions at the top of the page
        title = Label(border, text=TITLE, font=("Times New Roman", 28, "bold")).pack()
        instructions = Label(border, text=INSTRUCTIONS, wraplength=width-10,
                             font=("Times New Roman", 18), justify=LEFT).pack()

        # holds all questions on display
        questionsDisplay = Frame(border)

        n_true = Label(questionsDisplay, text="Not  \nTrue   ", font=("Times New Roman", 15)).grid(sticky=W, row=0,column=1)
        s_true = Label(questionsDisplay, text="Somewhat\nTrue", font=("Times New Roman", 15)).grid(sticky=W, row=0,column=2)
        c_true = Label(questionsDisplay, text="Certainly\nTrue", font=("Times New Roman", 15)).grid(sticky=W, row=0,column=3)

        # Keeps track of which row to place the question in
        # start with 1 for the labels above
        rowtrack = 1

        for question in self.screener.questions:
            qtext = Label(questionsDisplay, text=question.message,
                          font=("Times New Roman", 18)).grid(sticky = W, row=rowtrack, column=0)
            # Radio_answer is tied to the value given from the radio button objects
            Radio_answer = IntVar()
            for opt in range(3):
                new_option = Radiobutton(questionsDisplay, value=opt, variable=Radio_answer).grid(row=rowtrack,column=opt+1)
            # each question keeps track of the state of it's answer, once
            # the submit button is pressed, the question sets it's value equal to its state
            question.set_answerstate(Radio_answer)
            rowtrack+=1

        questionsDisplay.pack()

        submit = Button(border, text="Submit Screener", font=("Times New Roman", 20),
                command=lambda:{self.survey.destroy(), self.screener.submit, self.final_window()},
                cursor="plus", padx=5, pady=10).pack()
        self.survey.mainloop()

    def final_window(self):
        self.final = Tk()
        self.final.title(PROJECT)
        self.final.configure(bg="turquoise")
        self.final.geometry("800x250+200+200")
        message = Label(self.final, text=FINAL_MESSAGE, font=("Times New Roman", 20),
                        bg="turquoise", wraplength=780).pack()
        buttons = Frame(self.final)
        repeat = Button(buttons, text="Take Again", font=("Times New Roman", 20),
                        command=lambda:{self.final.destroy(), self.init_interface()},
                        cursor="plus", padx=5, pady=10).grid(row=0,column=0)
        finish = Button(buttons, text="Finish", font=("Times New Roman", 20), command=self.final.destroy,
                        cursor="plus", padx=5, pady=10).grid(row=0,column=2)
        buttons.pack()
        self.final.mainloop()




if __name__ == "__main__":
    test = UI(temp_questions)
    test.run()