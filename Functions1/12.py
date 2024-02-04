my_nums = input("My list: ")
my_list = [int(num) for num in my_nums.split(",")]

def histogram(my_nums, my_list):
    for i in my_list:
        print('*' * i)

histogram(my_nums, my_list)
