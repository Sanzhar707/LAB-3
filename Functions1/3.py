heads = int(input("How many heads: "))
legs = int(input("How many legs: "))
a = 0
numrabbits = 0
numchickens = 0
def quantity(heads, legs, a, numrabbits, numchickens):
    a = legs - heads * 2
    if a==0:
        print(heads, "chickens")
        print(0, "rabbits")
    else:
        numrabbits = a/2
        numchickens = heads - numrabbits
        print(numrabbits, "rabbits")
        print(numchickens, "chickens")   
quantity(heads, legs, a, numrabbits, numchickens) 