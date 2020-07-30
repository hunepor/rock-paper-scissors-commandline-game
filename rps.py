from random import choice

def game():
    r = 'rock'
    p = 'paper'
    s = 'scissors'
    options = [r, p, s]
    score = [0, 0]

    def askplayer():
        fromuser = input('Choose one of options (R / P / S): ').lower()
        
        if fromuser == "r":
            return r
        elif fromuser == "p":
            return p
        elif fromuser == "s":
            return s
        else:
            return askplayer()


    def play(fromuser):
        frompc = choice(options)
        
        if frompc == fromuser:
            
            print( "Draw")
        elif (frompc == s and fromuser == p) or \
             (frompc == p and fromuser == r) or \
             (frompc == s and fromuser == r):
            score[1] +=1
            print( "You lose")
        elif (frompc == p and fromuser == s) or \
             (frompc == r and fromuser == p) or \
             (frompc == r and fromuser == s):
            score[0] +=1
            print( "You win")
    
    def grid(fun):
        def f():
            return f'   {fun}'
        return f
    
    
    while (score[1] or score[0]) <= 2:
        play(askplayer())
        if score[0] == 3:
            print("     Cogratulations!")
            break
        print("     current score:")
        print("     You PC")
        print(f"      {score[0]}   {score[1]}")
        
    

if __name__ == "__main__":
    game()