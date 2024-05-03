#rock,paper,scissor game with computer
import random
def main():
    def rps(bot,you):
        if bot==you:
            print("Its a tie!")

        elif bot=='r':
            if you=='s':
                print("You lost!")
            elif you=='p':
                print("You won!")


        elif bot=='p':
            if you=='r':
                print("You lost!")
            elif you=='s':
                print("You won!")

        elif bot=='s':
            if you=='p':
                print("You lost!") 
            elif you=='r':
                print("You won!")

    print("WELCOME TO ROCK:PAPER:SCISSOR")
    print("Computer's is choosing...")
    print("Computer have chosen")
    randno=random.randint(1,3)
    if randno==1:
        bot='r'
    elif randno==2:
        bot='p'
    elif randno==3:
        bot='s'

    print("Your turn:rock(r) paper(p) scissor(s)")
    you=input("Press 'r' for rock, 'p' for paper, 's' for scissor\n")


    print("Computer have chosen", bot)
    print("You have chosen", you)
    a=rps(bot,you)
    restart=input("DO you want to start again?[y/n]\n").lower()
    if restart=='y':
        main()
    else:
        exit()


main()
