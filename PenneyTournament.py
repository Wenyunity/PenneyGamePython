from Penney import PenneyGameFixedLength as Penney

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
    moreGamesNeeded = True
    ## Initalize player list
    playerList = list(range(players-1, -1, -1))
    while moreGamesNeeded:
        ## For each set of contestants
        winCount = [0]*players
        ## Play Game
        for i in range(rounds):
            winner = Penney(playerList, length)
            winCount[winner] += 1
        ## Result counting
        for idxPlay, valWin in enumerate(winCount):
            ## Add wins
            totalWins[playerList[idxPlay]] += valWin
            ## Worst Game Check
            if valWin < worstWins[playerList[idxPlay]]:
                worstWins[playerList[idxPlay]] = valWin
                worstGame[playerList[idxPlay]] = list(playerList)
        print("Game", playerList, "- Wins:", winCount)

        ## Find next set
        ## Add 1 to first contestant
        playerList[0] += 1
        for idx, val in enumerate(playerList):
            ## If we've reached overflow
            if idx + val >= 2**length:
                ## If this is the final contestant, we're done
                if idx + 1 == len(playerList):
                    moreGamesNeeded = False
                else: ## Add to the next contestant
                    playerList[idx+1] += 1
                    playerList[idx] = 0
        ## Backfill any previous contestants to their next legal state.
        for i in range(len(playerList)-2, -1, -1):
            if playerList[i] < playerList[i+1]:
                playerList[i] = playerList[i+1]+1
    ## Summary Results
    print("Total wins: ", totalWins)
    print("Worst game: ", worstGame)
    print("Wins in worst game: ", worstWins)

