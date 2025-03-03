
# 3 --> Write a function in Python to check duplicate letters. It must accept a string,
# i.e., a sentence. The function should return True if the sentence has any word with
# duplicate letters, else return False.


def check_duplicate(word):
    for letter in word:
        if word.count(letter) > 1:
            return True
    return False

word = 'sentence'
duplicate_letters = check_duplicate(word.lower())
print(duplicate_letters)
