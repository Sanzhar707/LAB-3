def unique_elements(my_nums, my_list):
    unique_list = []

    for element in my_list:
        if element not in unique_list:
            unique_list.append(element)

    print(unique_list)

my_nums = input("My list: ")
my_list = [int(num) for num in my_nums.split(",")]

unique_elements(my_nums, my_list)

