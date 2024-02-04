F = float(input("Enter temperature in Fahrenheit: "))
C = 0.0
def Fahrenheit_to_centigrrade(F, C):
    C = (5 / 9) * (F - 32)
    print(C, "C")
Fahrenheit_to_centigrrade(F, C)