# Title: Test Average and Grade Program
# Program created by William Schaeffer
# CPS 313
# P. 297, Exercise 15, Test Average and Grade Program
# 01.25.22

# This program will take 5 test scores and display letter grade for each score and average score

import sys                                              # For Command-Line Args
number_of_scores = 5                                    # Global constant for number of scores to demonstrate global constant
                                                            # This would be better suited as user input per amount of scores needed
# Main Function

def main():
    
    #print(f'Please enter 5 test scores: ')             # Uncomment for for user input outside of terminal
    
    #score1 = double(input('What is the first test score? '))
    #score2 = double(input('What is the second test score? '))
    #score3 = double(input('What is the third test score? '))
    #score4 = double(input('What is the fourth test score? '))
    #score5 = double(input('What is the fifth test score? '))


    #score1 = double(sys.argv[1])                       # Command-Line Arguments
    #score2 = double(sys.argv[2])
    #score3 = double(sys.argv[3])
    #score4 = double(sys.argv[4])
    #score8 = double(sys.argv[5])

    score1 = 76                                         # Test defined variables
    score2 = 86
    score3 = 96
    score4 = 88
    score5 = 92

    average = calc_average(score1, score2, score3, score4, score5)

    print()
    print(f'Grades:')
    print(f'{score1} is a(n) ', end='')
    determine_grade(score1)
    print(f'{score2} is a(n) ', end='')
    determine_grade(score2)
    print(f'{score3} is a(n) ', end='')
    determine_grade(score3)
    print(f'{score4} is a(n) ', end='')
    determine_grade(score4)
    print(f'{score5} is a(n) ', end='')
    determine_grade(score5)
    print(f'Average Score: {average:.0f}')
    


# Function Definition

def calc_average(gr1, gr2, gr3, gr4, gr5):              # Function to calculate average score

    avg = (gr1+gr2+gr3+gr4+gr5)//number_of_scores       # avg = sum of entered scores divided by number of scores, // for integer division
                                                            # integer division for textbook example, real world example would want double
    return avg

def determine_grade(grade):                             # Function to determine letter grade

    if grade >= 90:                                     # If grade is equal to or greater than 90, print A
        print(f'A')
    elif grade >= 80 and grade < 90:                    # If grade is equal to or greater than 80 and less than 90, print B 
        print(f'B')
    elif grade >= 70 and grade < 80:                    # If grade is equal to or greater than 70 and less than 80, print C
        print(f'C')
    elif grade >= 60 and grade < 70:                    # If grade is equal to or greater than 60 and less than 70, print D
        print(f'D')
    elif grade < 60 and grade >= 0:                     # If grade is less than 60 and greater than 0, print F
        print(f'F')
    else:
        print(f'You entered an invalid score')          # Else if grade is less than 0, somebody made serious mistakes
    



main()                                                  # Call main function

