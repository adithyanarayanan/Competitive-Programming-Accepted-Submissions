#ONP- Reverse Polish Notation with Brackets - aided by Editorial https://spojeditorials.wordpress.com/2016/09/22/onp-transform-the-expression/


"""
Takes a string input expression and returns the Reverse Polish Notation of the Expression
Problem Description at https://www.spoj.com/problems/ONP/
"""


def print_rpn(str):
    notations = set(['+', '-', '/', '*', '^', '('])
    sol_stack = []
    sol_string = ""
    for char in str:
        if char in notations:
            sol_stack.append(char)
        elif char == ')':
            while True:
                op = sol_stack.pop()
                if op == '(':
                    break
                else:
                    sol_string = sol_string + op
        else:
            sol_string = sol_string + char

    print(sol_string)



t = int(input())

q = 0
while q < t:
    q += 1
    current_inp = input()
    print_rpn(current_inp)
