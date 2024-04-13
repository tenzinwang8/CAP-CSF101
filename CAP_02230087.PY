################################
# Tenzin Wangchuk
# BE ELECTRICAL ENGG. 1ST YEAR
# CSF101
# 02230087
################################
# REFERENCES
# chat gpt
# youtube
################################
# SOLUTION
# Total Score:
# Put your number here
# input_7_cap1.txt()
################################
# Define a dictionary to map outcomes to scores
outcome_scores = {
    ('X', 'A'): 3,
    ('X', 'B'): 1, ('X', 'C'): 2,
    ('Y', 'A'): 4, ('Y', 'B'): 5,
    ('Y', 'C'): 6, ('Z', 'A'): 8, 
    ('Z', 'B'): 9, ('Z', 'C'): 7
}
#Assigns scores to opponent choices and outcomes.
#each tuple key corresponds to a particular opponent pair and outcome.
#Assigned value is represented by the #matching score.

# To dead the input.txt file
def read_input(file_name):
    Tenzin = []
    with open(file_name, 'r') as file:
        for line in file:
            opponent_choice, outcome = line.split()
            Tenzin.append((opponent_choice, outcome))
    return Tenzin
# The file name or input is the parameter for the aforementioned function, which reads the whole file, line by line.
#Each line consists of two parts: the opponent's option, split by a space, and the outcome.
#It adds each pair of the opponent's selection and result as a tuple to the Turn list.
#In the end, it returns the list turn, including all of the opponent's choices and outcomes.


# Calculate the score for each round
def calculate_score(Turn):
    score = 0
    for opponent_choice, outcome in turn:
        score += outcome_scores[(outcome, opponent_choice)]
    print(f"The total score is: {score}")
#defines the function calculate_score(Turn)
#accepts a single parameter, Turn, which is a list of tuples with the opponent's decisions and results.

# Example usage:
file_name = "CAP-CSF101/input_7_cap1.txt" 
turn = read_input(file_name)
calculate_score(turn)

#Assigns "02230087/input_7_cap1.txt" as file_name.
# To read input from a specific file, call the read_input function.
#  turn are kept in the turn variable.
# To output the total score depending on opponent choices and outcome, call the calculate_score function.