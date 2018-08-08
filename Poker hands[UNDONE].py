poker_desk = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13,"A":14}

def pokerdesk(PlayerCards):
    cards = PlayerCards.split()
    for card in cards:
        nmbr = card[0]
        card = str(poker_desk[nmbr]) + card[1]
        print card
    print cards
        
def poker(cards):
    cards = "5H 5C 6S 7S KD 2C 3S 8S 8D TD".split()
    P1_cards = " ".join(cards[:5])
    P2_cards = " ".join(cards[5:])
    pokerdesk(P1_cards)



#with open("poker.txt") as f:
    #for line in f.readlines():
        #poker(cards)
poker("hi")
            
        
        
        
