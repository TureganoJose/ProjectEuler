from dataclasses import dataclass
from typing import List

@dataclass
class DataClassCard:
    rank: str
    suit: str

def is_OnePair(PlayerHand: List[DataClassCard]):
    CardRanks = [PlayerHand[0].rank , PlayerHand[1].rank , PlayerHand[2].rank , PlayerHand[3].rank , PlayerHand[4].rank  ]
    CardRanks = [Card if Card != 'T' else '10' for Card in CardRanks]
    CardRanks = [Card if Card!='J' else '11' for Card in CardRanks]
    CardRanks = [Card if Card != 'Q' else '12' for Card in CardRanks]
    CardRanks = [Card if Card != 'K' else '13' for Card in CardRanks]
    CardRanks = [Card if Card != 'A' else '14'  for Card in CardRanks]
    CardRanks = list(map(int, CardRanks))
    CardRanks.sort()

    CountingList = [0, 0, 0, 0, 0]
    for iCar,Card in enumerate(CardRanks):
        for jCar,CardJ in enumerate(CardRanks):
            if(Card==CardRanks[jCar]):
                CountingList[iCar]+=1

    count=0
    for iCar,NCards in enumerate(CountingList):
        if(NCards==2):
            count+=1;
    if(count==2):
        return True
    else:
        return False


def is_TwoPairs(PlayerHand: List[DataClassCard]):
    CardRanks = [PlayerHand[0].rank , PlayerHand[1].rank , PlayerHand[2].rank , PlayerHand[3].rank , PlayerHand[4].rank  ]
    CardRanks = [Card if Card != 'T' else '10' for Card in CardRanks]
    CardRanks = [Card if Card!='J' else '11' for Card in CardRanks]
    CardRanks = [Card if Card != 'Q' else '12' for Card in CardRanks]
    CardRanks = [Card if Card != 'K' else '13' for Card in CardRanks]
    CardRanks = [Card if Card != 'A' else '14'  for Card in CardRanks]
    CardRanks = list(map(int, CardRanks))
    CardRanks.sort()

    CountingList = [0, 0, 0, 0, 0]
    for iCar,Card in enumerate(CardRanks):
        for jCar,CardJ in enumerate(CardRanks):
            if(Card==CardRanks[jCar]):
                CountingList[iCar]+=1

    count=0
    for iCar,NCards in enumerate(CountingList):
        if(NCards==2):
            count+=1;
    if(count==4):
        return True
    else:
        return False


def is_ThreeofaKind(PlayerHand: List[DataClassCard]):
    CardRanks = [PlayerHand[0].rank , PlayerHand[1].rank , PlayerHand[2].rank , PlayerHand[3].rank , PlayerHand[4].rank  ]
    CardRanks = [Card if Card != 'T' else '10' for Card in CardRanks]
    CardRanks = [Card if Card!='J' else '11' for Card in CardRanks]
    CardRanks = [Card if Card != 'Q' else '12' for Card in CardRanks]
    CardRanks = [Card if Card != 'K' else '13' for Card in CardRanks]
    CardRanks = [Card if Card != 'A' else '14'  for Card in CardRanks]
    CardRanks = list(map(int, CardRanks))
    CardRanks.sort()

    CountingList = [0, 0, 0, 0, 0]
    for iCar,Card in enumerate(CardRanks):
        for jCar,CardJ in enumerate(CardRanks):
            if(Card==CardRanks[jCar]):
                CountingList[iCar]+=1

    count=0
    for iCar,NCards in enumerate(CountingList):
        if(NCards==3):
            count+=1;
    if(count==3):
        return True
    else:
        return False


def is_Straight(PlayerHand: List[DataClassCard]):
    CardRanks = [PlayerHand[0].rank , PlayerHand[1].rank , PlayerHand[2].rank , PlayerHand[3].rank , PlayerHand[4].rank  ]
    CardRanks = [Card if Card != 'T' else '10' for Card in CardRanks]
    CardRanks = [Card if Card!='J' else '11' for Card in CardRanks]
    CardRanks = [Card if Card != 'Q' else '12' for Card in CardRanks]
    CardRanks = [Card if Card != 'K' else '13' for Card in CardRanks]
    CardRanks = [Card if Card != 'A' else '14'  for Card in CardRanks]
    CardRanks = list(map(int, CardRanks))
    CardRanks.sort()
    SumConsequtive = 0
    for iCard,Card in enumerate(CardRanks):
        if iCard<4 and Card==CardRanks[iCard+1]+1 :
            SumConsequtive +=1
            if Card == 14 and CardRanks[iCard-1]==5 and CardRanks.__eq__([2,3,4,5,14]):
                return True
    if SumConsequtive==4:
        return True
    return False




