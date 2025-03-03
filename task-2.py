

# task-2 --> Get two lists ['a','b','c','d','e'],[1,2,3,4,5] and generate a single dictionary
# {'a':1,'b':2,'c':3,'d':4,'e':5} with the identical indexed items.


characters, numbers = ['a','b','c','d','e'],[1,2,3,4,5]
result = dict(zip(characters, numbers))
print(result)


