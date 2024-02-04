my_list = []
prime_numbers = []

numbers = [int(num) for num in input("Enter numbers: ").split(", ")]
my_list.extend(numbers)

def filter_prime(numbers, my_list, prime_numbers):
    for number in my_list:
        if number == 2 or number == 3 or number == 5 or number == 7 or (number > 1 and number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0):
            prime_numbers.append(number)

filter_prime(numbers, my_list, prime_numbers)
print(prime_numbers)
