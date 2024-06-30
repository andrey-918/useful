{\rtf1\ansi\ansicpg1251\cocoartf2758
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red191\green100\blue38;\red32\green32\blue32;\red254\green187\blue91;
\red153\green168\blue186;\red117\green114\blue185;\red86\green132\blue173;}
{\*\expandedcolortbl;;\csgenericrgb\c74902\c39216\c14902;\csgenericrgb\c12549\c12549\c12549;\csgenericrgb\c99608\c73333\c35686;
\csgenericrgb\c60000\c65882\c72941;\csgenericrgb\c45882\c44706\c72549;\csgenericrgb\c33725\c51765\c67843;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs60 \cf2 \cb3 def \cf4 answer\cf5 (a\cf2 , \cf5 b):\
    ans = []\
    n1 = \cf6 len\cf5 (a)\
    n2 = \cf6 len\cf5 (b)\
    i\cf2 , \cf5 j = \cf7 0\cf2 , \cf7 0\
    \cf2 while \cf5 i < n1 \cf2 or \cf5 j < n2:\
        \cf2 if \cf5 i >= n1:\
            ans.append(b[j])\
            j += \cf7 1\
        \cf2 elif \cf5 j >= n2:\
            ans.append(a[i])\
            i += \cf7 1\
        \cf2 else\cf5 :\
            \cf2 if \cf5 a[i] < b[j]:\
                ans.append(a[i])\
                i += \cf7 1\
            \cf2 else\cf5 :\
                ans.append(b[j])\
                j += \cf7 1\
    \cf2 return \cf5 ans\
\
\
\cf2 def \cf4 dooo\cf5 (a):\
    first = []\
    second = []\
    \cf2 if \cf6 len\cf5 (a) < \cf7 2\cf5 : \cf2 return \cf5 a\
    \cf2 for \cf5 i \cf2 in \cf6 range\cf5 (\cf6 len\cf5 (a)):\
        \cf2 if \cf5 i % \cf7 2 \cf5 == \cf7 0\cf5 :\
            first.append(a[i])\
        \cf2 else\cf5 :\
            second.append(a[i])\
    \cf2 return \cf5 answer(dooo(first)\cf2 , \cf5 dooo(second))\
\
\
\
\
\
n1 = \cf6 int\cf5 (\cf6 input\cf5 ())\
a = \cf6 list\cf5 (\cf6 map\cf5 (\cf6 int\cf2 , \cf6 input\cf5 ().split()))\
\cf6 print\cf5 (*dooo(a))\
}