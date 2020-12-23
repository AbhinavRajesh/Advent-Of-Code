def getDecks(file):
    deck1 = file[0].split('\n')[1:]
    deck2 = file[1].split('\n')[1:-1]
    deck1 = [int(i) for i in deck1]
    deck2 = [int(i) for i in deck2]
    return deck1, deck2

def solution1(deck1, deck2):
    while True:
        if len(deck1) <= 0 or len(deck2) <= 0:
            break
        card1 = deck1[0]
        card2 = deck2[0]
        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
            deck1.pop(0)
            deck2.pop(0)
        else:
            deck2.append(card2)
            deck2.append(card1)
            deck1.pop(0)
            deck2.pop(0)

def solution2(deck1, deck2) -> str:
    prevRound = []
    while len(deck1) != 0 and len(deck2) != 0:
        if (deck1, deck2) in prevRound:
            return 'p1'
        else:
            prevRound.append((deck1.copy(), deck2.copy()))
            p1 = deck1.pop(0)
            p2 = deck2.pop(0)
            if len(deck1) >= p1 and len(deck2) >= p2:
                winner = solution2(deck1.copy()[:p1], deck2.copy()[:p2])
                if winner == 'p1':
                    deck1.append(p1)
                    deck1.append(p2)
                else:
                    deck2.append(p2)
                    deck2.append(p1)

            else:
                if p1 > p2:
                    deck1.append(p1)
                    deck1.append(p2)
                elif p2 > p1:
                    deck2.append(p2)
                    deck2.append(p1)      
    return 'p2' if len(deck1) == 0 else 'p1'

def calculateScore(deck):
    score = 0
    deck.reverse()
    for i in range(1, len(deck) + 1):
        score += i * deck[i-1]        
    return score

def main():
    # Part 1
    file = open('input.txt', 'r').read().split('\n\n')
    deck1, deck2 = getDecks(file)
    solution1(deck1, deck2)
    print(f'Answer to Problem1: {calculateScore(deck1 if len(deck1) != 0 else deck2)}')
    # Part 2 
    deck1, deck2 = getDecks(file)
    winner = solution2(deck1, deck2)
    print(f'Answer to Problem2: {calculateScore(deck1 if winner == "p1" else deck2)}')
    
main()


