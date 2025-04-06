#60% people have caliomurphy virus --- 85% tested positive --- 15% of people tested negative
#40% people do not have caliomurphy virus --- 98% tested negative --- 2% tested positive 

def find_prob(a,b):
    if a ==1:
        prob_a = 0.6
        if b ==1:
          prob_p = 0.85
        else:
          prob_p = 0.15
        prob_a_and_b = prob_a * prob_p
        print("the probability of both events occurring is", prob_a_and_b)
    if a ==2:
        prob_b = 0.40
        if b ==1:
             prob_p == 0.2
        else:
             prob_p == 0.98()
        prob_a_and_b = prob_a * prob_p
        print("the probability of both events occurring is ", prob_a_and_b)
            

print("Yo u have caliomurphy? \n 1.Yes \n 2.No")
a = int(input("Answer Bozo(1/2):"))

print("Yo u have tested positive? \n 1.Yes \2.No")
b = int(input("Answer Bozo(1/2):"))

print("probability of a and b occurring is :",)
find_prob(a,b)