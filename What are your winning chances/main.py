
red_balls = 1
blue_balls = 6
white_balls = 3
total_balls = red_balls + blue_balls + white_balls


P_white1 = white_balls / total_balls


P_white2_given_white1 = white_balls / total_balls


print(f"The probability that the second ball is also white given that the first ball is white: {P_white2_given_white1:.2f}")
