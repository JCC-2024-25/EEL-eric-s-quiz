name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to the quiz.")
print("My name is Quizzy, and I will be quizzing you today.")
exit_outer_loop = False
while not exit_outer_loop:
    topic = input("What topic would you like to be quizzed on?(Math, History, Books)")
    if topic.lower() == "math":
        exit_outer_loop = True
        print("Great choice!")
        print("Let's get started with some math questions.")
        print("How we're going to do this is I will ask you a multiple choice question and you will have to answer it.")
        print("If you get it right, you will get a point. If you get it wrong, you will not get a point.")
        print("At the end of the quiz, I will tell you how many points you got.")
        print("The questions will start easy and get harder as we go.")
        print("Let's get started!")
    elif topic.lower() == "books":
        print("Great choice!")
        print("Let's get started with some book-related questions.")
        print("How we're going to do this is I will ask you a multiple choice question and you will have to answer it.")
        print("If you get it right, you will get a point. If you get it wrong, you will not get a point.")
        print("At the end of the quiz, I will tell you how many points you got.")
        print("The questions will start easy and get harder as we go.")
        print("Let's get started!")
    elif topic.lower() == "history":
        print("Great choice!")
        print("Let's get started with some history questions.")
        print("How we're going to do this is, I will ask you a multiple choice question and you will have to answer it.")
        print("If you get it right, you will get a point. If you get it wrong, you will not get a point.")
        print("At the end of the quiz, I will tell you how many points you got.")
        print("The questions will start easy and get harder as we go.")
        print("Let's get started!")    
else:
        print("Sorry, I don't have that topic. Please choose Math, History, or Books.")