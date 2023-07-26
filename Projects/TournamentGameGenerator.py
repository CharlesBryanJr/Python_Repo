'''TournamentGameGenerator.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0200
print(" ")

'''

Question:

For this project you will be asked to,
create a program that can,
schedule games that teams will play,
in an end of year tournament. 

You will only be responsible for,
determining the games played,
in the first round of the tournament.

You will first need to ask,
the user of your program,
to input the number of teams;
	you may assume,
    there will always be,
    an even number of teams
    (you don't need to validate this). 
	Next you will need to ask for,
    the names of all of the teams,
    and store them in some way.

After this you'll need to determine,
the number of games,
that were played by each team;
	you may assume each team, 
	plays the same number of games. 

Finally, you'll need to determine,
the number of wins,
each team had,
 during the regular season.

When asking for user input, 
you'll need to make sure all input is valid,
and ask the user to try again,
if they give you invalid input.
	You may assume user input, 
    will always be the correct type 
    (i.e. if you ask for a number,
    you will always get an integer). 
    You can determine, 
    if the input is invalid,
    by looking at the following constraints:

- There are always at least 2 teams,
in the tournament.
- Each team plays every other team,
at least once in the regular season.
- All team names contain,
at most 2 words and at least 2 characters.
- Each team has at minimum,
0 wins and no more wins,
than the number of games they played.

In the first round of the tournament,
the teams with the most regular season wins,
play the teams with the least regular season wins. 
For example, 
if Team A has 5 wins, 
Team B has 4 wins, 
Team C has 3 wins 
and Team D has 2 wins 
then Team A and Team D play each other 
and Team B and C play each other. 
If teams are tied,
for wins and/or losses,
then your program can choose any appropriate team.

Your program should output,
the games that should be played, 
in the format seen below. 

The first game outputted,
should contain,
the team with the most regular season wins, 
the second game, 
should contain,
the team with the second most regular season wins,
etc. 

The home team of each game,
should be the team with,
the least wins of the two, 
if there is a tie in wins, 
your program can chose any appropriate team.

See below for the sample program execution. 
Your prompts and output, 
should follow the same format as seen below.

Sample Program Execution #1
Sample Program Execution #1
Sample Program Execution #1

Enter the number of teams in the tournament: 1
The minimum number of teams is 2, try again.
Enter the number of teams in the tournament: 4
Enter the name for team #1: Python
Enter the name for team #2: Ruby
Enter the name for team #3: JavaScript
Enter the name for team #4: C
Team names must have at least 2 characters, try again.
Enter the name for team #4: C Is Great
Team names may have at most 2 words, try again.
Enter the name for Team #4: C#
Enter the number of games played by each team: 2
Invalid number of games. Each team plays each other at least once in the regular season, try again.
Enter the number of games played by each team: 3
Enter the number of wins Team Python had: 2 
Enter the number of wins Team Ruby had: 1 
Enter the number of wins Team JavaScript had: 0 
Enter the number of wins Team C# had: -2
The minimum number of wins is 0, try again.
Enter the number of wins Team C# had: 3
Generating the games to be played in the first round of the tournament...
Home: JavaScript VS Away: C#
Home: Ruby VS Away: Python






Sample Program Execution #2
Enter the number of teams in the tournament: 6
Enter the name for team #1: AA
Enter the name for team #2: BB
Enter the name for team #3: CC
Enter the name for team #4: DD
Enter the name for team #5: EE
Enter the name for team #6: FF
Enter the number of games played by each team: 2
Invalid number of games. Each team plays each other at least once in the regular season, try again.
Enter the number of games played by each team: 6
Enter the number of wins Team AA had: 1 
Enter the number of wins Team BB had: 4 
Enter the number of wins Team CC had: 3 
Enter the number of wins Team DD had: 4 
Enter the number of wins Team EE had: 2 
Enter the number of wins Team FF had: 7 
The maximum number of wins is 6, try again.
Enter the number of wins Team FF had: 5 
Generating the games to be played in the first round of the tournament...
Home: AA VS Away: FF
Home: EE VS Away: BB
Home: CC VS Away: DD


Type of Question:
- Array
		- draw indices
		- sorting
    - multiple pointers
    - mutating the current index or later index to count
    - hashing the index values
		- running sums
		- sliding windows
			- start_of_window
			- end_of_window

# Dictionaries (Hashmaps)
 # Understand how to add addition values to a key in a dictionary
    # for each key, create the values as a 2D array
    # when addition values need to be added to a key, append the addition values
	# Understand how to avoid duplicates
    # only add a key & value to a dictionary
    # at the last occurence/opportunity to create the key & value
    # or
    # add to a key's values in a dictionary
    # at the last occurence/opportunity to add to the key's values

# Recursion
	# the solution depends on solutions to smaller instances of the same problem
		# define the smaller instance of the problem
			# translate the for/while loop into a base case
	# will iterate/traverse until the function can return a value (base case)
		# always include return statment
	# base case == the smallest instance of the problem that can be solved directly
	# to keep track of element, store the element in a variable that connected to the recursion call
	# running variables left to right
			# arguments 
	# running variables right to left
			# return statment
	# Recursive functions often take a sub array of the original array
	# the outcome of a recursive function will affect code on lines after it
	# To optimize use memoization
		# store the answer to recursive calls in a hash table
	# 1. Base Case
	# 2. Action
	# 3. update variables
	# 4. Recursion
		if idx >= len(array):
	
 
# Searching
# Sorting
# Stacks
# Strings
# Tries

Input(matrix, array, matrix, array, int): calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
# Intuitive
# Primitive Types
		# Strings
			# Empty string
			# NULL or nil (and Optionals, depending on language)
			# Spaces (multiple words or sentences, or single/multiple whitespaces alone)
			# Punctuation
			# Upper, lowercase, or mixed (e.g., “stRiNg”)
			# Strings of numbers (e.g., “12”) Should these be changed to Int, Float, or Double?
			# Different Languages (Diacritics? Unicode compliant? ASCII?)
			# Emoji 👍 (especially if question is presented as a text field input by a user)
			# Long String
		# Arrays
			# Empty array
			# Nested or not nested
		# Dictionaries (Hashmaps)
			# Collisions

Techniques & Tricks
# peaks and valleys of integers
# draw indices
# sorting
# running sums
# multiple pointers
# isolating idx or node
# modifying the input
	# hashing the index values, for 1 to n values
# sliding windows
	# start_of_window and end_of_window
# pre compute
	# left to right
	# right to left

# simplest / smallest problem
	#

# If I knew / had this....
	# 
	# reverse this statement

'''

'''
# Time: O() | # Space: O()
get_number_of_teams




Output(int): num_teams
'''

# Time: O() | # Space: O()
def get_number_of_teams():
    while True:
        num_teams = int(input("Enter the number of teams in the tournament: "))

        if num_teams >= 2:
            break

        print("The minimum number of teams is 2, try again")

    return num_teams

'''
# Time: O() | # Space: O()
get_number_of_teams




Output(int): num_teams
'''

def get_team_names(num_teams):
    team_names = []

    for idx in range(num_teams):
        while True:
            team_name = input(f"Enter the name for team #{idx + 1}: ")
            num_words = len(team_name.split(" "))

            if num_words > 2:
                print("Team names may have at most 2 words, try again.")
            elif len(team_name) < 2:
                print("Team names must have at least 2 character, try again.")
            else:
                break

        team_names.append(team_name)

    return team_names

'''
# Time: O() | # Space: O()
get_number_of_teams




Output(int): num_teams
'''

def get_number_of_games_played(num_teams):
    while True:
        games_played = int(
            input("Enter the number of games played by each team: "))

        if games_played >= num_teams - 1:
            break

        print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")

    return games_played

'''
# Time: O() | # Space: O()
get_number_of_teams



Output(int): num_teams
'''

def get_team_wins(team_names, games_played):
    team_wins = []

    for team in team_names:
        while True:
            wins = int(input(f"Enter the number of wins Team {team} had: "))

            if wins > games_played:
                print(
                    f"The maximum number of wins is {games_played}, try again.")
            elif wins < 0:
                print("The minimum number of wins is 0, try again.")
            else:
                break

        team_wins.append((team, wins))

    return team_wins

def get_second_item(item):
    return item[1]

num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)

print("Generating the games to be played in the first round of the tournament...")
sorted_teams = sorted(team_wins, key=get_second_item)
game_pairings = []

games_to_make = len(sorted_teams)//2

for game_num in range(games_to_make):
    home_team = sorted_teams[game_num][0]
    away_team = sorted_teams[num_teams - 1 - game_num][0]
    game_pairings.append([home_team, away_team])

for pairing in game_pairings:
    home_team, away_team = pairing
    print(f"Home: {home_team} VS Away: {away_team}")