
# 3 --> Write a function in Python to check duplicate letters. It must accept a string,
# i.e., a sentence. The function should return True if the sentence has any word with
# duplicate letters, else return False.


def check_duplicate(sentence):
    strings = set()
    words = sentence.split(' ')

    for word in words:
        for duplicate_str in word:
            if duplicate_str in strings:
                return True
            strings.add(duplicate_str)
    return False

sentence = 'The person over me looks smart.'
duplicate_letters = check_duplicate(sentence.lower())
print(duplicate_letters)