from talk import talk


def game(cmove, pmove):
    if cmove == "rock" and pmove == "rock":
        talk("It is a draw !")

    elif cmove == "rock" and pmove == "paper":
        talk("You won !")

    elif cmove == "rock" and pmove == "scissor":
        talk("I won !")

    elif cmove == "paper" and pmove == "rock":
        talk("I won !")

    elif cmove == "paper" and pmove == "paper":
        talk("It is a draw !")

    elif cmove == "paper" and pmove == "scissor":
        talk("You won !")

    elif cmove == "scissor" and pmove == "rock":
        talk("You won !")

    elif cmove == "scissor" and pmove == "paper":
        talk("I won !")

    elif cmove == "scissor" and pmove == "scissor":
        talk("It is a draw !")
