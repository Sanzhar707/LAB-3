from itertools import permutations

def print_permutations():
    my_string = input("Enter a string: ")
    all_permutations = permutations(my_string)

    print("All permutations of the string: ")  
    for a in all_permutations:
        print(''.join(a))

print_permutations()