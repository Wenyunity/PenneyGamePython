from Penney import PenneyGame as Penney

def PenneyTournament(length=3, rounds=1000):
    """Plays Penney's Game using all strings of the specified length.
    Each pair will play the amount of rounds specified.

    length -- Length of each string.
    rounds -- Number of rounds each player plays.
    """
    contestants = []
    totalWins = []
    totalTies = []
    worstOpponent = []
    worstWins = []
    
    ## Initialize all contestants
    for i in range(2**length):
        """Uses binary to initalize each contestant..
        Format gives a binary string with the desired number of leading 0's.
        List takes each character from a string for its list.
        """
        contestants.append(list(format(i, "0>" + str(length) + "b")))
        totalWins.append(0)
        totalTies.append(0)
        worstOpponent.append(-1)
        worstWins.append(1000)

    ## Play games between each pair
    for i in range(2**length):
        for j in range(i+1, 2**length):
            winsA = 0
            winsB = 0
            ties = 0
            for k in range(rounds):
                ## Play game
                winner = Penney(contestants[i], contestants[j])
                ## Add to the appropriate winner
                if winner == -1:
                    winsA += 1
                if winner == 0:
                    ties += 1
                if winner == 1:
                    winsB += 1
            ## Add scores
            totalWins[i] += winsA
            totalWins[j] += winsB
            totalTies[i] += ties
            totalTies[j] += ties
            ## Find if this matchup was the worst so far
            ## If so, update worst wins and worst competitor
            if worstWins[i] > winsA:
                worstWins[i] = winsA
                worstOpponent[i] = j
            if worstWins[j] > winsB:
                worstWins[j] = winsB
                worstOpponent[j] = i
            ## Print results
            print(contestants[i], " vs. ", contestants[j],
                  " Result: ", winsA, "-", winsB, "-", ties)
    ## Print total results
    print("Total Wins: ", totalWins)
    print("Worst Competitor: ", worstOpponent)
    print("Wins vs. Worst: ", worstWins)