def is_StraightFlush(PlayerHand: List[DataClassCard]):
    if PlayerHand[0].suit == PlayerHand[1].suit and PlayerHand[1].suit == PlayerHand[2].suit and  PlayerHand[2].suit == PlayerHand[3].suit and  PlayerHand[3].suit == PlayerHand[4].suit:
        CardRanks = [PlayerHand[0].rank , PlayerHand[1].rank , PlayerHand[2].rank , PlayerHand[3].rank , PlayerHand[4].rank  ]
        CardRanks = [Card if Card != 'T' else '10' for Card in CardRanks]
        CardRanks = [Card if Card!='J' else '11' for Card in CardRanks]
        CardRanks = [Card if Card != 'Q' else '12' for Card in CardRanks]
        CardRanks = [Card if Card != 'K' else '13' for Card in CardRanks]
        CardRanks = [Card if Card != 'A' else '14'  for Card in CardRanks]
        CardRanks = list(map(int, CardRanks))
        CardRanks.sort()
        SumConsequtive = 0
        for iCard, Card in enumerate(CardRanks):
            if iCard<4 and Card==CardRanks[iCard+1]+1:
                SumConsequtive +=1
            if Card == 14 and CardRanks[iCard-1]==5 and CardRanks.__eq__([2,3,4,5,14]):
                return True
        if SumConsequtive==4:
            return True
    return False

def is_FourKind(PlayerHand: List[DataClassCard]):
    CardRanks = [PlayerHand[0].rank, PlayerHand[1].rank, PlayerHand[2].rank, PlayerHand[3].rank, PlayerHand[4].rank]
    CardRanks = [Card if Card != 'T' else '10' for Card in CardRanks]
    CardRanks = [Card if Card != 'J' else '11' for Card in CardRanks]
    CardRanks = [Card if Card != 'Q' else '12' for Card in CardRanks]
    CardRanks = [Card if Card != 'K' else '13' for Card in CardRanks]
    CardRanks = [Card if Card != 'A' else '14' for Card in CardRanks]
    CardRanks = list(map(int, CardRanks))
    CardRanks.sort()
    if CardRanks[0] == CardRanks[1] and CardRanks[1] == CardRanks[2] and CardRanks[2] == CardRanks[3]:
        return True
    elif CardRanks[1] == CardRanks[2] and CardRanks[2] == CardRanks[3] and CardRanks[3] == CardRanks[4]:
        return True
    else:
        return False

def is_FullHouse(PlayerHand: List[DataClassCard]):
    CardRanks = [PlayerHand[0].rank, PlayerHand[1].rank, PlayerHand[2].rank, PlayerHand[3].rank, PlayerHand[4].rank]
    CardRanks = [Card if Card != 'T' else '10' for Card in CardRanks]
    CardRanks = [Card if Card != 'J' else '11' for Card in CardRanks]
    CardRanks = [Card if Card != 'Q' else '12' for Card in CardRanks]
    CardRanks = [Card if Card != 'K' else '13' for Card in CardRanks]
    CardRanks = [Card if Card != 'A' else '14' for Card in CardRanks]
    CardRanks = list(map(int, CardRanks))
    CardRanks.sort()
    if CardRanks[0] == CardRanks[1] and CardRanks[1] == CardRanks[2] and CardRanks[3] == CardRanks[4]:
        return True
    elif CardRanks[0] == CardRanks[1] and CardRanks[2] == CardRanks[3] and CardRanks[3] == CardRanks[4]:
        return True
    else:
        return False


def is_Flush(PlayerHand: List[DataClassCard]):
    CardRanks = [PlayerHand[0].rank , PlayerHand[1].rank , PlayerHand[2].rank , PlayerHand[3].rank , PlayerHand[4].rank  ]
    CardRanks = [Card if Card != 'T' else '10' for Card in CardRanks]
    CardRanks = [Card if Card!='J' else '11' for Card in CardRanks]
    CardRanks = [Card if Card != 'Q' else '12' for Card in CardRanks]
    CardRanks = [Card if Card != 'K' else '13' for Card in CardRanks]
    CardRanks = [Card if Card != 'A' else '14'  for Card in CardRanks]
    CardRanks = list(map(int, CardRanks))
    CardRanks.sort()
    if PlayerHand[0].suit == PlayerHand[1].suit and PlayerHand[1].suit == PlayerHand[2].suit and  PlayerHand[2].suit == PlayerHand[3].suit and  PlayerHand[3].suit == PlayerHand[4].suit:
        return True
    else:
        return False


def is_RoyalFlush(PlayerHand: List[DataClassCard]):
    if PlayerHand[0].suit == PlayerHand[1].suit and PlayerHand[1].suit == PlayerHand[2].suit and  PlayerHand[3].suit == PlayerHand[4].suit:
        CardRanks = [PlayerHand[0].rank , PlayerHand[1].rank , PlayerHand[2].rank , PlayerHand[3].rank , PlayerHand[4].rank  ]
        CardRanks = [Card if Card != 'T' else '10' for Card in CardRanks]
        CardRanks = [Card if Card!='J' else '11' for Card in CardRanks]
        CardRanks = [Card if Card != 'Q' else '12' for Card in CardRanks]
        CardRanks = [Card if Card != 'K' else '13' for Card in CardRanks]
        CardRanks = [Card if Card != 'A' else '14'  for Card in CardRanks]
        CardRanks = list(map(int, CardRanks))
        if sum(CardRanks)==60:
            return True
        else:
            return False
    else:
        return False


f = open("p054_poker.txt", "r")

