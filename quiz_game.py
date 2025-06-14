def quiz_game():
    print("Welcome to my computer quiz")
    
    playing = input("Are you interested in playing the game? (yes/no) ").lower()
    
    if playing != "yes":
        quit()

    print("Ok, let's play :)")

    answer = input("What does CPU stand for? ")

    if answer.lower() == "central processing unit":
        print("Correct!")
    else:
        print("Incorrect")

    answer = input("What does RAM stand for? ")

    if answer.lower() == "Random access Memory":
        print("Correct!")
    else:
        print("Incorrect")

    answer = input("What does PSU stand for? ")

    if answer.lower() == "power supply unit":
        print("Correct!")
    else:
        print("Incorrect")

    answer = input("What does GPU stand for? ")

    if answer.lower() == "Graphical processing unit":
        print("Correct!")
    else:
        print("Incorrect")

quiz_game()