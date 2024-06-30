{\rtf1\ansi\ansicpg1251\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\fmodern\fcharset0 Courier-Bold;\f2\fmodern\fcharset0 Courier-Oblique;
}
{\colortbl;\red255\green255\blue255;\red109\green111\blue5;\red15\green112\blue3;\red0\green0\blue109;
\red14\green110\blue109;\red41\green15\blue109;\red0\green0\blue254;\red109\green109\blue109;}
{\*\expandedcolortbl;;\csgenericrgb\c42745\c43529\c1961;\csgenericrgb\c5882\c43922\c1176;\csgenericrgb\c0\c0\c42745;
\csgenericrgb\c5490\c43137\c42745;\csgenericrgb\c16078\c5882\c42745;\csgenericrgb\c0\c0\c99608;\csgenericrgb\c42745\c42745\c42745;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs40 \cf2 #include 
\f1\b \cf3 <iostream>\

\f0\b0 \cf2 #include 
\f1\b \cf3 <set>\

\f0\b0 \cf2 #include 
\f1\b \cf3 <vector>\
\cf4 using namespace 
\f0\b0 \cf5 std\cf0 ;\

\f1\b \cf4 using 
\f0\b0 \cf6 ull \cf0 = 
\f1\b \cf4 unsigned long long
\f0\b0 \cf0 ;\
\cf6 ull \cf0 find_summ(\cf5 set\cf0 <\cf5 vector\cf0 <
\f1\b \cf4 int
\f0\b0 \cf0 >>& a, 
\f1\b \cf4 const int 
\f0\b0 \cf0 number) \{\
    \cf5 vector\cf0 <
\f1\b \cf4 int
\f0\b0 \cf0 > new_one;\
    
\f1\b \cf4 int 
\f0\b0 \cf0 finding = \cf7 2\cf0 ;\
    \cf6 ull \cf0 answer = \cf7 1\cf0 ;\
    
\f1\b \cf4 while 
\f0\b0 \cf0 (finding <= number) \{\
        
\f1\b \cf4 for 
\f0\b0 \cf0 (\cf5 vector\cf0 <
\f1\b \cf4 int
\f0\b0 \cf0 > x: a) \{\
            
\f1\b \cf4 if 
\f0\b0 \cf0 (x.size() > finding - \cf7 1 \cf0 && x\cf5 [\cf0 finding - \cf7 1\cf5 ] \cf0 == \cf7 1\cf0 ) \{\
                new_one \cf5 = \cf0 \{x.begin() \cf5 + \cf0 finding, x.end()\};\
                new_one.push_back(finding);\
                ++answer;\
                a.insert(new_one);\
            \}\
            
\f1\b \cf4 else continue
\f0\b0 \cf0 ;\
        \}\
        ++finding;\
    \}\
    
\f1\b \cf4 return 
\f0\b0 \cf0 answer;\
\}\

\f1\b \cf4 void 
\f0\b0 \cf0 ready(\cf5 set\cf0 <\cf5 vector\cf0 <
\f1\b \cf4 int
\f0\b0 \cf0 >>& a, 
\f1\b \cf4 int 
\f0\b0 \cf0 number)\{\
    \cf5 vector \cf0 <
\f1\b \cf4 int
\f0\b0 \cf0 > line;\
    
\f1\b \cf4 for 
\f0\b0 \cf0 (
\f1\b \cf4 int 
\f0\b0 \cf0 i = \cf7 0\cf0 ; i != number; ++i) \{\
        line.push_back(\cf7 1\cf0 );\
    \}\
    a.insert(line);\
\
\}\

\f1\b \cf4 void 
\f0\b0 \cf0 out(
\f1\b \cf4 const 
\f0\b0 \cf5 set\cf0 <\cf5 vector\cf0 <
\f1\b \cf4 int
\f0\b0 \cf0 >>& a)\{\
    
\f1\b \cf4 for 
\f0\b0 \cf0 (
\f1\b \cf4 const 
\f0\b0 \cf5 vector\cf0 <
\f1\b \cf4 int
\f0\b0 \cf0 >& x: a)\{\
        
\f1\b \cf4 for 
\f0\b0 \cf0 (
\f1\b \cf4 int 
\f0\b0 \cf0 y: x) cout \cf5 << \cf0 y \cf5 << 
\f1\b \cf3 " "
\f0\b0 \cf0 ;\
        cout \cf5 << 
\f1\b \cf3 '\cf4 \\n\cf3 '
\f0\b0 \cf0 ;\
    \}\
\}\

\f1\b \cf4 int 
\f0\b0 \cf0 main() \{\
    
\f1\b \cf4 int 
\f0\b0 \cf0 number;\
    \cf5 set \cf0 <\cf5 vector\cf0 <
\f1\b \cf4 int
\f0\b0 \cf0 >> a;\
    cin \cf5 >> \cf0 number;\
    ready(a, number);\
    cout \cf5 << \cf0 find_summ(a, number) \cf5 << 
\f1\b \cf3 '\cf4 \\n\cf3 '
\f0\b0 \cf0 ;\
    
\f2\i \cf8 //out(a);\

\f0\i0 \cf0 \}\
}