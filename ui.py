from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)
        self.window.wm_iconphoto(False, PhotoImage(file="images/quiz.png"))
        self.window.rowconfigure((0,1,2), pad=20)

        self.category_label = Label(text="Topic: Science", bg=THEME_COLOR, fg="white", font=("Ariel", 15, "bold"))
        self.category_label.grid(row=0, column=0, sticky="w")

        self.score_label = Label(text=f"Score: {self.quiz.score}/10", bg=THEME_COLOR,fg="white",font=("Ariel", 15, "bold"))
        self.score_label.config(pady=20)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300,height=250)
        self.question_text = self.canvas.create_text(150, 125,width=280, text="This is the question text", fill=THEME_COLOR, font=("Ariel", 20, "bold"))
        self.canvas.grid(column=0,row=1,columnspan=2)

        true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true,highlightthickness=0,border=0,command=self.true_pressed)
        self.true_button.config(pady=20)
        self.true_button.grid(column=0, row=2)

        false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false,highlightthickness=0,border=0,command=self.false_pressed)
        self.false_button.config(pady=20)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Thank You for Playing the Quizzler made by Anubhav!\nHave a Nice Day!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="Green")
            self.score_label.config(text=f"Score: {self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        else:
            self.canvas.config(bg="Red")
            self.score_label.config(text=f"Score: {self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        self.window.after(1000,self.get_next_question)