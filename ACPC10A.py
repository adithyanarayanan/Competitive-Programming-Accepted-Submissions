#ACPC10A - What’s Next - SPOJ

"""
Find the next number in an AP or a GP after identifying it as such
Problem: https://www.spoj.com/problems/ACPC10A/
"""


while True:
    inp = input()

    if inp == "0 0 0":
        break


    a, b, c = inp.split()

    b = int(b)
    c = int(c)
    if (c - b) == (b - int(a)):
        print("AP", c + (c-b))
        continue

    print("GP", int(c*(c/b)))
