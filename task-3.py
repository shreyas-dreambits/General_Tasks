
# 3 --> Write a function in Python to check duplicate letters. It must accept a string,
# i.e., a sentence. The function should return True if the sentence has any word with
# duplicate letters, else return False.


strings = set()

def check_duplicate(sentence):

    words = sentence.split()

    for word in words:
        strings.clear()
        for letter in word:
            if letter in strings:
                return True
            strings.add(letter)
    return False

sentence = 'The person over me looks smart.'
duplicate_letters = check_duplicate(sentence.lower())
print(duplicate_letters)