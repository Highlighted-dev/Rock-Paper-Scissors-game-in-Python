import random
i = 0

while True:
    userInput = input("Rock, Paper or Scissors: ")
    userInput = userInput.capitalize()
    if userInput.lower() == "exit":
        break

    randomIntForBot = random.randint(0,2)
    rockPaperScissorsArray = ["Rock","Paper","Scissors"]
    botChoice = rockPaperScissorsArray[randomIntForBot]

    print(f"You: {userInput}")
    print(f"Bot: {botChoice}")
    if not userInput in rockPaperScissorsArray:
        print("You have to type 'Rock', 'Paper' or 'Scissors' \n")
    elif userInput == botChoice:
        print("Result: Draw! \n")
    elif userInput == "Rock" and botChoice == "Scissors" or userInput == "Scissors" and botChoice == "Rock" or userInput == "Paper" and botChoice == "Rock":
        print("Result: You won! \n")
    else:
        print("Result: Bot  won! \n")


    i = 0






