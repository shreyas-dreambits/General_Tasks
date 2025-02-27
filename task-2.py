

# task-2 --> Get two lists ['a','b','c','d','e'],[1,2,3,4,5] and generate a single dictionary
# {'a':1,'b':2,'c':3,'d':4,'e':5} with the identical indexed items.


characters = ['a','b','c','d','e']
numbers = [1,2,3,4,5]
dict = {}
dict1 = {}

for char in characters:
    for num in numbers:
        dict[char] = num
        dict1.update({char:num})

print(dict)
print(dict1)
