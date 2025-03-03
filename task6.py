'''
Write a Python program to print the following string in a specific format (see the output).

Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"

Output :
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
'''

# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")



# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

# name = 'Shreyas Vora'
# print(name[::-1])



# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23

# print(list((3, 5, 7, 23)))
# print(tuple((3, 5, 7, 23)))



# Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java

# string = 'password.java'
# file_extension = string.split('.')
# print(file_extension[1])



# Write a Python program to display the first and last colors from the following list.

# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0:4:3])



# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

# exam_st_date = (11, 12, 2014)
# print(f"{exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]}")


# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

# n = int(input('Give a number to find an '))






sentence = "Samy has {} balloons.".format(5)
print(sentence)


