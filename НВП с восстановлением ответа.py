{\rtf1\ansi\ansicpg1251\cocoartf2758
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 A = int(input())\
numbers = list(map(int, input().split()))\
dp = \{\}\
prev = \{\}\
answer = 0\
for i in range(len(numbers)):\
    number = numbers[i]\
    dp[i] = 0\
    prev[i] = -1\
    for j in dp:\
        if number > numbers[j] and dp[j] > dp[i]:\
            dp[i] = dp[j]\
            prev[i] = j\
    dp[i] += 1\
    if dp[i] > dp[answer]:\
        answer = i\
answer_list = []\
answer_list.append(numbers[answer])\
while prev[answer] != -1:\
    answer = prev[answer]\
    answer_list.append(numbers[answer])\
answer_list.reverse()\
for i in answer_list:\
    print(i, end = ' ')\
#4 8 2 6 2 10 6 29 30 58 9}