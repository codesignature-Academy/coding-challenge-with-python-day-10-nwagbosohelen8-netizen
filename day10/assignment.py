def is_pangram(word):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    word = word.lower()

    for letter in alphabet:
        if letter not in word:
            return False
        else:
            pass
    return True
print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Hello world"))




def even_numbers(numbers):
    even = []
    for n in numbers:
        if n % 2 == 0:
            even.append(n)
    return even


