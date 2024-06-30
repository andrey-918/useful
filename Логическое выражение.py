def into_postfix(stroka):
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    priority = {'|': 0, '^': 0,  '&': 1, '!': 2, '(': 3, ')': 3}
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
                return 7 / 0
            number += i
            ERROR = False
        else:
            if number != '':
                postif_input.append(int(number))
            number = ''
            while __postfix__ != [] and priority[__postfix__[-1]] >= priority[i] and i != ')' and i != '(' and \
                    __postfix__[-1] != '(':
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
    i = 0
    while len(postfix_input) != 1:
        if postfix_input[i] == '&':
            answer = ((postfix_input[i - 2] * postfix_input[i - 1]) != 0) * 1
            postfix_input.pop(i)
            postfix_input.pop(i - 1)
            postfix_input[i - 2] = answer
            i = 0
        elif postfix_input[i] == '|':
            answer = ((postfix_input[i - 2] + postfix_input[i - 1]) != 0) * 1
            postfix_input.pop(i)
            postfix_input.pop(i - 1)
            postfix_input[i - 2] = answer
            i = 0
        elif postfix_input[i] == '!':
            answer = postfix_input[i - 1] == 0
            postfix_input.pop(i)
            postfix_input[i - 1] = answer
            i = 0
        elif postfix_input[i] == '^':
            answer = ((postfix_input[i - 2] * postfix_input[i - 1]) == 0) * ((postfix_input[i - 1] + postfix_input[i - 2]))
            postfix_input.pop(i)
            postfix_input.pop(i - 1)
            postfix_input[i - 2] = answer
            i = 0
        else:
            i += 1
    return postfix_input[0]

to_eval = input()
print(int(get_answer(into_postfix(to_eval))))
