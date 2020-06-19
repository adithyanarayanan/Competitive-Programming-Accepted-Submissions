#LASTDIG

"""
Given a and b - two numbers, what is the last digit of a^b?
Problem: https://www.spoj.com/problems/LASTDIG/
"""


t = int(input())

q = 0
while q < t:
    q +=1
    a, b  = input().split()

    if b == '0':
        print(1)
        continue
    if a == '0':
        print(0)
        continue
    if int(b)%4 == 0:
        print((int(a)**(4))%10)
        continue

    print((int(a)**(int(b)%4))%10)
