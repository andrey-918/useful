{\rtf1\ansi\ansicpg1251\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\fmodern\fcharset0 Courier-Bold;\f2\fmodern\fcharset0 Courier-Oblique;
}
{\colortbl;\red255\green255\blue255;\red109\green111\blue5;\red15\green112\blue3;\red0\green0\blue109;
\red14\green110\blue109;\red0\green0\blue254;\red109\green109\blue109;}
{\*\expandedcolortbl;;\csgenericrgb\c42745\c43529\c1961;\csgenericrgb\c5882\c43922\c1176;\csgenericrgb\c0\c0\c42745;
\csgenericrgb\c5490\c43137\c42745;\csgenericrgb\c0\c0\c99608;\csgenericrgb\c42745\c42745\c42745;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs40 \cf2 #include 
\f1\b \cf3 <iostream>\

\f0\b0 \cf2 #include 
\f1\b \cf3 <set>\

\f0\b0 \cf2 #include 
\f1\b \cf3 <vector>\
\cf4 using namespace 
\f0\b0 \cf5 std\cf0 ;\

\f1\b \cf4 void 
\f0\b0 \cf0 find_summ(\cf5 set\cf0 <\cf5 vector\cf0 <
\f1\b \cf4 int
\f0\b0 \cf0 >>& a, 
\f1\b \cf4 const int 
\f0\b0 \cf0 number) \{\
    \cf5 vector\cf0 <
\f1\b \cf4 int
\f0\b0 \cf0 > new_one;\
    
\f1\b \cf4 int 
\f0\b0 \cf0 finding = \cf6 2\cf0 ;\
    
\f1\b \cf4 while 
\f0\b0 \cf0 (finding != number) \{\
        
\f1\b \cf4 for 
\f0\b0 \cf0 (\cf5 vector\cf0 <
\f1\b \cf4 int
\f0\b0 \cf0 > x: a) \{\
            
\f1\b \cf4 int 
\f0\b0 \cf0 check = count(x.begin(), x.end(), \cf6 1\cf0 );\
            
\f1\b \cf4 if 
\f0\b0 \cf0 (check >= finding) \{\
                new_one \cf5 = \cf0 x;\
                new_one.erase(new_one.begin(), new_one.begin() \cf5 + \cf0 finding);\
                new_one.push_back(finding);\
            \}\
            a.insert(new_one);\
        \}\
        ++finding;\
    \}\
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
\f0\b0 \cf0 i = \cf6 0\cf0 ; i != number; ++i) \{\
        line.push_back(\cf6 1\cf0 );\
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
\f0\b0 \cf0 number, summ, repeat;\
    \cf5 set \cf0 <\cf5 vector\cf0 <
\f1\b \cf4 int
\f0\b0 \cf0 >> a;\
    cin \cf5 >> \cf0 number;\
    ready(a, number);\
    find_summ(a, number);\
    cout \cf5 << \cf0 a.size() + \cf6 1 \cf5 << 
\f1\b \cf3 "\cf4 \\n\cf3 "
\f0\b0 \cf0 ;\
    
\f2\i \cf7 //out(a);\

\f0\i0 \cf0 \}\
}