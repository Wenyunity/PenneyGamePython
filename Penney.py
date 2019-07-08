import collections as c
import random as rand

def PenneyGame(A, B):
    """Plays a round of Penney's Game.
    A coin is flipped multiple times until either sequence A or B comes up.
    Heads = '0'
    Tails = '1'

    A -- Player A's sequence of heads/tails (List)
    B -- Player B's sequence of heads/tails (List)
    Returns -1 if A wins, 0 if Draw, 1 if B wins
    """

    ## Create deque with maximum length equal to the greater of A and B
    ## This deque will be used to check if A/B has met their condition
    flips = c.deque("", max(len(A), len(B)))
    
    ## Fill Deque with filler
    for i in range(max(len(A), len(B))):
        flips.append(-20)

    ## Create list to record all flips
    ## This list does not check win conditions
    record = []

    winner = 0
    winnerDetermined = False
    ## Continually Flip Coins
    while winnerDetermined == False:
        ## Flip a coin
        coin = rand.choice(['0', '1'])
        ## Append to flips and record
        flips.append(coin)
        record.append(coin)
        ## Did A win?
        if list(flips)[max(len(B), len(A))-len(A):] == A:
            winnerDetermined = True
            winner -= 1
        ## Did B win?
        if list(flips)[max(len(B), len(A))-len(B):] == B:
            winnerDetermined = True
            winner += 1
    return winner

def PenneyGameFixedLength(playerList, length):
    """ 
    Plays a round of Penney's Game with the playerList given.
    A coin is flipped multiple times until any sequence in playerList is given.

    This version only supports sequences of the same length.
    Sequences are defined by integers; the binary interpretation of the sequence
    determines heads or tails.
    
    Returns the index of the player that won.
    """
    ## Number
    flipNumber = 0

    ## First length-1 flips (No possible winner)
    flipNumber = rand.randint(0, (2**length)-1)

    ## Flips with possible wins
    while True:
        ## Flip a coin and get rid of oldest flip
        flipNumber = ((flipNumber * 2) + rand.choice([0, 1])) % (2**length)
        ## Print sequence
        ## print(format(flipNumber, "0>" + str(length) + "b"))
        ## Check all coins for possible wins
        for idx, val in enumerate(playerList):
            if val == flipNumber:
                return idx
