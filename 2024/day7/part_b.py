file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day7/input.txt"
alphabet = "AKQT98765432J"


class Hand():

    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid
        self.type = find_type(cards)

    def __str__(self):
        return f'hand: {self.cards}, bid: {self.bid}, type: {self.type}'


def find_type(cards):
    d = {}
    for card in cards:
        if card in d:
            d[card] += 1
        else:
            d[card] = 1
    if "J" in cards and d["J"] < 5:
        del d['J']
        m = max(d.values())
        l = sorted(d.keys(), key=lambda s: [alphabet.index(c) for c in s])
        for letter in l :
            if d[letter] == m:
                cards = cards.replace("J", letter)
        d = {}
        for card in cards:
            if card in d:
                d[card] += 1
            else:
                d[card] = 1

    keys = len(d.keys())
    if keys == 1:
        return 1
    elif keys == 2:
        if list(d.values())[0] in [1, 4]:
            return 2
        else:
            return 3
    elif keys == 3:
        for v in d.values():
            if v == 3:
                return 4
        return 5
    elif keys == 4:
        return 6
    else:
        return 7

def run():
    sum = 0
    with open(file_name) as f:
        lines = f.readlines()
        res = dict(zip(list(range(1, 8)),[[],[],[],[],[],[],[]]))
        rank = len(lines)
        for line in lines:
            cards, bid = line.split(" ")
            hand = Hand(cards, int(bid))
            res[hand.type].append(hand)


        for k,v in res.items():
            l = sorted(v, key=lambda hand: [alphabet.index(c) for c in hand.cards])
            for hand in l:
                sum+= hand.bid * rank
                rank -=1

        print(sum)

run()