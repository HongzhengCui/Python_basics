import sys
from sys import argv

def read_key_values(filename):
    """
    Reads a key-value delimited file (separated by first =) into a dictionary

    Args:
    filename(str): name of the file to read
    
    Returns:
    dictionary of the read items
    """
    dict = {}
    
    f = open(filename, 'r')
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        key, value = line.split("=")
        dict[key] = value
    
    return dict
    

def create_output_filename(name):
    """
    create the output file name.  Given an input filename such as "input.txt",
    return "input.txt.counts"
    """
    outname = name + ".counts"
    return outname

def process_key_file(filename,key_values):
    """
    Loads in a key file and produces a dictionary of the count of the values 
    If a key is not found in key_values use "<unknown>"

    Args:
    filename(str): file containing keys to process
    key_values(dict): existing keys to load
    """
    counts = {}
    f = open(filename, 'r')
    for line in f:
        line = line.strip()
        if line in key_values:
            value = key_values[line]
        else:
            value = "<unknown>"
            
        if value in counts:
            counts[value] = counts[value] + 1
        else:
            counts[value] = 1
    
    return counts

def write_output(filename,counts):
    """
    Sort the output value the highest count descending. If two values are
    equal, arbitrarily choose 1
    """
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0])) # From Chatgpt
    f = open(filename, 'w')
    for key, count in sorted_counts:
        f.write(f"{key}: {count}\n")

def process(args):
    """
    Implement your algorithm in this function
    """
    # print(args)   #Uncomment if you want to validate/see the command-line arguments
    key_value = read_key_values(args[1])
    
    for file in args[2:]:
        counts = process_key_file(file, key_value)
        output_name = create_output_filename(file)
        write_output(output_name, counts)

# __name__ == "__main__" and argv explained in the "modules" notebook
if __name__ == "__main__":
    if len(argv) < 3:
        print("Usage: python3 key_value.py file1_name file2_name ...")
        sys.exit(-1)
    process(argv)
