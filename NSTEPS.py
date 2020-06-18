#NSTEPS

"""
Given a x,y coordinate value, print the number that is written at that coordinate when it follows a given patter depicted in the link below.
Problem: https://www.spoj.com/problems/NSTEPS/

"""

t = int(input())

q = 0
while q < t:
    q +=1
    xy = input().split()
    x = int(xy[0])
    y = int(xy[1])


    if (y > x) or (x- y > 2):
        print("No Number")
        continue

    if (x == 1) and (y == 0):
        print("No Number")
        continue


    if x == y:
        if x%2 == 1:
            print(x + y -1)
        else:
            print(x + y)
            continue
    else:
        if (x-y == 1):
            print("No Number")
            continue
        if y%2 == 1:
            print(1 + (y*2))
        else:

            print(2 + (y*2))
