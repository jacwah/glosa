from sys import argv
from random import shuffle, random

def pairize(s):
    l = list(map(lambda z: z.strip(), s.split(",")))
    return l[0], l[1]

words = list(map(pairize, open(argv[1], "r")))
shuffle(words)

while words:
    ok = 0
    fails = []
    for w0, w1 in words:
        if random() <= 0.5:
            w0, w1 = w1, w0
        print(w0)
        x = input("> ").strip()
        if x == w1:
            ok += 1
            print("OK")
        else:
            print("NO: " + w1)
            fails.append((w0, w1))

    print(f"{ok} / {len(words)}")
    words = fails
