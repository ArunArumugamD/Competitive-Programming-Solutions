a='2x+y'
b='3x-5y'
res=[]
if a[0]!='-' and a[0]!='+':
    n_s='+'
    for i in a:
        n_s+=i
    a=n_s
if b[0]!='-' and b[0]!='+':
    n_s='+'
    for i in b:
        n_s+=i
    b=n_s

print(a,b)
def sign_chk(s):
    sign_lis=[]
    for i in range(len(s)):

         if s[i]=='+' or s[i]=='-':
            sign_lis.append(i)
    return sign_lis

def grp(s,lis):
    res=[]
    st = ''
    for i in range(s.__len__()):
        if i in lis:
            if not st:
                st+=s[i]

            else:
                res.append(st)
                st=''
                st+=s[i]


        else:
            st+=s[i]
            if i == len(s) - 1:
                res.append(st)

    return res







class LinkedList:
    def __init__(self):
        self.head=None
        self.curr=None
        self.count=0

    def addEQ(self,co_eff,x,y,z):
        if self.head == None:
            self.head = self.Node(co_eff,x,y,z)
            self.curr = self.head

        else:
            self.curr.next = self.Node(co_eff,x,y,z)
            self.curr = self.curr.next
        self.count += 1
    def trav(self):
        c = self.head

        while (c):
            print(c.co_eff,c.x,c.y,c.z)
            c=c.next
    class Node:
        def __init__(self,co_eff,x,y,z):
            self.co_eff=co_eff
            self.x=x
            self.y=y
            self.z=z
            self.next=None




def char_check(s):
    res=[]
    for i in range(len(s)):
        if s[i] =='x' or s[i]=='y' or s[i]=='z' or s[i]=='+'or s[i]=='-':
            res.append(i)
    res.append(len(s))
    return res


def insert_eq(chk,grp):
    res=[]
    for i in  range(len(chk)-1):

        st=grp[chk[i]:chk[i+1]]
        res.append(st)
    return res

def EQ(st):
    res=grp(st,sign_chk(st))

    chk =[char_check(i) for i in res]
    f_lis=[]
    for i in range(len(chk)):
        f_lis.append(insert_eq(chk[i],res[i]))

    eq=LinkedList()


    for i in f_lis:
        co_eff=0
        x=0
        y=0
        z=0
        for j in i:
            if '+' in j  or '-' in j:
                if j=='+' or j=='-':
                    if j=='+':
                        co_eff=1
                    else:
                        co_eff=-1
                else:
                    co_eff=int(j)
            if 'x' in j :
                if '^' in j:
                    x=int(j[2:])
                else:
                    x=1
            if 'y' in j :
                if '^' in j:
                    y=int(j[2:])
                else:
                    y=1
            if 'z' in j :
                if '^' in j:
                    z=int(j[2:])
                else:
                    z=1
        eq.addEQ(co_eff,x,y,z)
    return eq

a=EQ(a)
b=EQ(b)
a.trav()
print(a.count)
b.trav()
print(b.count)

a_c=a.head
b_c=b.head

def mult(o1,o2):
    res=[]
    t=o1.co_eff * o2.co_eff
    if t<0:
        t=str(t)
    else:
        t='+'+str(t)

    res.append(t)
    res.append( 'x'+str((o1.x+o2.x)) )
    res.append( 'y'+str((o1.y + o2.y)) )
    res.append('z'+str((o1.z + o2.z)))
    return res
for i in range(a.count):
    for j in range(b.count):
        res=mult(a_c,b_c)
        for i in res:
            print(i,end='')
        b_c=b_c.next
    b_c=b.head
    a_c=a_c.next
