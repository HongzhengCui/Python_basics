def convert_mass(value, current, target):
    """
    The convert_mass function is to convert the current unit to the target unit automatically
    """
    unit = ["Kilogram", "Pound", "Stone", "Jin", "Seer", "Gram", "Oka"]
    # Create a list of strings for locating the current and target unit
    num = [1.0, 0.453592, 6.35029, 0.5, 1.25, 0.001, 1.2829]
    # Create a list of numbers coresponding to the list of units
    a1, a2 = 0, 0
    for i in range(len(unit)):  # Use a for loop to locate the current unit
        if unit[i] == current:
            a1 = i
            
    for j in range(len(unit)):  # Use a for loop to locate the target unit
        if unit[j] == target:
            a2 = j
            
    new = value * num[a1] / num[a2]  # Calculate the converted value
    return new
