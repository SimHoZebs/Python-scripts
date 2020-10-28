answers = []
#contains list 'winners', which contain 1 or more 'wiiner'
ballot = []
#contains list 'voters', which contains 'candidates' sorted by 'rank'.
candidates = {}

def main():
    global answers, ballot, candidates

    candidates = {input(): 0 for _ in range(int(input()))}
    ballot = get_votes()
    candidates = count_votes()

    break_point = (len(ballot))/2
    #print("Breakpoint:", break_point)
    winners = winner_names(break_point)

    while len(winners) < 1:
        eliminate()
        candidates = count_votes()
        winners = winner_names(break_point)

    answers.append(winners)

def get_votes():
    global candidates
    temp_ballot = []

    while True:
        voted_ranks = [int(rank) for rank in input().split()]

        if len(voted_ranks) < 1:
            #Catches EOL/ \n input
            break

        voter = [0 for i in candidates]
        for candidate, rank in zip(candidates, voted_ranks):
            voter[rank - 1] = candidate
        
        temp_ballot.append(voter)
    
    return temp_ballot

def count_votes():
    global ballot, candidates
    temp_candidates = {candidate: 0 for candidate in candidates.keys()}

    for voter in ballot:
        temp_candidates[voter[0]] += 1
    
    #print("Candidates", temp_candidates)
    return temp_candidates

def winner_names(break_point):
    global candidates, ballot
    winner = []

    highest_votes = max(list(candidates.values()))

    if highest_votes > break_point:
        for candidate, score in candidates.items():
            if score == highest_votes:
                winner = [candidate]
                break
    elif highest_votes == len(ballot)/len(candidates):
        winner = list(candidates.keys())

    #print("Winner is", winner)
    return winner

def eliminate():
    global candidates, ballot
    lowest_votes = min(list(candidates.values()))
    eliminated = []

    eliminated = [candidate for candidate, score in candidates.items() if score == lowest_votes]
    
    for candidate in eliminated:
        candidates.pop(candidate)
        for voter in ballot:
            voter.remove(candidate)
    
    #print("Eliminated", eliminated)

if __name__ == "__main__":

    test_case = int(input())
    input()     #space after case input
    for _ in range(test_case):
        main()
    
    for winners in answers:
        print()
        if len(winners) == 1:
            print(winners[0])
        else:
            for winner in winners:
                print(winner)