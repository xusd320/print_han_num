# coding=utf-8
a=-1214567090000
b=abs(a)
def digits(x):
    nums=[]
    while 1:
        if x!=0:
            y =x%10000
            num=[]
            while 1:
                if y!=0:
                    z=y%10
                    y=int(y/10)
                    num.append(z)
                else:
                    break
            x=int(x/10000)
            nums.append(num)
        else:
            break
    return nums

def conver(x):

    l=digits(x)
    numl=[['','拾','佰','仟'],['万','拾','佰','仟'],['亿','拾','佰','仟'],['兆','拾','佰','仟']]
    numdict={0:'',1:'壹',2:'贰',3:'叁',4:'肆',5:'伍',6:'陆',7:'柒',8:'捌',9:'玖'}
    pnum=[]
    for i in range(len(l)):
        for j in range(len(l[i])):
            pnum.append(numdict[l[i][j]] + numl[i][j])
    pnum=['零' if h in ['拾','佰','仟'] else h for h in pnum]

    return ''.join(pnum[::-1])
str=conver(b) + '圆' if a>=0 else '负' + conver(b) + '圆'
print(str)
