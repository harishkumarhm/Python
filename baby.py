from random import choice
questions=["What is your name?: ", "Why sky is blue?: ", "Why moon is bright?: "]
question = choice(questions)
answer = input(question).strip().lower()
while answer!="just like that":
    answer =input("Why?: ").strip().lower()
