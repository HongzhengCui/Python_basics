def make_change(amount):
    """
    Make changes
    """
    # Initialize an empty list to store the counts of each denomination
    change = []
    # Define a list of predefined denominations
    key = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.25, 0.10, 0.05, 0.01]
    
    # Loop through the denominations and calculate the count of each denomination needed
    for i in range(11):
        value = round(amount // key[i])  # Calculate the count of the current denomination
        change.append(value)  # Append the count to the change list
        amount = round(amount % key[i], 2)  # Update the remaining amount
    
    # Create a dictionary to represent the change, removing denominations with a count of 0
    change_dict = {
        100.00: change[0],
        50.00: change[1],
        20.00: change[2],
        10.00: change[3],
        5.00: change[4],
        2.00: change[5],
        1.00: change[6],
        0.25: change[7],
        0.10: change[8],
        0.05: change[9],
        0.01: change[10]
    }
    
    # Create a list of denominations to remove from the dictionary
    remove = []
    for x in change_dict:
        if change_dict[x] == 0:
            remove.append(x)
    
    # Remove denominations with a count of 0 from the dictionary
    for i in remove:
        change_dict.pop(i)
    
    return change_dict
    
    
def print_change(dict):
    """
    Print changes
    """
    for key, value in dict.items():
        print(f"${key:.2f}: {value}")        