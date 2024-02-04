my_str = input("Write a word: ")
def palindrome(my_str):
    clone_my_str = list(my_str)
    palindromed_str = list(reversed(clone_my_str))
    if palindromed_str == clone_my_str:
        return True
    else:
        return False

result = palindrome(my_str)
print(result)