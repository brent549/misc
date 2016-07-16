#!/usr/bin/python
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def setBit(int_type,offset):
    mask = 1 << offset
    return(int_type | mask)

def clearBit(int_type , offset):
    mask = ~(1<<offset)
    return(int_type & mask)

def testBit(int_type, offset):
    mask = 1 << offset
    return(int_type & mask)

# get int then range of nums per line
(N,Q) = map(int,raw_input().strip().split(' '))
A = int(raw_input().rstrip(),2)
B = int(raw_input().rstrip(),2)

res=[]
#line=[]
for i in xrange(Q):
    #line = sys.stdin.readline().rstrip().split(' ')
    line = map(str,raw_input().strip().split(' '))
    cmd = line[0]
    offset = int(line[1])
    val = None
    if len(line) > 2:
        val = int(line[2])
    if cmd == "set_a":
        if val == 0:
            A = clearBit(A,offset)
        if val == 1:
            A = setBit(A,offset)
    if cmd == "set_b":
        if val == 0:
            B = clearBit(B,offset)
        if val == 1:
            B = setBit(B,offset)
    if cmd == "get_c":
        C = bin(A+B)
        if testBit(int(C,2),offset):
            res.append('1')
        else:
            res.append('0')
            
print "".join(res)

