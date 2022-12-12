win_num = 43
guess = 1
num = int(input("guesss a number btw 1 and 100: "))
game_over =False
 
while not game_over:
    if num == win_num:
        print("you win,you guessed this number in",guess,"times")
        game_over = True
    else:
        if num<win_num:
            print("too low")
            guess += 1
            num = int(input("guess again:"))       
        else:
            print("too high:")
            guess+=1
            num = int(input("guess again:"))