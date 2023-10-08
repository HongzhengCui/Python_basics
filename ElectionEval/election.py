from sys import argv
import sys


def parse_state_information(filename):
    """
    Opens the state information file named in filename, loads all of the 
    values, placing them in a single data structure. Returns that data 
    structure.  You may created nested data structures.
    """
    file = open(filename, "r")
    lines = file.readlines()
    state_info = {}  # Create a nested data structure: {state name: [state population, electoral votes]}
    
    for line in lines:
        line = line.strip()
        parts = line.split(":")  
        # The parts includes the state name, the state population and the number of electoral votes it has
        
        for i in range(len(parts) // 3):
            state = parts[3 * i]
            population = int(parts[3 * i + 1])
            elecvote = int(parts[3 * i + 2])
            state_info[state] = [population, elecvote]
    
    return state_info


def print_state_information(state_info):
    """
    For the state_info data structure (produced as a result),  
    print all statues in alphabetical order using the string:
    "{}: Population - {:,d}, Electoral Votes: {:d}"
    """
    for state, info in sorted(state_info.items()):
        print("{}: Population - {:,d}, Electoral Votes: {:d}".format(state, info[0], info[1]))
        

def parse_vote_information(filename):
    """
    Opens the vote information file and returns the information 
    in a data structure
    """
    file = open(filename, "r")
    lines = file.readlines()
    vote_info = {}  # Create a dictionary: {state name: votes for Candidate A}
    
    for line in lines:
        line = line.strip()
        parts = line.split(":")  # The parts includes the state name and the votes received by Candidate A
        
        for i in range(len(parts) // 2):
            state = parts[2 * i]
            vote = int(parts[2 * i + 1])
            vote_info[state] = vote  
            
    return vote_info
        

def count_electoral_votes(state_info, vote_info):
    """
    Counts and returns the number of electoral votes received by 
    Candidate A in the election.

    For our purposes, Candidate A receives ALL electoral votes for a
    state if Candidate A receives strictly more than 50% of the votes in
    that State.  [Yes, we know that in the US there are a few states
    with more complex rules, but we will ignore them.  We will also
    ignore the electoral complexities of what would happen if a
    candidate received exactly 50%, and in this case, just say that
    Candidate A does not receive those electoral votes.  We are also
    assuming everyone in every state votes--while this doesn't happen in
    a real election, it is what we are doing here].
    """
    elec_vote_A = 0
    
    for state_name in state_info:
        # The voting rate of A is the number of votes for A divided by the total voting population in the state
        rate = vote_info[state_name] / state_info[state_name][0]
         
        # Candidate A will get all electoral votes of the state if the vote share passes the 50%
        if rate > 0.5:
            elec_vote_A += state_info[state_name][1]  
    
    return elec_vote_A
    

def determine_winner(state_info, candidate_a_electoral_votes):
    """
    Determines whether Candidate A or Candidate B won based upon who
    won the majority of the electoral votes. If there is a tie, return None.
    Returns "A", "B", or None    the last one is the value None
    """
    total_elec_vote = 0
    
    for state_name in state_info:
        # Calculate the US total electoral votes by summing all states' electoral votes up
        total_elec_vote += state_info[state_name][1] 
         
    # Candidate A will win if A gets more than half of the total electoral votes    
    if candidate_a_electoral_votes / total_elec_vote > 0.5:  
        return "A"
    
    elif candidate_a_electoral_votes / total_elec_vote == 0.5:
        return None
    
    else:
        return "B"


def print_winner(winner_name, number_of_votes):
    """
    Prints the winner.  If Candidate A or B wins, print
    "Candidate {} wins the election with {:d} votes" using the winner_name
    and number of Electoral College votes.

    If neither won the vote, print "It's a tie in the Electoral College."
    """
    if winner_name is None:
        print("It's a tie in the Electoral College.")
        
    elif winner_name == "A":
        print("Candidate {} wins the election with {:d} votes".format(winner_name, number_of_votes))
        
    else:
        # Votes earned by Candidate B is the US total electoral votes minus the electoral votes received by A
        print("Candidate {} wins the election with {:d} votes".format(winner_name, 538 - number_of_votes))  
         

def determine_recounts(state_info, vote_info):
    """
    Produces a list of strings, where each string represents information
    about a state the requires a recount. Recounts are required when a 
    Candidate A is within +/ 0.5% of 50% of the votes.  So 49.50% or 50.50%
    require a recount, while 49.49% and 50.51% do not require a recount.
    
    Only include states that require a recount in the result. For each state
    that requires a recount, include a line of the form:
    "{} requires a recount (Candidate A has {:.2f}% of the vote)".
    """
    elec_vote_A = 0
    recount = []
    
    for state_name in state_info:
        rate = vote_info[state_name] / state_info[state_name][0]
        
        # Recount is required if the voting rate of A is between [49.5%, 50.5%] in the state
        if rate > 0.495 and rate < 0.505:  
            recount.append("{} requires a recount (Candidate A has {:.2f}% of the vote)".format(state_name, rate * 100))
        
    return recount


def save_recounts(recount_list):
    """
    saves each entry of the list to a file named "recounts.txt".  The
    entries must be printed in alphabetical order.
    """
    file = open("recounts.txt", "w")
    recount_list = sorted(recount_list)
    
    for entry in recount_list:
        file.write(entry + "\n")


def determine_largest_win(state_info, vote_info):
    """
    Determines in which state Candidate A won the largest percentage 
    of the vote.

    returns a string with the following format:
    "Candidate A won {} with {:.2f}% of the vote"

    where the first {} should be the name of the state, and the {.2f} 
    should be the percentage of the vote won.  For example, it might return
    "Candidate A won California with 73.24% of the vote"

    None is returned if candidate A did not win a state
    """
    state_rates = []  # Create a 2D list: [[state name, voting rate of Candidate A]]
    max_rate = 0
    
    for state_name in state_info:
        rate = vote_info[state_name] / state_info[state_name][0]
        state_rates.append([state_name, rate])
    
    # Iterate through all the states and compare until find where Candidate A earns the largest win
    for i in range(len(state_rates)):
        if max_rate < state_rates[i][1]:
            max_rate = state_rates[i][1]
            max_state = state_rates[i][0]
    
    if max_rate <= 0.5:
        return None
    
    else:
        largest_win_string = "Candidate A won {} with {:.2f}% of the vote".format(max_state, max_rate * 100)
        return largest_win_string


def process(state_info_filename, voter_info_filename):
    """
    Implements the "Several steps exist for this assignment" section
    """
    state_info = parse_state_information(state_info_filename)        
    vote_info = parse_vote_information(voter_info_filename)
    print_state_information(state_info)
    
    elec_vote_A = count_electoral_votes(state_info, vote_info)
    winner = determine_winner(state_info, elec_vote_A)
    print_winner(winner, elec_vote_A)
    print(determine_largest_win(state_info, vote_info))
    
    recount_list = determine_recounts(state_info, vote_info)
    save_recounts(recount_list)
    
    
if __name__ == "__main__":
    """implement checking command line arguments, call process()"""
    if len(sys.argv) != 3:
        print("Usage: python3 election.py <state_info_filename> <voter_info_filename>")
        sys.exit(1)

    state_info_filename = sys.argv[1]
    voter_info_filename = sys.argv[2]

    try:
        process(state_info_filename, voter_info_filename)
        
    except SystemExit:
        sys.exit(1)
