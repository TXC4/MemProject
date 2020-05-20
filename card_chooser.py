import random

quantity = 5
group = 'cards'
cardImageList = ["c01.png","c02.png","c03.png","c04.png","c05.png","c06.png","c07.png","c08.png","c09.png","c10.png","c11.png","c12.png","c13.png",
"d01.png","d02.png","d03.png","d04.png","d05.png","d06.png","d07.png","d08.png","d09.png","d10.png","d11.png","d12.png","d13.png",
"h01.png","h02.png","h03.png","h04.png","h05.png","h06.png","h07.png","h08.png","h09.png","h10.png","h11.png","h12.png","h13.png",
"s01.png","s02.png","s03.png","s04.png","s05.png","s06.png","s07.png","s08.png","s09.png","s10.png","s11.png","s12.png","s13.png"]

def createList(q):
    myList = []
    for i in range(q):
        myList.append(i)
    return myList

def shuffleCards(q, g):
    c = 0
    if g == 'decks':
        c = q * 52
        q = q * 52
    elif g == 'cards':
        c = q
        q = 52
    print("c", c, "q", q)
    temp = random.sample(createList(q), c)
    for i in range(c):
        print(i, ", ", temp[i] % 52)
        print(cardImageList[temp[i] % 52])

shuffleCards(quantity, group)
