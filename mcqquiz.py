# MCQ Quiz
from mcqqn import Question


question_prompts = [
    "What color are woods ?\n(a)Red\n(b)Brown\n(c)White\n\n",
    "What color are Guava ?\n(a)Red\n(b)Green\n(c)White\n\n",
    "What color are Oranges ?\n(a)Red\n(b)Brown\n(c)Orange\n\n",
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]


def run_test(questions):
    score = 0
    for qn in questions:
        answer = input(qn.prompt)
        if answer == qn.answer:
            score += 1
    print("You Got {}/{}".format(score, len(questions)))


run_test(questions)
