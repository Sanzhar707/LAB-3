radius = float(input("Enter the radius: "))

def volume_of_sphere(radius):
    volume = (4/3) * 3.14 * radius**3
    print("volume: ", volume)

volume_of_sphere(radius)