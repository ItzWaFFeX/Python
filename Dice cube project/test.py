import random

def black_men():
    men = ["Eden", "Paul", "Myles", "Jabali"]
    result = random.choice(black_men)
    probability = 1 / len(black_men)  
    print("The odds of picking the right one:", probability)
    
    if result == random.choice(black_men):
        return "You got it right"
    else:
        return "You lost" 

print(black_men())