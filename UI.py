"""
Script Name:    UI

Description:    The user interface for administering the screener and
                displaying the results

Authors:        Luke Vandecasteele

Last Edited:    2/27/2022
Last Edit by:   Luke Vandecasteele

Credits: User Akash Shendage for his post on how to make a scrollbar using
         tkinter for an entire window.
         https://stackoverflow.com/questions/19860047/python-tkinter-scrollbar-for-entire-window
"""


from tkinter import *
from tkinter import ttk

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

        # For each question add the question and possible answer selections
        for phrase in self.question:
            new_frame = Frame(border)
            new_frame.pack(anchor="w")
            q = Label(new_frame, text=phrase, font=("Times New Roman", 18)).pack(side=LEFT)
            for opt in range(3):
                answer_frame = Frame(new_frame)
                answer_frame.pack(side=LEFT)
                new_option = Radiobutton(answer_frame, value=opt).grid(row=0, column=opt+1)

        self.survey.mainloop()


if __name__ == "__main__":
    test = UI()