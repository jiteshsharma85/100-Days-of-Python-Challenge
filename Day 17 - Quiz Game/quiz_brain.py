class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        self.quit = True

    # Returns True if there are more questions and the user hasn't quit
    def still_have_question(self):
        return self.question_number < len(self.question_list) and self.quit

    # Asks the next question and checks the user's answer
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").lower()
        if user_answer == "quit":
            self.quit = False
            return
        self.check_answer(user_answer, current_question.answer)

    # Compares user answer to the correct answer and updates the score
    def check_answer(self, user_ans, correct_ans):
        if user_ans == correct_ans.lower():
            self.score += 1
            print("You are right!")
        else:
            print("You are wrong!")
        print(f"The correct answer is: {correct_ans}")
        print(f"Your current score: {self.score}/{self.question_number}\n")
