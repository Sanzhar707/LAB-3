def reverse_words(my_str):
    words_in_split = my_str.split()
    reversed_sentence = ' '.join(reversed(words_in_split))
    return reversed_sentence

my_str = input("Enter a sentence: ")

result = reverse_words(my_str)
print(result)