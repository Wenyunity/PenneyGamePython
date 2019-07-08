from Penney import PenneyGameFixedLength as Penney
from itertools import combinations as comb

def PenneyTournament(length=3, rounds=1000, players=2):
    """Plays Penney's Game using all possible combinations
    of the specified length.
    The number of players determined will play the amount of rounds specified.

    length -- Length of each string.
    rounds -- Number of rounds each player plays.
    players -- How many players participate in a game.
    """

    ## Initialize items
    totalWins = [0]*(2**length)
    worstGame = [-1]*(2**length)
    worstWins = [rounds+1]*(2**length)

    ## Go through all combinations
    bracket = list(comb(range(2**length), players))
    for idx, val in enumerate(bracket):
        ## For each set of contestants
        winCount = [0]*players
        ## Play Game
        for i in range(rounds):
            winner = Penney(val, length)
            winCount[winner] += 1
        ## Result counting
        for idxPlay, valWin in enumerate(winCount):
            ## Add wins
            totalWins[val[idxPlay]] += valWin
            if valWin < worstWins[val[idxPlay]]:
                worstWins[val[idxPlay]] = valWin
                worstGame[val[idxPlay]] = val
        print("Game", val, "- Wins:", winCount)
    print("Total wins: ", totalWins)
    print("Worst game: ", worstGame)
    print("Wins in worst game: ", worstWins)
