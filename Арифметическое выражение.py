def into_postfix(stroka):
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    priority = {'+': 0, '-': 0, '*': 1, '/': 1, '(': 2, ')': 2, '^': 2}
    postif_input = []
    __postfix__ = []
    ERROR = False
    number = ''
    for i in stroka:
        if i == ' ':
            ERROR = True
            continue
        if i in numbers:
            if ERROR and number != '':
                return 911 / 0 #throwing an error
            number += i
            ERROR = False
        else:
            if number != '':
                postif_input.append(int(number))
            number = ''
            while __postfix__ != [] and priority[__postfix__[-1]] >= priority[i] and i != ')' and i != '(' and \
                    __postfix__[-1] != '(':
                if __postfix__[-1] == '^' and i == '^':
                    break
                postif_input += __postfix__[-1]
                __postfix__.pop()
            __postfix__.append(i)
            if i == ')':
                __postfix__.pop()
                while __postfix__[-1] != '(':
                    postif_input.append(__postfix__[-1])
                    __postfix__.pop()
                __postfix__.pop()
    if number != '':
        postif_input.append(int(number))
    while __postfix__ != []:
        postif_input.append(__postfix__[-1])
        __postfix__.pop()
    return postif_input

def get_answer(postfix_input):
    answer = 0
    i = 0
    while len(postfix_input) != 1:
        if postfix_input[i] == '*':
            answer = postfix_input[i - 2] * postfix_input[i - 1]
            postfix_input.pop(i)
            postfix_input.pop(i - 1)
            postfix_input[i - 2] = answer
            i = 0
        elif postfix_input[i] == '/':
            answer = postfix_input[i - 2] / postfix_input[i - 1]
            postfix_input.pop(i)
            postfix_input.pop(i - 1)
            postfix_input[i - 2] = answer
            i = 0
        elif postfix_input[i] == '+':
            answer = postfix_input[i - 2] + postfix_input[i - 1]
            postfix_input.pop(i)
            postfix_input.pop(i - 1)
            postfix_input[i - 2] = answer
            i = 0
        elif postfix_input[i] == '-':
            answer = postfix_input[i - 2] - postfix_input[i - 1]
            postfix_input.pop(i)
            postfix_input.pop(i - 1)
            postfix_input[i - 2] = answer
            i = 0
        else:
            i += 1
    return postfix_input[0]

to_eval = input()
try:
    print(get_answer(into_postfix(to_eval)))
except:
    print("WRONG INPUT")




