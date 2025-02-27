
# 4 --> Write a function in Python to parse a string such that it accepts a parameter- an encoded string.
# This encoded string will contain a first name, last name, and an id. You can separate the values in the
# string by any number of zeros. The id will not contain any zeros. The function should return a Python
# dictionary with the first name, last name, and id values. For example, if the input would be “John000Doe000123”.
# Then the function should return: { “first_name”: “John”, “last_name”: “Doe”, “id”: “123” }


def encrytedText(encoded_string):

    cleaned_Data = encoded_string.replace('0',' ').split()

    return {
            'first_name': cleaned_Data[0],
            'last_name': cleaned_Data[1],
            'id': cleaned_Data[2]
        }

encodedData='Shreyas00Vora0000163'
parsed_Data = encrytedText(encodedData)
print(parsed_Data)
