#!/usr/bin/python3
for i in range(0, 100, 1):
    f = int(i / 10)
    kl = int(i % 10)
    if f ==kl:
        continue
    if f > kl:
        continue
    if i == 89:
        print("{}{}".format(f, kl))
        break
    print("{}{}, ".format(f, kl), end="")
