def calculate_humanity(initial_humanity, degree_of_damage, degree_of_permanence):
    humanity = (initial_humanity - degree_of_damage) * (1 - degree_of_permanence)
    return humanity

while(True):
    initial_humanity = int(input("initial humanity(e.g 100): "))
    degree_of_damage = int(input("degree of damage(e.g 20): "))
    degree_of_permanence = float(input("degree of permanence(e.g 0.3): "))

    result = calculate_humanity(initial_humanity, degree_of_damage, degree_of_permanence)
    print("Calculated Humanity:", result)
    print()
