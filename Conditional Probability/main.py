def a_and_b (a,b):
    if a ==1:
        prob_freshman = 0.3
        if b ==1:
            prob_eating = 0.75
        else:
            prob_eating = 0.25
        print("probability of a given b", prob_eating)
    if a == 2:
        prob_freshman = 0.7
    if b == 2:
        pron_eating = 0.6
    else:
        prob_eating = 0.4
    print("the probability of a given b", prob_eating)

    prob_a_and_b = prob_freshman * prob_eating

    print("probability of a given b ", prob_dining)

prob_a_and_b = prob_student * prob_dining #joint probability

print("Check the probability of any event occuring. Enter your choices:")

print("is the student a freshman? \n 1.Yes \n 2.No")

a = int(input("Enter your choice(1/2): "))

print("is the student eating in the dining hall? \n 1.Yes \n 2.No")

b = int(input("Enter your choice(1/2): "))

print("this is the probability of both events occuring", a_and_b(a,b))
