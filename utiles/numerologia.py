# -*- coding: utf-8 -*-

p = 5040        # 7!
q = 479001600   # 12!

c1=[x for x in range(p) if x%1==0]
c2=[x for x in range(p) if x%2==0]
c3=[x for x in range(p) if x%3==0]
c4=[x for x in range(p) if x%4==0]
c5=[x for x in range(p) if x%5==0]
c6=[x for x in range(p) if x%6==0]
c7=[x for x in range(p) if x%7==0]
c8=[x for x in range(p) if x%8==0]
c9=[x for x in range(p) if x%9==0]
c10=[x for x in range(p) if x%10==0]
c11=[x for x in range(p) if x%11==0]
c12=[x for x in range(p) if x%12==0]

log_ratios = [round(2/(2**(a/12)),3) for a in range(12)]
log_ratios.reverse()
pitag_ratios = [1, 9/8, 81/64, 4/3, 3/2, 27/16, 243/128, 2]

sets = [set(), set(c1), set(c2), set(c3), set(c4), set(c5),set(c6),set(c7),set(c8),set(c9),set(c10),set(c11),set(c12)]

def harmd(n):
    return [n,n/2,n/3,n/4,n/5,n/6,n/7,n/8]

def harma(n):
    return [n,n*2,n*3,n*4,n*5,n*6,n*7,n*8]

def base10toN(num,n):
    """Change a  to a base-n number.
    Up to base-36 is supported without special notation."""
    num_rep={10:'a',
         11:'b',
         12:'c',
         13:'d',
         14:'e',
         15:'f',
         16:'g',
         17:'h',
         18:'i',
         19:'j',
         20:'k',
         21:'l',
         22:'m',
         23:'n',
         24:'o',
         25:'p',
         26:'q',
         27:'r',
         28:'s',
         29:'t',
         30:'u',
         31:'v',
         32:'w',
         33:'x',
         34:'y',
         35:'z'}
    new_num_string=''
    current=num
    while current!=0:
        remainder=current%n
        if 36>remainder>9:
            remainder_string=num_rep[remainder]
        elif remainder>=36:
            remainder_string='('+str(remainder)+')'
        else:
            remainder_string=str(remainder)
        new_num_string=remainder_string+new_num_string
        current=current/n
    return new_num_string
