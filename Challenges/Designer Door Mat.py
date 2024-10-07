Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
Input Format

A single line containing the space separated values of  and .

Constraints

Output Format

Output the design pattern.

Sample Input

9 27
Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------




# Enter your code here. Read input from STDIN. Print output to STDOUT

def design_door_mat(N, M):
    # Calculate the number of rows above and below the middle line
    num_rows = (N - 1) // 2
    
    # Generate the top half of the mat including the middle line
    for i in range(num_rows):
        # Number of '.|.' patterns in the current row
        num_patterns = 2 * i + 1
        # Generate the pattern string for the current row
        pattern = '.|.' * num_patterns
        # Center the pattern with dashes
        print(pattern.center(M, '-'))
    
    # Print the middle line
    print('WELCOME'.center(M, '-'))
    
    # Generate the bottom half of the mat, which is a mirror of the top half
    for i in range(num_rows - 1, -1, -1):
        # Number of '.|.' patterns in the current row
        num_patterns = 2 * i + 1
        # Generate the pattern string for the current row
        pattern = '.|.' * num_patterns
        # Center the pattern with dashes
        print(pattern.center(M, '-'))

if __name__ == '__main__':
    # Read the input values
    N, M = map(int, input().split())
    # Generate and print the door mat design
    design_door_mat(N, M)
