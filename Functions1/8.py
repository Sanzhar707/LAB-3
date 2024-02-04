def contain_007(my_list):
    for i in range(len(my_list)-1):
        if my_list[i] == 0 and my_list[i+1]==0:
            if my_list[i+2]==7 and i+2 < len(my_list):
                print(True)
    return False

my_nums = input("My list: ")
my_list = [int(num) for num in my_nums.split(",")]

contain_007(my_list) 