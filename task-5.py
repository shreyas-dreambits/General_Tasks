
# 5 --> In a park, there are a certain number of buffaloes and cranes.
# Take the total number of heads and legs as input from the user to calculate 
# the number of buffaloes and cranes in the park.

total_number_of_heads = int(input('Add the number for buffalo and crane heads : '))
total_number_of_legs = int(input('Add the number for buffalo and crane legs : '))

def countingAnimals(total_number_of_heads, total_number_of_legs):
    
    total_number_of_buffaloes = (total_number_of_legs - total_number_of_heads * 2) // 2
    total_number_of_cranes = total_number_of_heads - total_number_of_buffaloes

    print('total number of buffaloes : ', total_number_of_buffaloes)
    print('total number of cranes : ', total_number_of_cranes)

countingAnimals(total_number_of_heads, total_number_of_legs)