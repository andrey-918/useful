{\rtf1\ansi\ansicpg1251\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red195\green123\blue90;\red23\green23\blue26;\red71\green149\blue242;
\red174\green176\blue183;\red89\green158\blue96;\red38\green157\blue169;\red103\green107\blue114;\red117\green114\blue185;
\red92\green96\blue103;}
{\*\expandedcolortbl;;\csgenericrgb\c76471\c48235\c35294;\csgenericrgb\c9020\c9020\c10196;\csgenericrgb\c27843\c58431\c94902;
\csgenericrgb\c68235\c69020\c71765;\csgenericrgb\c34902\c61961\c37647;\csgenericrgb\c14902\c61569\c66275;\csgenericrgb\c40392\c41961\c44706;\csgenericrgb\c45882\c44706\c72549;
\csgenericrgb\c36078\c37647\c40392;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs26 \cf2 \cb3 def \cf4 into_postfix\cf5 (stroka):\
    numbers = [\cf6 "1"\cf5 , \cf6 "2"\cf5 , \cf6 "3"\cf5 , \cf6 "4"\cf5 , \cf6 "5"\cf5 , \cf6 "6"\cf5 , \cf6 "7"\cf5 , \cf6 "8"\cf5 , \cf6 "9"\cf5 , \cf6 "0"\cf5 ]\
    priority = \{\cf6 '+'\cf5 : \cf7 0\cf5 , \cf6 '-'\cf5 : \cf7 0\cf5 , \cf6 '*'\cf5 : \cf7 1\cf5 , \cf6 '/'\cf5 : \cf7 1\cf5 , \cf6 '('\cf5 : \cf7 2\cf5 , \cf6 ')'\cf5 : \cf7 2\cf5 , \cf6 '^'\cf5 : \cf7 2\cf5 \}\
    postif_input = []\
    __postfix__ = []\
    ERROR = \cf2 False\
    \cf5 number = \cf6 ''\
    \cf2 for \cf5 i \cf2 in \cf5 stroka:\
        \cf2 if \cf5 i == \cf6 ' '\cf5 :\
            ERROR = \cf2 True\
            continue\
        if \cf5 i \cf2 in \cf5 numbers:\
            \cf2 if \cf5 ERROR \cf2 and \cf5 number != \cf6 ''\cf5 :\
                \cf2 return \cf7 911 \cf5 / \cf7 0 \cf8 #throwing an error\
            \cf5 number += i\
            ERROR = \cf2 False\
        else\cf5 :\
            \cf2 if \cf5 number != \cf6 ''\cf5 :\
                postif_input.append(\cf9 int\cf5 (number))\
            number = \cf6 ''\
            \cf2 while \cf5 __postfix__ != [] \cf2 and \cf5 priority[__postfix__[-\cf7 1\cf5 ]] >= priority[i] \cf2 and \cf5 i != \cf6 ')' \cf2 and \cf5 i != \cf6 '(' \cf2 and \cf5 \\\
                    __postfix__[-\cf7 1\cf5 ] != \cf6 '('\cf5 :\
                \cf2 if \cf5 __postfix__[-\cf7 1\cf5 ] == \cf6 '^' \cf2 and \cf5 i == \cf6 '^'\cf5 :\
                    \cf2 break\
                \cf5 postif_input += __postfix__[-\cf7 1\cf5 ]\
                __postfix__.pop()\
            __postfix__.append(i)\
            \cf2 if \cf5 i == \cf6 ')'\cf5 :\
                __postfix__.pop()\
                \cf2 while \cf5 __postfix__[-\cf7 1\cf5 ] != \cf6 '('\cf5 :\
                    postif_input.append(__postfix__[-\cf7 1\cf5 ])\
                    __postfix__.pop()\
                __postfix__.pop()\
    \cf2 if \cf5 number != \cf6 ''\cf5 :\
        postif_input.append(\cf9 int\cf5 (number))\
    \cf2 while \cf5 __postfix__ != []:\
        postif_input.append(__postfix__[-\cf7 1\cf5 ])\
        __postfix__.pop()\
    \cf2 return \cf5 postif_input\
\
\cf2 def \cf4 get_answer\cf5 (postfix_input):\
    \cf10 answer \cf5 = \cf7 0\
    \cf5 i = \cf7 0\
    \cf2 while \cf9 len\cf5 (postfix_input) != \cf7 1\cf5 :\
        \cf2 if \cf5 postfix_input[i] == \cf6 '*'\cf5 :\
            answer = postfix_input[i - \cf7 2\cf5 ] * postfix_input[i - \cf7 1\cf5 ]\
            postfix_input.pop(i)\
            postfix_input.pop(i - \cf7 1\cf5 )\
            postfix_input[i - \cf7 2\cf5 ] = answer\
            i = \cf7 0\
        \cf2 elif \cf5 postfix_input[i] == \cf6 '/'\cf5 :\
            answer = postfix_input[i - \cf7 2\cf5 ] / postfix_input[i - \cf7 1\cf5 ]\
            postfix_input.pop(i)\
            postfix_input.pop(i - \cf7 1\cf5 )\
            postfix_input[i - \cf7 2\cf5 ] = answer\
            i = \cf7 0\
        \cf2 elif \cf5 postfix_input[i] == \cf6 '+'\cf5 :\
            answer = postfix_input[i - \cf7 2\cf5 ] + postfix_input[i - \cf7 1\cf5 ]\
            postfix_input.pop(i)\
            postfix_input.pop(i - \cf7 1\cf5 )\
            postfix_input[i - \cf7 2\cf5 ] = answer\
            i = \cf7 0\
        \cf2 elif \cf5 postfix_input[i] == \cf6 '-'\cf5 :\
            answer = postfix_input[i - \cf7 2\cf5 ] - postfix_input[i - \cf7 1\cf5 ]\
            postfix_input.pop(i)\
            postfix_input.pop(i - \cf7 1\cf5 )\
            postfix_input[i - \cf7 2\cf5 ] = answer\
            i = \cf7 0\
        \cf2 else\cf5 :\
            i += \cf7 1\
    \cf2 return \cf5 postfix_input[\cf7 0\cf5 ]\
\
to_eval = \cf9 input\cf5 ()\
\cf2 try\cf5 :\
    \cf9 print\cf5 (get_answer(into_postfix(to_eval)))\
\cf2 except\cf5 :\
    \cf9 print\cf5 (\cf6 "WRONG INPUT"\cf5 )\
\
\
\
\
}