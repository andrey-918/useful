{\rtf1\ansi\ansicpg1251\cocoartf2758
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red191\green100\blue38;\red32\green32\blue32;\red254\green187\blue91;
\red153\green168\blue186;\red117\green114\blue185;\red86\green132\blue173;}
{\*\expandedcolortbl;;\csgenericrgb\c74902\c39216\c14902;\csgenericrgb\c12549\c12549\c12549;\csgenericrgb\c99608\c73333\c35686;
\csgenericrgb\c60000\c65882\c72941;\csgenericrgb\c45882\c44706\c72549;\csgenericrgb\c33725\c51765\c67843;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs60 \cf2 \cb3 def \cf4 partition\cf5 (a):\
    less = []\
    more = []\
    \cf2 if \cf6 len\cf5 (a) < \cf7 2\cf5 : \cf2 return \cf5 a\
    x = (\cf6 min\cf5 (a) + \cf6 max\cf5 (a)) / \cf7 2\
    \cf2 if \cf6 min\cf5 (a) == \cf6 max\cf5 (a): \cf2 return \cf5 a\
    \cf2 for \cf5 i \cf2 in \cf5 a:\
        \cf2 if \cf5 i < x:\
            less.append(i)\
        \cf2 else\cf5 :\
            more.append(i)\
    less = partition(less)\
    more = partition(more)\
    \cf2 return \cf5 less + more\
\cf6 print\cf5 (*partition(\cf6 list\cf5 (\cf6 map\cf5 (\cf6 int\cf2 , \cf6 input\cf5 ().split()))))\
}