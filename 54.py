import numpy as np
from numpy.core.defchararray import lstrip, rstrip
from collections import defaultdict

sf = [
    set("23456"),
    set("34567"),
    set("45678"),
    set("56789"),
    set("6789T"),
    set("789TJ"),
    set("89TJQ"),
    set("9TJQK"),
]

def value_giver(card):
    valstring = "23456789TJQKA"
    return valstring.index(card)

def max_card(arr):
    return sorted(arr, key=value_giver)[-1]


hands = np.genfromtxt("54.csv", delimiter=", ", dtype=np.str)
p1 = hands[:,:5]
p2 = hands[:,5:]
p1_vals = rstrip(p1, "CDHS")
p1_suites = lstrip(p1, "123456789TAKQJ")
p1_split = []
for i in range(int(p1.size / 5)):
    p1_split.append([p1_vals[i], p1_suites[i]])
p1 = np.array(p1_split)

p2_vals = rstrip(p2, "CDHS")
p2_suites = lstrip(p2, "123456789TAKQJ")
p2_split = []
for i in range(int(p2.size / 5)):
    p2_split.append([p2_vals[i], p2_suites[i]])
p2 = np.array(p2_split)





def is_flush(arr):
    return len(set(arr)) == 1

def is_royal_flush(arr):
    rf = set(["T", "J", "Q", "K", "A"])
    return set(arr) == rf

def is_straight(arr):
    return set(arr) in sf


def flush_parser(arr):
    if is_flush(arr[1]):
        if is_royal_flush(arr[0]):
            return ("RF", "A")
        high = max_card(arr[0])
        if is_straight(arr[0]):
            return ("SF", high)
        return ("FL", high)
    return None



def nonflush_parser(arr):
    hi = max_card(arr[0])
    vals = defaultdict(int)
    for i in arr[0]:
        vals[i] += 1
    # straight
    if is_straight(arr[0]):
        return ("ST", hi)
    # all unique, so high card
    if len(vals) == 5:
        return ("HC", hi)
    # 1 pair
    if len(vals) == 4:
        pair = None
        for k,v in vals.items():
            if v == 2:
                pair = k
        return ("PA", pair)
    # 3kind and 2pair
    if len(vals) == 3:
        stuff = []
        for k, v in vals.items():
            if v == 3:
                return ("TK", k)
            elif v == 2:
                stuff.append(k)
        return ("TP",max(stuff, key=value_giver))
    # now full house and four of a kind
    for k, v in vals.items():
        if v == 4:
            return ("FK", k)
        if v == 3:
            return ("FH", k)


def hand_parser(arr):
    result = flush_parser(arr)
    if not result:
        result = nonflush_parser(arr)
    return result
    


def hand_comparer(res1, res2):
    options = "HC PA TP TK ST FL FH FK SF RF".split(" ")
    h1 = options.index(res1[0])
    h2 = options.index(res2[0])
    if h1 > h2:
        return "p1"
    if h1 < h2:
        return "p2"
    if value_giver(res1[1]) > value_giver(res2[1]):
        return "p1"
    if value_giver(res1[1]) < value_giver(res2[1]):
        return "p2"
    return None

def fallback(i):
    h1 = sorted(p1[i][0], key=value_giver)[::-1]
    h2 = sorted(p2[i][0], key=value_giver)[::-1]
    for i, card in enumerate(h1):
        if value_giver(card) > value_giver(h2[i]):
            return "p1"
        
    return "p2"

wins = 0
for i, round in enumerate(p1):
    h1 = hand_parser(round)
    h2 = hand_parser(p2[i])
    result = hand_comparer(h1, h2)
    if not result:
        print(hands[i])
        print(h1, "\t\t", h2)
        result = fallback(i)
    if result == "p1":
        wins +=1
print(wins)