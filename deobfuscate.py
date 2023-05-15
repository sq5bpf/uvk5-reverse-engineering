#!/usr/bin/python3
# quick hack to deobfuscate the UV-K5 communication
# (c) 2023 Jacek Lipkowski SQ5BPF <sq5bpf@lipkowski.org>

# usage:
# ./deobfuscate.py < sample_read.txt |less

# This program is licensed under the GNU GENERAL PUBLIC LICENSE v3
# License text avaliable at: http://www.gnu.org/copyleft/gpl.html 


import sys

def xorarr(arr):
    tbl=[ 22, 108, 20, 230, 46, 145, 13, 64, 33, 53, 213, 64, 19, 3, 233, 128]
    x=[]
    r=0
    for j in arr:
        x.append(j^tbl[r])
        r=(r+1)%len(tbl)
    return x

def hdump(arr):
    x=0
    print("######### dump len:",len(arr))
    for j in arr:
        print(hex(j)," ",end="")
    x+=1
    if x==16:
        x=0
    print("\n-------------------------------")
    for j in arr:
        c=chr(j)
        if not c.isprintable():
            c='.'
        print(c,end="")
    print("") 
    print("############################\n")



for line in sys.stdin:
    j=line.split()
    if len(j)<8:
        continue
    if (j[1]!="ab") or (j[2]!="cd")  :
        continue
    k=[]
    ofs=5
    for a in range(ofs,len(j)-4):
        k.append(int(j[a],16))
    print("line:",line)
    x=xorarr(k)
    hdump(xorarr(k))



    
