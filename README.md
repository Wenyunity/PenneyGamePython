# PenneyGamePython

Penney's Game involves two players picking a sequence of heads or tails. The original game uses sequences of three, although this program supports sequences of any length as well as sequences of unequal length.

The PenneyTournament file runs all possible pairs of sequences of length N against each other and finds each contestant's worst possible opponent.

## How To Read PenneyTournament Results
Each competitor can be referenced by a number between 0 and (2^length) - 1, and their index matches that number. The sequence is gotten by converting the number into binary and adding leading zeroes if necessary.

For example, with length=3, 5 is the sequence `['1', '0', '1']` and would be index 5 in each list.

- The Total Wins list shows how many wins they have against all opponents.
- The Worst Opponent list gives the number of the opponent that did best against them.
- The Wins vs. Worst list gives the number of wins the sequence got against their worst opponent.

For each matchup, the results are in Left Wins-Right Wins-Ties order, although ties are most likely impossible for sequences of the same length.

## To-Do

- Make an implementation of the actual game with AI as Player 1 or 2.
