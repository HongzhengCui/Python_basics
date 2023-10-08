import sys


def read_SP(filename):
    """
    _Read the valid SP data file, convert the data type and then return a 2D list_

    Args:
        filename (_csv_): _The file should contain three elements: Date, Index Level and Dividend_

    Returns:
        _2D list_: _The data structure is [[Year, Month, Index Level, Dividend]]_
    """
    try:  # Test the input file can be operated appropriately
        if (".csv" in filename) is False:  # Test if the input file type is 'csv'
            print("The type of the SP data input file should be '.csv'")
            sys.exit(20)
        
        file = open(filename, "r")
        lines = file.readlines()
        SP_info = []
    
        for line in lines[1:]:
            line = line.strip()
            parts = line.split(",")
        
            if len(parts) != 3:  # Test if the input file contain the expected number of data attributes
                print("The SP data input file should contain three elements: Date, Index Level and Dividend")
                sys.exit(20)

            for i in range(len(parts) // 3):
                date = parts[3 * i]
                date = date.split(".")
            
                year = int(date[0])
                month = int(date[1])
                
                if month > 12 or month < 1:  # Test if the month data is valid
                    print("The month should be from Jan to Dec in the SP data input file")
                    sys.exit(20)
            
                index_level = float(parts[3 * i + 1])
                dividend = float(parts[3 * i + 2])
                
                if index_level <= 0 or dividend <= 0:  # Test if the index level and dividend is valid
                    print("The values of Index Level and Dividend must be positive")
                    sys.exit(20)
            
                SP_info.append([year, month, index_level, dividend])
        
        # Test if the date in the SP input data file is consecutively increasing
        for i in range(1, len(SP_info)):
            if SP_info[i][0] * 12 + SP_info[i][1] <= SP_info[i - 1][0] * 12 + SP_info[i - 1][1]:
                print("The dates in the SP data input file must be consecutively increasing")
                sys.exit(20)
                    
    except SystemExit:
        print("The SP data input file is invalid")
        sys.exit(20)
            
    return SP_info


def read_Bond(filename):
    """
    _Read the valid Bond data file, convert the data type and then return a 2D list_

    Args:
        filename (_csv_): _The file should contain two elements: Date and PercentageRate_

    Returns:
        _2D list_: _The data structure is [[Year, Month, PercentageRate]]_
    """
    try:  # Test the input file can be operated appropriately
        if (".csv" in Bond_info_filename) is False:  # Test if the input file type is 'csv'
            print("The type of input files should be '.csv'")
            sys.exit(30)
        
        file = open(filename, "r")
        lines = file.readlines()
        Bond_info = []
    
        for line in lines[1:]:
            line = line.strip()
            parts = line.split(",")
        
            if len(parts) != 2:  # Test if the input file contain the expected number of data attributes
                print("The Bond data input file should contain two elements: Date and PercentageRate")
                sys.exit(30)

            for i in range(len(parts) // 2):
                date = parts[2 * i]
                date = date.split(".")
            
                year = int(date[0])
                month = int(date[1])
                
                if month > 12 or month < 1:  # Test if the month data is valid
                    print("The month should be from Jan to Dec in the Bond data input file")
                    sys.exit(30)
            
            PR = float(parts[2 * i + 1]) * 0.01
            
            if PR <= 0:  # Test if the index level and dividend is valid
                print("The values of PercentageRate must be positive")
                sys.exit(30)
            
            Bond_info.append([year, month, PR])
        
        # Test if the date in the Bond input data file is consecutively increasing    
        for i in range(1, len(Bond_info)):
            if Bond_info[i][0] * 12 + Bond_info[i][1] <= Bond_info[i - 1][0] * 12 + Bond_info[i - 1][1]:
                print("The dates in the Bond data input file must be consecutively increasing")
                sys.exit(30)
            
    except SystemExit:
        print("The SP data input file is invalid")
        sys.exit(20)      
          
    return Bond_info


def invest_equity(SP_info):
    """
    _Calculate the ROR of Strategy 1, and return a 2D list_

    Args:
        SP_info (_2D list_): _The data structure is [[Year, Month, Index Level, Dividend]]_

    Returns:
        _2D list_: _The data structure is [[Year, Month, Total_ROR]]_
    """
    equity_info = []
    
    for i in range(1, len(SP_info)):
        SP_ROR = SP_info[i][2] / SP_info[i - 1][2] - 1  # S&P ROR(t) = S&P(t) / S&P(t-1) – 1
        Div_ROR = (SP_info[i][3] / 12) / SP_info[i][2]  # Div ROR(t) = [Div(t) / 12] / S&P(t)
        total_ROR = SP_ROR + Div_ROR  # Portfolio ROR(t) = S&P ROR(t) + Div ROR(t)
        
        equity_info.append([SP_info[i][0], SP_info[i][1], total_ROR])
    
    return equity_info


def invest_bond(Bond_info):
    """
    _Calculate the ROR of Strategy 2, and return a 2D list_

    Args:
        Bond_info (_2D list_): _The data structure is [[Year, Month, PercentageRate]]_

    Returns:
        _type_: _The data structure is [[Year, Month, Bond_ROR]]_
    """
    bond_info = []
    
    for i in range(1, len(Bond_info)):
        Bond_ROR = Bond_info[i][2] / 12  # Bond ROR(t) = Bond(t) / 12
        
        bond_info.append([Bond_info[i][0], Bond_info[i][1], Bond_ROR])
    
    return bond_info


def calc_SP_bond(start_year, current_year, balance, ROR):
    """
    _Implement the equations to calculate the balances in Strategy 1 and Strategy 2_

    Args:
        start_year (_int_): _The year of the start date_
        current_year (_int_): _The year of the current date_
        balance (_float_): _The balance from the previous month_
        ROR (_float_): _The corresponding ROR with the current date_

    Returns:
        _float_: _The balance of the current date_
    """
    contribution = 100 * (1 + 0.025) ** (current_year - start_year)

    balance = balance * (1 + ROR) + contribution

    return balance


def calc_s1(start_year, start_month, end_year, end_month, equity_info):
    """
    _Calculate the balance of Strategy 1 and return a 2D list recording the balance_

    Args:
        start_year (_int_): _The year of the start date_
        start_month (_int_): _The month of the start date_
        end_year (_int_): _The year of the end date_
        end_month (_int_): _The month of the end date_
        equity_info (_a 2D list_): _The data structure is [[Year, Month, Total_ROR]]_

    Returns:
        _2D list_: _The data structure is [[Year, Month, balance]]_
    """
    balance = 0
    s1_record = []
    
    for i in range(1, len(equity_info)):
        if equity_info[i][0] == start_year and equity_info[i][1] == start_month:
            for x in range(i, len(equity_info)):
                balance = calc_SP_bond(start_year, equity_info[x][0], balance, equity_info[x][2])
                
                s1_record.append([equity_info[x][0], equity_info[x][1], balance])
                
                if equity_info[x][0] == end_year and equity_info[x][1] == end_month:
                    break
                
    return s1_record
    
 
def calc_s2(start_year, start_month, end_year, end_month, bond_info):
    """
    _Calculate the balance of Strategy 2 and return a 2D list recording the balance_

    Args:
        start_year (_int_): _The year of the start date_
        start_month (_int_): _The month of the start date_
        end_year (_int_): _The year of the end date_
        end_month (_int_): _The month of the end date_
        bond_info (_a 2D list_): _The data structure is [[Year, Month, Bond_ROR]]_

    Returns:
        _2D list_: _The data structure is [[Year, Month, balance]]_
    """
    balance = 0
    s2_record = []
    
    for i in range(1, len(bond_info)):
        if bond_info[i][0] == start_year and bond_info[i][1] == start_month:
            for x in range(i, len(bond_info)):
                balance = calc_SP_bond(start_year, bond_info[x][0], balance, bond_info[x][2])
                
                s2_record.append([bond_info[x][0], bond_info[x][1], balance])
                
                if bond_info[x][0] == end_year and bond_info[x][1] == end_month:
                    break
                
    return s2_record


def calc_lifecycle(start_year, current_year, balance, SP_ROR, Bond_ROR):
    """
    _Implement the equations to calculate the balances in Strategy 3_

    Args:
        start_year (_int_): _The year of the start date_
        current_year (_int_): _The year of the current date_
        balance (_float_): _The balance from the previous month_
        SP_ROR (_type_): _The corresponding SP ROR with the current date_
        Bond_ROR (_type_): _The corresponding Bond ROR with the current date_

    Returns:
        _float_: _The balance of the current date_
    """
    contribution = 100 * (1 + 0.025) ** (current_year - start_year)
    balance_equity = balance * (1 + SP_ROR) * (1 - 0.02 * (current_year - start_year))
    balance_bond = balance * (1 + Bond_ROR) * 0.02 * (current_year - start_year)
    
    balance = balance_equity + balance_bond + contribution
    
    return balance

    
def calc_s3(start_year, start_month, end_year, end_month, equity_info, bond_info):
    """
    _Calculate the balance of Strategy 3 and return a 2D list recording the balance_

    Args:
        start_year (_int_): _The year of the start date_
        start_month (_int_): _The month of the start date_
        end_year (_int_): _The year of the end date_
        end_month (_int_): _The month of the end date_
        equity_info (_a 2D list_): _The data structure is [[Year, Month, Total_ROR]]_
        bond_info (_a 2D list_): _The data structure is [[Year, Month, Bond_ROR]]_

    Returns:
        _2D list_: _The data structure is [[Year, Month, balance]]_
    """
    balance = 0
    s3_record = []
    
    for i in range(1, len(equity_info)):
        if equity_info[i][0] == start_year and equity_info[i][1] == start_month:
            for x in range(i, len(equity_info)):
                
                balance = calc_lifecycle(start_year, equity_info[x][0], balance, equity_info[x][2], bond_info[x][2])
                    
                s3_record.append([equity_info[x][0], equity_info[x][1], balance])
                
                if equity_info[x][0] == end_year and equity_info[x][1] == end_month:
                    break
                
    return s3_record
  
    
def save_balances(s1_record, s2_record, s3_record):
    """
    _Aggregate the lists and write the results as expected format to the target file_

    Args:
        s1_record (_2D list_): _The data structure is [[Year, Month, balance]]_
        s2_record (_2D list_): _The data structure is [[Year, Month, balance]]_
        s3_record (_2D list_): _The data structure is [[Year, Month, balance]]_
    """
    file = open("portfolio.csv", "w")
    file.write("Date,StrategyOne,StrategyTwo,StrategyThree" + "\n")
    
    for i in range(len(s1_record)):
        if s1_record[i][1] < 10:
            file.write("{}.0{},{:.2f},{:.2f},{:.2f}".format(
                s1_record[i][0], s1_record[i][1], s1_record[i][2], s2_record[i][2], s3_record[i][2]) + "\n")

        else:
            file.write("{}.{},{:.2f},{:.2f},{:.2f}".format(
                s1_record[i][0], s1_record[i][1], s1_record[i][2], s2_record[i][2], s3_record[i][2]) + "\n")


def process(SP_info_filename, Bond_info_filename, start_year, start_month, end_year, end_month):
    """
    _Implement all functions with order to achieve the result_

    Args:
        SP_info_filename (_csv_): _The file should contain three elements: Date, Index Level and Dividend_
        Bond_info_filename (_csv_): _The file should contain three elements: Date and PercentageRate_
        start_year (_int_): _The year of the start date_
        start_month (_int_): _The month of the start date_
        end_year (_int_): _The year of the end date_
        end_month (_int_): _The month of the end date_
    """
    SP_info = read_SP(SP_info_filename)
    equity_info = invest_equity(SP_info)

    Bond_info = read_Bond(Bond_info_filename)
    bond_info = invest_bond(Bond_info)
    
    s1_record = calc_s1(start_year, start_month, end_year, end_month, equity_info)
    s2_record = calc_s2(start_year, start_month, end_year, end_month, bond_info)
    s3_record = calc_s3(start_year, start_month, end_year, end_month, equity_info, bond_info)
    
    save_balances(s1_record, s2_record, s3_record)
      
      
if __name__ == "__main__":
    """
        _Implement checking command line arguments, call process()_
    """
    if len(sys.argv) != 5:
        print("Usage: python3 retirement.py <SP_info_filename> <Bond_info_filename> <start_date> <end_date>")
        sys.exit(10)
    
    SP_info_filename = sys.argv[1]
    Bond_info_filename = sys.argv[2]
        
    start_date = sys.argv[3]
    start_date = start_date.split(".")
    start_year = int(start_date[0])
    start_month = int(start_date[1])
    
    end_date = sys.argv[4]
    end_date = end_date.split(".")
    end_year = int(end_date[0])
    end_month = int(end_date[1])
    
    # Tests that the end date cannot before the start date
    if end_year * 12 + end_month <= start_year * 12 + start_month:  
        print("The end date cannot be before the start date")
        sys.exit(10)
    
    try:
        test_bond_info = open(Bond_info_filename)
        
    except FileNotFoundError:
        print("The Bond data input file is invalid")
        sys.exit(30)

    process(SP_info_filename, Bond_info_filename, start_year, start_month, end_year, end_month)