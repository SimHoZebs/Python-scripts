candidates = {}
ballot_content = []
voters_count = 0

def main():
    global candidates
    global ballot_content

    cases = int(input())

    for case in range(cases):
        #Repeat the code as many times as there are cases for it

        input()     #Empty input for spacing
        candidate_count = int(input())
        candidates = {input(): 0 for count in range(candidate_count)}

        while True:
            try:
                ballot_content.append([int(vote) for vote in input().split()])

                count_votes()
            except:
                break
        
        print(candidates)
        eliminate()

def count_votes():
    global ballot_content
    global candidates
    global voters_count

    for count, candidate in enumerate(candidates):
        candidates[candidate] = candidates[candidate] + ballot_content[voters_count][count]
    voters_count += 1

def eliminate():
    global voters_count
    global candidates
    candidate_count = len(candidates)

    breaking_point = (voters_count * (candidate_count + 1))/2
    print(breaking_point)
    for candidate in candidates:
        if candidates[candidate] <= breaking_point:
            print()
    pass