# Jack 11
# Queen 12
# King 13
# Ace 1
count = 0
countdraws = 0

for line in f:

    Player1Card1 = DataClassCard(line[0], line[1])
    Player1Card2 = DataClassCard(line[3], line[4])
    Player1Card3 = DataClassCard(line[6], line[7])
    Player1Card4 = DataClassCard(line[9], line[10])
    Player1Card5 = DataClassCard(line[12], line[13])
    Player1Hand = [Player1Card1, Player1Card2, Player1Card3, Player1Card4, Player1Card5 ]
    Player2Card1 = DataClassCard(line[15], line[16])
    Player2Card2 = DataClassCard(line[18], line[19])
    Player2Card3 = DataClassCard(line[21], line[22])
    Player2Card4 = DataClassCard(line[24], line[25])
    Player2Card5 = DataClassCard(line[27], line[28])
    Player2Hand = [Player2Card1, Player2Card2, Player2Card3, Player2Card4, Player2Card5 ]

    #is_RoyalFlush(Player1Hand) #9
    #is_StraightFlush()    #8
    #is_FourKind()#7
    #is_FullHouse()#6
    #is_Flush()#5
    #is_Straight()#4
    #is_ThreeofaKind()#3
    #is_TwoPairs()#2
    #is_OnePair()#1


    if(is_RoyalFlush(Player1Hand)):
        Hand1Score=9
    elif(is_StraightFlush(Player1Hand)):
        Hand1Score=8
    elif(is_FourKind(Player1Hand)):
        Hand1Score=7
    elif(is_FullHouse(Player1Hand)):
        Hand1Score=6
    elif(is_Flush(Player1Hand)):
        Hand1Score=5
    elif(is_Straight(Player1Hand)):
        Hand1Score=4
    elif(is_ThreeofaKind(Player1Hand)):
        Hand1Score=3
    elif(is_TwoPairs(Player1Hand)):
        Hand1Score=2
    elif(is_OnePair(Player1Hand)):
        Hand1Score=1
    else:
        Hand1Score = 0

    if(is_RoyalFlush(Player2Hand)):
        Hand2Score=9
    elif(is_StraightFlush(Player2Hand)):
        Hand2Score=8
    elif(is_FourKind(Player2Hand)):
        Hand2Score=7
    elif(is_FullHouse(Player2Hand)):
        Hand2Score=6
    elif(is_Flush(Player2Hand)):
        Hand2Score=5
    elif(is_Straight(Player2Hand)):
        Hand2Score=4
    elif(is_ThreeofaKind(Player2Hand)):
        Hand2Score=3
    elif(is_TwoPairs(Player2Hand)):
        Hand2Score=2
    elif(is_OnePair(Player2Hand)):
        Hand2Score=1
    else:
        Hand2Score = 0




    if(Hand1Score>Hand2Score):
        count+=1
    elif(Hand1Score==Hand2Score): #Draw
        Card1Ranks = [Player1Hand[0].rank, Player1Hand[1].rank, Player1Hand[2].rank, Player1Hand[3].rank,
                         Player1Hand[4].rank]
        Card1Ranks = [Card if Card != 'T' else '10' for Card in Card1Ranks]
        Card1Ranks = [Card if Card != 'J' else '11' for Card in Card1Ranks]
        Card1Ranks = [Card if Card != 'Q' else '12' for Card in Card1Ranks]
        Card1Ranks = [Card if Card != 'K' else '13' for Card in Card1Ranks]
        Card1Ranks = [Card if Card != 'A' else '14' for Card in Card1Ranks]
        Card1Ranks = list(map(int, Card1Ranks))
        Card1Ranks.sort()

        Card2Ranks = [Player2Hand[0].rank, Player2Hand[1].rank, Player2Hand[2].rank, Player2Hand[3].rank,
                         Player2Hand[4].rank]
        Card2Ranks = [Card if Card != 'T' else '10' for Card in Card2Ranks]
        Card2Ranks = [Card if Card != 'J' else '11' for Card in Card2Ranks]
        Card2Ranks = [Card if Card != 'Q' else '12' for Card in Card2Ranks]
        Card2Ranks = [Card if Card != 'K' else '13' for Card in Card2Ranks]
        Card2Ranks = [Card if Card != 'A' else '14' for Card in Card2Ranks]
        Card2Ranks = list(map(int, Card2Ranks))
        Card2Ranks.sort()

        # is_RoyalFlush(Player1Hand) #9
        # is_StraightFlush()    #8
        # is_FourKind()#7
        # is_FullHouse()#6
        # is_Flush()#5
        # is_Straight()#4
        # is_ThreeofaKind()#3
        # is_TwoPairs()#2
        # is_OnePair()#1

        if(Hand1Score==0):
            iCard=0
            for iCard, Card in enumerate(Card1Ranks):
                if(Card1Ranks[4-iCard]>Card2Ranks[4-iCard]):
                    count+=1
                    break
                elif(Card1Ranks[4-iCard]<Card2Ranks[4-iCard]):
                    break
        elif(Hand1Score==1):
            iCard = 33


print(countdraws)
print(count)

