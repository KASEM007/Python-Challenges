# Multiple choice quiz
from Questions import Questions

question_prompts = [
    "1-What is one right or freedom from the first Amendment? \n (a) Speech\n (b) religion\n (c) assembly\n (d) petition the government\n (e) press\n\n",
    "2-What is an amendment?\n (a) a change to the Constitution\n (b) an addition to the Constitution\n\n"
    "3-What is the highest court in the United State?\n (a) The Supreme Court",
]

questions = [
    Questions(question_prompts[0], "a"),
    Questions(question_prompts[0], "b"),
    Questions(question_prompts[0], "a"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print(f"You got {score} out of {str(len(questions))} correct")
    # print("You got " + str(score) + "/" + str(len(questions)) + "correct")


run_test(questions)

