#ADDREV

"""
Reverse Numbers, add them, reverse the sum and return.
Problem: https://www.spoj.com/problems/ADDREV/
"""

t = int(input())

q = 0
while q < t:
    q += 1
    i = input().split()

    #break into digits
    m = [digit for digit in i[0]]
    n = [digit for digit in i[1]]

    m_t = "".join(list(reversed(m)))
    n_t = "".join(list(reversed(n)))


    unreversed_sum = [digit for digit in str(int(int(m_t) + int(n_t)))]

    print("".join(list(reversed(unreversed_sum))).lstrip('0'))
