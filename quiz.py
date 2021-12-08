from component.quizQuestion import questions
from component import vars,quizTally
from PIL import Image
from colorama import Fore, Back, Style


answer1 = questions ["q1"] [input(questions["q1"]["question"])]
print(answer1)

vars.quizTotal += answer1
print(Fore.MAGENTA + '-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n')

answer2 = questions ["q2"] [input(questions["q2"]["question"])]
print(answer2)

vars.quizTotal += answer2
print(Fore.GREEN + '-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n')

answer3 = questions ["q3"] [input(questions["q3"]["question"])]
print(answer3)

vars.quizTotal += answer3
print(Fore.CYAN + '-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n')

answer4 = questions ["q4"] [input(questions["q4"]["question"])]
print(answer4)

vars.quizTotal += answer4
print(Fore.YELLOW + '-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n')

answer5 = questions ["q5"] [input(questions["q5"]["question"])]
print(answer5)

vars.quizTotal += answer5
print(Fore.MAGENTA + '-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n')

print("total so far: " + str(vars.quizTotal) + "\n")

quizTally.total(vars.quizTotal)



