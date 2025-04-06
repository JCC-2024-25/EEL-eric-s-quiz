name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to the quiz.")
print("My name is Quizzy, and I will be quizzing you today.😀")
exit_outer_loop = False
while not exit_outer_loop:
    topic = input("What topic would you like to be quizzed on?(Math, History, Books)")
    if topic.lower() == "math":
        print("Great choice!")
        exit_outer_loop = True
        while True:
            difficulty = input("What difficulty level would you like? (easy, medium, hard)")
            if difficulty.lower() == "easy":
                print("Easy math questions coming up!")
                break
                #easy math questions here
            elif difficulty.lower() == "medium":
                print("Medium math questions coming up!")
                break
                #medium math questions here
            elif difficulty.lower() == "hard":
                print("Hard math questions coming up!")
                break
                #hard math questions here
            else:
                print("Sorry, I don't have that difficulty level. Please choose easy, medium, or hard.")
    elif topic.lower() == "history":
        print("Great choice!")
        exit_outer_loop = True
        while True:
            difficulty = input("What difficulty level would you like? (easy, medium, hard)")
            if difficulty.lower() == "easy":
                print("Easy history questions coming up!")
                break
                #easy history questions here
            elif difficulty.lower() == "medium":
                print("Medium history questions coming up!")
                break
                #medium history questions here
            elif difficulty.lower() == "hard":
                print("Hard history questions coming up!")
                break
                #hard history questions here
            else:
                print("Sorry, I don't have that difficulty level. Please choose easy, medium, or hard.")
    elif topic.lower() == "books":
        print("Great choice!")
        exit_outer_loop = True
        while True:
            difficulty = input("What difficulty level would you like? (easy, medium, hard)")
            if difficulty.lower() == "easy":
                print("Easy book questions coming up!")
                break
                #easy book questions here
            elif difficulty.lower() == "medium":
                print("Medium book questions coming up!")
                break
                #medium book questions here
            elif difficulty.lower() == "hard":
                print("Hard book questions coming up!")
                break
                #hard book questions here
            else:
                print("Sorry, I don't have that difficulty level. Please choose easy, medium, or hard.")
    else:
        print("Sorry, I don't have that topic. Please choose Math, History, or Books.")