def retirement(start_age, initial_savings, working_info, retired_info):
    """
    Prints the current status of an individual's retirement account.

    The dictionaries both have these fields:
         "months","contribution","rate_of_return"

    Args:
      start_age (int): At what age (in months) does the individual start
      initial_savings (float): initial savings in dollars
      working_info (dict): information about working
      retired_into (dict): information about retirement
    Returns:
      None
    """    
    print(f"Age {(start_age//12):3d} month {(start_age%12):2d} you have ${initial_savings:,.2f}")
    
    for i in range(start_age, 1199, 1):
        start_age = start_age + 1
        year = start_age // 12
        month = start_age % 12
        
        if start_age <= 68*12:
            rate_of_return = working_info["rate_of_return"]
            contribution = working_info["contribution"]
        else:
            rate_of_return = retired_info["rate_of_return"]
            contribution = retired_info["contribution"]
        
        initial_savings = initial_savings*(1+rate_of_return) + contribution
        
        print(f"Age {year:3d} month {month:2d} you have ${initial_savings:,.2f}")
    
#####################
working_info = {
    "contribution": 1000,
    "rate_of_return": 0.045/12
}

retired_info = {
    "contribution": -4000,
    "rate_of_return": 0.01/12
}

retirement(327, 21345, working_info, retired_info)
