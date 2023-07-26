'''tournament_winner.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0200

'''
Question:
# team compete against each other in a round robin
# home and away team
# [homeTeam, awayTeam]
# 1, home team won
# 0, away team won
# one winner and loser
# no ties
# winning team receives 3 points
# team name < 30 chars

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

Input:
- Intuitive
- Primitive Types
	- Strings
		- Empty string
		- NULL or nil (and Optionals, depending on language)
		- Spaces (multiple words or sentences, or single/multiple whitespaces alone)
		- Punctuation
		- Upper, lowercase, or mixed (e.g., “stRiNg”)
		- Strings of numbers (e.g., “12”) Should these be changed to Int, Float, or Double?
		- Different Languages (Diacritics? Unicode compliant? ASCII?)
		- Emoji 👍 (especially if question is presented as a text field input by a user)
		- Long String
'''
# Time: O(n) | # Space: O(k)
def tournamentWinner(competitions, results):
    results_dict = {}
    winner = 0

    for competition in range(len(competitions)):
        home_team = competitions[competition][1]
        away_team = competitions[competition][0]
        if home_team not in results_dict:
            results_dict[home_team] = 0
        if away_team not in results_dict:
            results_dict[away_team] = 0

        if results[competition] == 1:
            results_dict[home_team] += 1
            if results_dict[home_team] > winner:
                winner = results_dict[home_team]
        if results[competition] == 0:
            results_dict[away_team] += 1
            if results_dict[away_team] > winner:
                winner = results_dict[away_team]

    for team, result in results_dict.items():
        print("team:", team)
        print("result:", result)
        if result == winner:
            return team


competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]
results = [0, 0, 1]
print("competitions:", competitions)
print("results:", results)
print("tournamentWinner:", tournamentWinner(competitions, results))
print(" ")

competitions = [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"],
    ["C#", "Python"],
    ["Java", "C#"],
    ["C#", "HTML"],
    ["SQL", "C#"],
    ["HTML", "SQL"],
    ["SQL", "Python"],
    ["SQL", "Java"]
]
results = [0, 1, 1, 1, 0, 1, 0, 1, 1, 0]
print("competitions:", competitions)
print("results:", results)
print("tournamentWinner:", tournamentWinner(competitions, results))
print(" ")

competitions = [
    ["Bulls", "Eagles"],
    ["Bulls", "Bears"],
    ["Bears", "Eagles"]
]
results = [0, 1, 1, 1, 0, 1]
print("competitions:", competitions)
print("results:", results)
print("tournamentWinner:", tournamentWinner(competitions, results))
print(" ")
