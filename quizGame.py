print("Welcome to my coding quiz!")

play = input("Do you want to play? ")

if play.lower() != "yes":
    quit()

print("Okay, Let's play :)")
score = 0

answer = input("What is HTML in full? ")
if answer.lower() == "hyper text markup language":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What is CSS in full? ")
if answer.lower() == "cascading style sheets":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What is JS in full? ")
if answer.lower() == "Java Script":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What is py in full? ")
if answer.lower() == "python":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What is DBMS in full? ")
if answer.lower() == "database management system":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + "questions correct!")
print("You got " + str((score / 5) * 100) + "%.")

