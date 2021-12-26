print("Welcome in game Questions and Answer!!")

name = input("What's your name : ")
ready = input("Ok {} do you ready play this game (yes/no) : ".format(name))

questions = 5
score = 0

if ready.lower() == "yes":
    ans = input("What animal do you like? : ")
    if ans.lower() == "cat":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    ans = input("What sport do you like? : ")
    if ans.lower() == "football":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")

    ans = input("What food do you like? : ")
    if ans.lower() == "fried rice":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    ans = input("What kind of place do you like? : ")
    if ans.lower() == "panorama":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    
    ans = input("What lessons do you like? : ")
    if ans.lower == "database":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

else:
    print("Ok, thank you ", name, "\n")

total = (score/questions) * 100

print("Your score is : {:.1f}%".format(total))
print("It is finished, Goodbye...")
