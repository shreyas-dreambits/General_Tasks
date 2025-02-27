
# 5 --> In a park, there are a certain number of buffaloes and cranes.
# Take the total number of heads and legs as input from the user to calculate 
# the number of buffaloes and cranes in the park.


def countingParts(buffaloes_heads, buffaloes_legs, cranes_heads, cranes_legs):
    
    number_of_buffaloes =  (buffaloes_heads + buffaloes_legs) / 5
    number_of_cranes = (cranes_heads + cranes_legs) / 3

    print('total number of buffaloes : ', number_of_buffaloes)
    print('total number of cranes : ', number_of_cranes)

countingParts(15,60,12,24)