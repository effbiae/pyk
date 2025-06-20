from p import p,P;import sys
def ev(x):
 try:return int(x)
 except:pass
 if x[0]=='!':return tuple(range(ev(x[1])))
 if type(x[0])==tuple:
  if len(x)==2:return adv(x[0],0,ev(x[1]))
  else:return adv(x[0],ev(x[1]),ev(x[2]))
 if type(x)==tuple:
  if x[0]in"\\/'":return ev(x[1])+x[0]
 if x in P:return x
 print(x);assert(0)
def accu_(f,y,z):
 if not len(z):return()
 assert(len(z));r0=f(y,z[0]);return (r0,)+(accu_(f,r0,z[1:])if 1<len(z)else())
def accum1(f,y,z):return accu_(f,y,z)
def accum0(f,z):
 if not len(z):return()
 return (z[0],)+accu_(f,z[0],z[1:])
def scan(x,y,z):
 if x=='+':
  if y==0:return accum0(lambda x,y:x+y,z)
  else:return accum1(lambda x,y:x+y,y,z)
ad={'\\':scan,'/':None,"'":None}
def adv(x,y,z):return ad[x[0]](x[1],y,z)
f=sys.stdin
while 1:
 x=f.readline()
 if not x:break
 x=p(x.strip())
 print(x)
 print(ev(x))
