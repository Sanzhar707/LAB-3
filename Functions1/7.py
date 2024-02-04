def three_and_three(my_list):
    for i in range(len(my_list)-1):
        if my_list[i] == 3 and my_list[i+1]==3:
            print(True)
    return False

my_nums = input("My list: ")
my_list = [int(num) for num in my_nums.split(",")]

three_and_three(my_list)