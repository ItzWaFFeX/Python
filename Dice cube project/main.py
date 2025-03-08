import random

def dice_cube():
    numbers = [1, 2, 3, 4, 5, 6]
    result = random.choice(numbers)
    probability = 1 / len(numbers)  
    print("The odds of picking the right one:", probability)
    
    if result == random.choice(numbers):
        return "You got it right"
    else:
        return "You lost" 

print(dice_cube())
