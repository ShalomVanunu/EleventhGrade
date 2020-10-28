"""
this program check the number of users with random number

"""

import functions
import random

counter = 0 # reset the number of gussed
rand = random.randint(1,100) # this random a number of the computer

answer = "High"
while answer != "Equal"  :
    number, count = functions.user_choice(counter)
    answer = functions.compare(number, rand)
    print(answer)